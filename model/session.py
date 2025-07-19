from datetime import datetime
from typing import List

class Session:
    def __init__(self, session_id: str, mode: str, timestamp: datetime, player_name: str, 
                 score: int, duration: float, words_used: List[str], correct_count: int, wrong_count: int):
        self.session_id = session_id
        self.mode = mode
        self.timestamp = timestamp
        self.player_name = player_name
        self.score = score
        self.duration = duration
        self.words_used = words_used
        self.correct_count = correct_count
        self.wrong_count = wrong_count