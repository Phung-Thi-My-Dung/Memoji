import numpy as np
from datetime import datetime
# from ulti.logger import Logger

class BaseWord:
    def __init__(self, word):
        """
        Initialize a Word object with the required 'word' field.

        Attributes:
            - word (str): the vocabulary word
            - pos (str): part of speech (e.g., noun, verb, adj)
            - emoji (str): emoji representing the meaning
            - vietnamese_translation (str): meaning in Vietnamese
            - english_meaning (str): explanation in English
            - created_date (str): timestamp of creation
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


