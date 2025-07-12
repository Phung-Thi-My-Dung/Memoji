import json
from datetime import datetime

class HistoryManager:
    def __init__(self, filepath='data/history.json'):
        self.filepath = filepath

    def save_session(self, word, correct, time_taken):
        try:
            with open(self.filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
        except:
            data = []

        data.append({
            "word": word,
            "correct": correct,
            "time_taken": time_taken,
            "timestamp": datetime.now().isoformat()
        })

        with open(self.filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
