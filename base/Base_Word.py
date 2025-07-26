import numpy as np
from datetime import datetime
# from ulti.logger import Logger

class BaseWord:
    def __init__(self, word):
        """
        Baseword chứa định nghĩa chung cơ bản nhất cho một từ.
        Nó dùng để định nghĩa các thuộc tính và phương thức cơ bản cho từ,
        bao gồm các phương thức để lấy và thiết lập các thuộc tính cơ bản.
        Attributes:
            - word (str): từ cần định nghĩa
            - pos (str): từ loại của từ
            - emoji (str): biểu tượng cảm xúc liên quan đến từ
            - meaning (str): nghĩa của từ
            - created_date (str): ngày tạo từ, định dạng dd/mm/yyyy hh:mm:ss
        Những thuộc tính này sẽ được sử dụng trong các lớp con để mở rộng và định nghĩa các thuộc tính khác.
        """
        if not isinstance(word, str):
            raise TypeError("Word must be a string.")
        
        self.word = word.strip()
        self.pos = None
        # self.emoji = None
        self.meaning = None

    # ---------- SETTERS ----------
    def set_pos(self, pos):
        self.pos = pos.strip() if isinstance(pos, str) else None

    def set_meaning(self, meaning):
        self.meaning = meaning.strip() if isinstance(meaning, str) else None

    # ---------- GETTERS ----------
    def get_word(self):
        return self.word

    def get_pos(self):
        return self.pos
    
    def get_meaning(self):
        return self.meaning

    # ---------- REPRESENTATION ----------
    def to_string(self):
        """Returns a brief summary string of the word"""
        return f"'{self.word}' was created on {self.created_date}"


