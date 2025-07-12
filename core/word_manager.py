import pandas as pd

class WordManager:
    def __init__(self, filepath='db/words.xlsx'):
        self.filepath = filepath
        self.words = self.load_words()

    def load_words(self):
        try:
            df = pd.read_excel(self.filepath)
            return df['word'].tolist() if 'word' in df.columns else []
        except Exception as e:
            print(f"Error loading words from {self.filepath}: {e}")
            return []           

    def get_random_word(self):
        import random
        return random.choice(self.words)
