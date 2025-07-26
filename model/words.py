import numpy as np
from datetime import datetime
from base import BaseWord

class Word(BaseWord):
    def __init__(self, word):
        """
        Word là định nghĩa mở rộng từ BaseWord,
        bao gồm các thuộc tính và phương thức cụ thể cho từ trong hệ thống.
        Nó kế thừa các thuộc tính cơ bản từ BaseWord và thêm các thuộc tính mới
        như vietnamese_translation, english_meaning và created_date. Phục vụ cho việc định nghĩa
        word của game 
        Attributes:
            - word (str): từ cần định nghĩa
            - pos (str): từ loại của từ
            - emoji (str): biểu tượng cảm xúc liên quan đến từ
            - vietnamese_translation (str): nghĩa của từ bằng tiếng Việt
            - english_meaning (str): nghĩa của từ bằng tiếng Anh
            - created_date (str): ngày tạo từ, định dạng dd/mm/yyyy hh:mm:ss
        
        Đối với game nó dùng đễ đối tượng dữ liệu từ file và dữ liệu được người dùng nhập trong game
        sau đó sẽ chuyển các dữ liệu đó thành đối tượng để tương tác với game.
        """
        super().__init__(word)  # Call parent class constructor
        self.vietnamese_translation = None
        self.english_meaning = None
        self.created_date = self._get_datetime()

    def _get_datetime(self):
        """Returns current date and time in format dd/mm/yyyy hh:mm:ss"""
        return datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    
    # ---------- SETTERS ----------
    def set_vietnamese_translation(self, translation):
        self.vietnamese_translation = translation.strip() if isinstance(translation, str) else None

    def set_english_meaning(self, meaning):
        self.english_meaning = meaning.strip() if isinstance(meaning, str) else None

    # ---------- GETTERS ----------
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
            "vietnamese_translation": self.vietnamese_translation,
            "english_meaning": self.english_meaning,
            "created_date": self.created_date
        }

        has_missing = False
        for field_name, value in required_fields.items():
            status = "✔" if value else "✘"
            print(f"{status} {field_name} {'is filled' if value else 'is missing'}.")
            has_missing = has_missing or not value

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


# if __name__ == "__main__":
#     # Example usage
#     word = Word("example")
#     word.set_pos("noun")
#     word.set_emoji("📘")
#     word.set_vietnamese_translation("ví dụ")
#     word.set_english_meaning("a representative form or pattern")

#     print(word)
#     print(word.is_valid())
#     print(word.to_string())