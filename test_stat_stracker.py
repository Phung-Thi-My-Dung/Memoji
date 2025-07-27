# import tkinter as tk
# from tkinter import filedialog, messagebox
# import os
# import subprocess # Để mở file bằng ứng dụng mặc định

# def open_file_dialog():
#     # Mở hộp thoại chọn file
#     file_path = filedialog.askopenfilename(
#         title="Chọn một file",
#         filetypes=[
#             ("Tất cả các file", "*.*"), # Tùy chọn, bạn có thể chỉ định loại file cụ thể
#             ("File văn bản", "*.txt"),
#             ("File Python", "*.py")
#         ]
#     )

#     if file_path: # Nếu người dùng đã chọn một file
#         try:
#             # Hiển thị đường dẫn file đã chọn
#             status_label.config(text=f"Đường dẫn file đã chọn: {file_path}")

#             # Mở file bằng ứng dụng mặc định của hệ điều hành
#             # Windows: os.startfile(file_path)
#             # macOS: subprocess.call(['open', file_path])
#             # Linux: subprocess.call(['xdg-open', file_path])

#             if os.name == 'nt':  # Windows
#                 os.startfile(file_path)
#             elif os.uname().sysname == 'Darwin':  # macOS
#                 subprocess.call(['open', file_path])
#             else:  # Linux
#                 subprocess.call(['xdg-open', file_path])

#             messagebox.showinfo("Thành công", f"Đã mở file: {file_path}")

#         except Exception as e:
#             messagebox.showerror("Lỗi", f"Không thể mở file: {e}")
#     else:
#         status_label.config(text="Chưa chọn file nào.")

# # Tạo cửa sổ chính
# root = tk.Tk()
# root.title("Ứng dụng mở file")
# root.geometry("400x200")

# # Tạo một nhãn để hiển thị trạng thái hoặc đường dẫn file
# status_label = tk.Label(root, text="Chưa chọn file nào.", wraplength=350)
# status_label.pack(pady=20)

# # Tạo nút để mở hộp thoại chọn file
# open_button = tk.Button(root, text="Chọn và mở File", command=open_file_dialog)
# open_button.pack(pady=10)

# # Chạy vòng lặp sự kiện chính của Tkinter
# root.mainloop()