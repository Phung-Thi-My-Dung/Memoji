import pandas as pd

# Dữ liệu stat
df_stat = pd.DataFrame([
    [1, 120, 80, "normal", "completed", "S001", "2025-07-01 09:15:00"],
    [2, 90, 70, "hard", "completed", "S002", "2025-07-02 10:30:00"],
    [3, 100, 60, "normal", "incomplete", "S003", "2025-07-02 15:00:00"],
    [4, 110, 85, "normal", "completed", "S004", "2025-07-03 14:20:00"],
    [5, 95, 75, "hard", "completed", "S005", "2025-07-05 18:45:00"],
], columns=["id", "play_time", "score", "mode", "status", "session_id", "Datetime"])

# Dữ liệu session
df_session = pd.DataFrame([
    ["S001", "normal", "2025-07-01 09:15:00", 80, 120, "apple,banana,cat", "2025-07-01 09:15:00", 1],
    ["S002", "hard", "2025-07-02 10:30:00", 70, 90, "orange,pear,grape", "2025-07-02 10:30:00", 2],
    ["S003", "normal", "2025-07-02 15:00:00", 60, 100, "cat,dog,fish", "2025-07-02 15:00:00", 0],
    ["S004", "normal", "2025-07-03 14:20:00", 85, 110, "car,bike,train", "2025-07-03 14:20:00", 1],
    ["S005", "hard", "2025-07-05 18:45:00", 75, 95, "book,pen,pencil", "2025-07-05 18:45:00", 2],
], columns=["id_session", "mode", "time_stamp", "score", "duration", "words_used", "Datetime", "wrong_word_count"])

# Ghi file Exceld
df_stat.to_excel("db/stat.xlsx", index=False)
df_session.to_excel("db/session.xlsx", index=False)