import time

class GameEngine:
    def __init__(self, word):
        self.word = word
        self.start_time = None
        self.end_time = None

    def start(self):
        self.start_time = time.time()
        print("Câu ví dụ:", self.word["example_sentence"])
        print("Từ cần nối:", self.word["english"])
        # Gợi ý: in từng ký tự một để nối

    def end(self):
        self.end_time = time.time()

    def get_duration(self):
        return round(self.end_time - self.start_time, 2)
