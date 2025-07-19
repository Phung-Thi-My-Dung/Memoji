from typing import Dict, List
from ulti.logger import Logger

class StatsTracker:
    def __init__(self, logger: Logger):
        self.logger = logger
        self.correct_answers: Dict[str, int] = {}
        self.wrong_answers: Dict[str, List[str]] = {}
        self.correct_count = 0
        self.wrong_count = 0
        self.total_duration = 0.0

    def reset(self):
        self.correct_answers = {}
        self.wrong_answers = {}
        self.correct_count = 0
        self.wrong_count = 0
        self.total_duration = 0.0

    def record_correct(self, word: str):
        self.correct_count += 1
        self.correct_answers[word] = self.correct_answers.get(word, 0) + 1
        self.logger.log_info(f"Recorded correct answer for word: {word}")

    def record_wrong(self, word: str, user_answer: str):
        self.wrong_count += 1
        if word not in self.wrong_answers:
            self.wrong_answers[word] = []
        self.wrong_answers[word].append(user_answer)
        self.logger.log_info(f"Recorded wrong answer for word: {word}, answer: {user_answer}")

    def update_stats(self, correct: int, wrong: int, duration: float):
        self.correct_count += correct
        self.wrong_count += wrong
        self.total_duration += duration