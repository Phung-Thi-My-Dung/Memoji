import numpy as np
from datetime import datetime

class Word:
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
        self.emoji = None
        self.vietnamese_translation = None
        self.english_meaning = None
        self.created_date = self._get_datetime()

    def _get_datetime(self):
        """Returns current date and time in format dd/mm/yyyy hh:mm:ss"""
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    # ---------- SETTERS ----------
    def set_pos(self, pos):
        self.pos = pos.strip() if isinstance(pos, str) else None

    def set_emoji(self, emoji):
        self.emoji = emoji.strip() if isinstance(emoji, str) else None

    def set_vietnamese_translation(self, translation):
        self.vietnamese_translation = translation.strip() if isinstance(translation, str) else None

    def set_english_meaning(self, meaning):
        self.english_meaning = meaning.strip() if isinstance(meaning, str) else None

    # ---------- GETTERS ----------
    def get_word(self):
        return self.word

    def get_pos(self):
        return self.pos

    def get_emoji(self):
        return self.emoji

    def get_vietnamese_translation(self):
        return self.vietnamese_translation

    def get_english_meaning(self):
        return self.english_meaning

    def get_created_date(self):
        return self.created_date

    # ---------- VALIDATION ----------
    def is_valid(self):
        """
        Check which required fields are filled and which are missing.
        Prints each field's status.

        Required fields: word, pos, vietnamese_translation, english_meaning
        Emoji is optional and excluded from the check.
        """
        required_fields = {
            "word": self.word,
            "pos": self.pos,
            "emoji": self.emoji,
            "vietnamese_translation": self.vietnamese_translation,
            "english_meaning": self.english_meaning,
            "created_date": self.get_created_date()
        }

        has_missing = False
        for field_name, value in required_fields.items():
            if value:
                print(f"✔ {field_name} is filled.")
            else:
                print(f"✘ {field_name} is missing.")
                has_missing = True

        return not has_missing

    # ---------- REPRESENTATION ----------
    def to_string(self):
        """Returns a brief summary string of the word"""
        return f"'{self.word}' was created on {self.created_date}"

    def __repr__(self):
        """Detailed representation of the Word object"""
        return (f"Word('{self.word}', POS={self.pos}, Emoji={self.emoji}, "
                f"VN={self.vietnamese_translation}, EN={self.english_meaning}, "
                f"Created={self.created_date})")
