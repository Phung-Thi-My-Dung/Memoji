from core import StatsTracker

if __name__ == "__main__":
    tracker = StatsTracker(start_date="2025-07-01", end_date="2025-07-31")
    tracker.generate_all()

    print("📊 Báo cáo thống kê:")
    print(tracker.df_stat)

    print("🖼️ Đã lưu biểu đồ vào file summary_plot.png")