from core import WordManager
from model import Word
import pandas as pd

if __name__ == "__main__":
    # Example usage
    word_manager_instance = WordManager()
    
    # Create a new Word object
    new_word = Word("example")
    new_word.set_pos("noun")
    new_word.set_vietnamese_translation("ví dụ")
    new_word.set_english_meaning("an instance of something")
    
    # Enter the word into the game
    word_manager_instance.enter_word(new_word)
    
    print("Word entered successfully!")

    test_word_df = pd.read_excel("test_word.xlsx")
    word_manager_instance.load_file_word(test_word_df)
