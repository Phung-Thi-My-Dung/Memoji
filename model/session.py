from datetime import datetime

class Session:
    def __init__(self, word: str, correct: bool, time_taken: float, timestamp: str = None):
        self.word = word
        self.correct = correct
        self.time_taken = time_taken
        self.timestamp = timestamp or datetime.now().isoformat()

    def to_dict(self):
        return {
            "word": self.word,
            "correct": self.correct,
            "time_taken": self.time_taken,
            "timestamp": self.timestamp
        }

    @staticmethod
    def from_dict(data: dict):
        return Session(
            word=data["word"],
            correct=data["correct"],
            time_taken=data["time_taken"],
            timestamp=data.get("timestamp")
        )
