import pandas as pd
from typing import List, Optional
from model import Word, FileHandler, WrongWord
from config import Setting

class WordManager:
    def __init__(self):
        """"
        Dùng trong việc thực hiện các chức năng liên quan đến từ vựng trong game
        có thể add thông qua file
        thông qua nhấn từ vào
        Tìm kiếm và chỉnh sửa từ trên file word.xlsx là file chứa từ vựng của game từ quá khứ đến hiện tại.
        tương tác với file wrong_word.xlsx là file chứa từ vựng sai của người chơi.
        """
    
    def enter_word(self, word: Word):
        """
        Dùng cho việc người dùng nhập từ vào game
        
        Args:
            word (Word): Đối tượng Word chứa thông tin từ cần thêm.
        """
        file_word = FileHandler(file_path= Setting().db_path, file_name= "words", file_type= "xlsx").read_file_excel()
        _last_record = file_word.iloc[-1] if not file_word.empty else None
        # Khởi tạo ID mới cho từ
        word.id = Setting().generate_next_id(_last_record['id']) if _last_record is not None else "w000001"
        new_word_data = {
            "id": word.id,
            "word": word.word,
            "pos": word.pos,
            "meanings": word.english_meaning,
            "vietnamese_translation": word.vietnamese_translation,
            "created_date": word.created_date
        }
        new_df = pd.DataFrame([new_word_data])
        # Append the new word to the existing DataFrame
        file_word = pd.concat([file_word, new_df], ignore_index=True)
        # Save the updated DataFrame back to the Excel file
        file_word.to_excel(Setting().db_path + "/words.xlsx", index=False)

    def load_file_word(self, df) -> pd.DataFrame:
        """
        Đưa dữ liệu từ người chơi nhập vào file_word.xlsx
        Đưa vào db words.py
        """
        for i in range(len(df)):
            word = Word(df.iloc[i]['word'])
            word.set_pos(df.iloc[i]['pos'])
            word.set_english_meaning(df.iloc[i]['meanings'])
            word.set_vietnamese_translation(df.iloc[i]['vietnamese_translation'])
            self.enter_word(word)

    def load_file_wrong_word(self, df: pd.DataFrame) -> List[WrongWord]:
        """
        Đưa dữ liệu từ người chơi nhập vào file_wrong_word.xlsx
        Đưa vào db wrong_word.py
        """
        wrong_words = []
        for i in range(len(df)):
            wrong_word = WrongWord(df.iloc[i]['word'])
            wrong_word.set_pos(df.iloc[i]['pos'])
            wrong_word.set_english_meaning(df.iloc[i]['meanings'])
            wrong_word.set_vietnamese_translation(df.iloc[i]['vietnamese_translation'])
            wrong_words.append(wrong_word)
        return wrong_words
    

        
        
        




