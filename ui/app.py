import tkinter as tk
from tkinter import messagebox
from core.word_manager import WordManager
from core.stats_tracker import StatsTracker
from core.history_manager import HistoryManager
from utils.logger import get_logger
from utils.timer import Timer
from models.session import Session
from models.word import Word

class WordGameApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Word Game App")
        self.master.geometry("400x300")

        self.logger = get_logger()
        self.word_manager = WordManager()
        self.stats = StatsTracker()
        self.history = HistoryManager()

        self.current_word = None
        self.timer = Timer()

        self.create_widgets()
        self.next_round()

    def create_widgets(self):
        self.label_sentence = tk.Label(self.master, text="", wraplength=380, font=("Arial", 12))
        self.label_sentence.pack(pady=10)

        self.label_hint = tk.Label(self.master, text="", font=("Arial", 10, "italic"))
        self.label_hint.pack(pady=5)

        self.entry = tk.Entry(self.master, font=("Arial", 14))
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.check_answer)

        self.button = tk.Button(self.master, text="Kiểm tra", command=self.check_answer)
        self.button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.pack(pady=5)

    def next_round(self):
        self.result_label.config(text="")
        self.entry.delete(0, tk.END)
        self.current_word = Word.from_dict(self.word_manager.get_random_word())
        self.label_sentence.config(text=f"Câu ví dụ: {self.current_word.example_sentence}")
        self.label_hint.config(text=f"Gợi ý: {len(self.current_word.english)} ký tự")
        self.timer.reset()
        self.timer.start()

    def check_answer(self, event=None):
        user_input = self.entry.get().strip().lower()
        self.timer.stop()
        time_taken = self.timer.elapsed()

        is_correct = user_input == self.current_word.english.lower()

        if is_correct:
            self.result_label.config(text="✅ Đúng rồi!", fg="green")
        else:
            self.result_label.config(
                text=f"❌ Sai! Đáp án đúng: {self.current_word.english}", fg="red"
            )

        self.stats.record(is_correct, time_taken)
        session = Session(self.current_word.english, is_correct, time_taken)
        self.history.save_session(session)
        self.logger.info(f"word={self.current_word.english}, input={user_input}, correct={is_correct}, time={time_taken}")

        self.master.after(2000, self.next_round)

def run_app():
    root = tk.Tk()
    app = WordGameApp(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()
