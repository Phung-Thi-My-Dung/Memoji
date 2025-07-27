import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
from typing import Dict
from model import Statistic, FileHandler, Session
from config import Setting

class StatsTracker:
    def __init__(self, start_date, end_date):
        self.statistics = Statistic()
        self.df_session = None
        self.start_date = start_date
        self.end_date = end_date
        self.df_stat = pd.DataFrame()

    def add_data_stat(self):
        path = Setting().db_path 
        name = "stat"
        type=   "xlsx"
        self.statistics.data = FileHandler(file_path=path, file_name= name, file_type=type).read_file_excel()

    def add_data_session(self):
        path = Setting().db_path 
        name = "session"
        type=   "xlsx"

        self.df_session = FileHandler(file_path=path, file_name= name, file_type=type).read_file_excel()
        self.df_session["Datetime"] = pd.to_datetime(self.df_session["Datetime"], errors='coerce')
        self.df_session = self.filter_by_range(self.df_session, self.start_date, self.end_date)
        self.df_session["date"] = self.df_session["Datetime"].dt.date
        self.df_session["month"] = self.df_session["Datetime"].dt.to_period("M")
        self.df_session["week"] = self.df_session["Datetime"].dt.to_period("W")

    def filter_by_range(self, df, start_date, end_date):
        return df[(df["Datetime"] >= start_date) & (df["Datetime"] <= end_date)]

    def avg_sessions_per_day(self):
        return self.df_session.groupby("date")["id_session"].count().mean()

    def total_wrong_word_count(self):
        if "wrong_word_count" not in self.df_session.columns:
            return 0
        return self.df_session["wrong_word_count"].sum()

    def generate_summary_report_df(self):
        """
        Lưu report dưới dạng DataFrame vào self.df_stat
        """
        summary = {
            "avg_sessions_per_day": [self.avg_sessions_per_day()],
            "total_wrong_word_count": [self.total_wrong_word_count()],
        }
        self.df_stat = pd.DataFrame(summary)

    def save_all_plots(self, save_path="summary_plot.png"):
        """
        Vẽ và lưu các biểu đồ thống kê vào 1 file ảnh duy nhất.
        """
        fig, axes = plt.subplots(1, 2, figsize=(16, 6))
        fig.suptitle("Thống kê người chơi", fontsize=16)

        # Biểu đồ 1: số ngày chơi theo tháng
        days_played = self.df_session.groupby("month")["date"].nunique()
        days_played.plot(kind="bar", ax=axes[0], title="Số ngày chơi mỗi tháng")
        axes[0].set_ylabel("Số ngày")

        # Biểu đồ 2: số từ học mỗi ngày
        if "words_used" in self.df_session.columns:
            self.df_session["num_words_learned"] = self.df_session["words_used"].fillna("").apply(lambda x: len(x.split(",")))
            words_per_day = self.df_session.groupby("date")["num_words_learned"].sum()
            words_per_day.plot(kind="line", ax=axes[1], marker='o', title="Số từ học mỗi ngày")
            axes[1].set_ylabel("Số từ")
            axes[1].tick_params(axis='x', labelrotation=45)

        plt.tight_layout(rect=[0, 0.03, 1, 0.95])
        plt.savefig(save_path)
        plt.close(fig)

    def generate_all(self):
        """
        Chạy toàn bộ thống kê: load dữ liệu, lưu bảng summary và lưu ảnh.
        """
        self.add_data_stat()
        self.add_data_session()
        self.generate_summary_report_df()
        self.save_all_plots()
