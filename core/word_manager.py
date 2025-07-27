import pandas as pd
from typing import List, Optional
from model.words import Word
from datetime import datetime

class WordManager:
    def __init__(self, file_path: str,):
        self.file_path = file_path
        self.words = self.load_words()

    def load_words(self) -> List[Word]:
        try:
            df = pd.read_excel(self.file_path)
            words = []
            for _, row in df.iterrows():
                word = Word(
                    word=row["word"]
                )
                word.set_pos(row.get("pos", ""))
                word.set_vietnamese_translation(row.get("vietnamese_translation", ""))
                word.set_english_meaning(row.get("english_meaning", ""))
                word.set_emoji(row.get("emoji", ""))
                word.created_date = row.get("created_date", datetime.now().strftime("%d/%m/%Y %H:%M:%S"))

                words.append(word)
            return words
        except Exception as e:
            return []
        
    def get_words(self, max_words: int = 10, category: Optional[str] = None) -> List[Word]:
        filtered_words = self.words
        if category:
            filtered_words = [w for w in self.words if w.category == category]
        return filtered_words[:max_words]