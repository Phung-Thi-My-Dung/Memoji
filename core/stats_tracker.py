from typing import Dict, List
from model import Statistic
from model import FileHandler
from model import Session
from config import Setting
import seaborn as sns
import pandas as pd
import os
import base64 # To embed images in HTML
import matplotlib.pyplot as plt

class StatsTracker:
    def __init__(self, start_date, end_date):
        """
            Dùng để hiển thị các thông tin về thống kê html cho người choi
            có thể lấy ra để xem chi tiết thống kê về các lượt chơi của người chơi.
            Dùng dữ liệu của stat.py có lưu lại thông tin chi tiết về các lượt chơi.
        Args:
            start_date (str): Ngày bắt đầu trong file thống kê cần lấy.
            end_date (str): Ngày kết thúc file thống kê cần lấy. 
        """
        self.statistics = Statistic()
        self.df_session = None # Lấy session liên kết để tính được stat
        self.start_date = None
        self.end_date = None
        self.df_stat = pd.DataFrame() # Hiện ra cho người dùng xem stat cụ thể đã làm được gì
    
    def add_data_stat(self):
        """        Add data to the statistics object.
        """
        path_full_data = Setting().db_path + "stat.xlsx"
        self.statistics.data = FileHandler().read_file_excel(path_full_data)
    
    def add_data_session(self):
        """
        Add data to the session object.
        """
        path_full_data = Setting().db_path + "session.xlsx"
        self.df_session = FileHandler().read_file_excel(path_full_data)
        # Tách dữ liệu ngày tháng ra bên ngoài
        self.df_session = self.filter_by_range(self.df_session, self.start_date, self.end_date)
        
        # Cái đặt ngày tháng

        self.df_session["date"] = self.df_session["Datetime"].dt.date
        self.df_session["month"] = self.df_session["Datetime"].dt.to_period("M")
        self.df_session["week"] = self.df_session["Datetime"].dt.to_period("W")

        
    def filter_by_range(df, start_date, end_date):
            return df[(df["Datetime"] >= start_date) & (df["Datetime"] <= end_date)]
    
    def avg_sessions_per_day(self):
        avg_sessions_per_day = self.df_session.groupby("date")["id_session"].count().mean()
        return avg_sessions_per_day

    def plot_avg_sessions_per_day(self, type = "month"):
        # Đếm số ngày có chơi trong từng tháng
        days_played_per_month = self.df_session.groupby(type)["date"].nunique()

        # Plot
        days_played_per_month.plot(kind="bar", title="Số ngày chơi mỗi tháng")
        plt.ylabel("Số ngày")
        plt.show()
         
    def total_wrong_word_count(self):
         total_wrong_words = self.df_session["wrong_word_count"].sum()
         return total_wrong_words
    
    def total_words_used(self):
        # Giả sử "words_used" là danh sách từ cách nhau bởi dấu phẩy
        self.df_session["num_words_learned"] = self.df_session["words_used"].fillna("").apply(lambda x: len(x.split(",")))

        words_per_day = self.df_session.groupby("date")["num_words_learned"].sum()

        # Plot
        words_per_day.plot(kind="line", marker='o', title="Số từ học mỗi ngày")
        plt.ylabel("Số từ")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    


         
         
         