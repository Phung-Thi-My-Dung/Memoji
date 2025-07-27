import random
from typing import List, Optional
from model.words import Word
from model.session import Session
from word_manager import WordManager
from stats_tracker import StatsTracker
from history_manager import HistoryManager
from datetime import datetime

class GameEngine:
    def __init__(self, config: dict, word_manager: WordManager, stats_tracker: StatsTracker, 
                 history_manager: HistoryManager, timer: Timer, logger: Logger):
        self.config = config
        self.word_manager = word_manager
        self.stats_tracker = stats_tracker
        self.history_manager = history_manager
        self.timer = timer
        self.logger = logger
        self.session_id = f"session_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        self.player_name = config.get("player_name", "Anonymous")
        self.words_in_session: List[Word] = []
        self.correct_count = 0
        self.wrong_count = 0
        self.score = 0
        self.mode = None

    def start_session(self, mode: str):
        self.mode = mode
        self.logger.log_info(f"Starting new game session: {self.session_id}, Mode: {mode}")
        self.timer.start()
        self.words_in_session = []
        self.correct_count = 0
        self.wrong_count = 0
        self.score = 0
        self.stats_tracker.reset()

    def get_next_word(self) -> Optional[Word]:
        available_words = self.word_manager.get_words(
            max_words=self.config.get("max_questions", 10)
        )
        available_words = [w for w in available_words if w not in self.words_in_session]
        if not available_words:
            self.logger.log_warning("No more available words for this session.")
            return None
        word = random.choice(available_words)
        self.words_in_session.append(word)
        self.logger.log_info(f"Selected word: {word.word}")
        return word

    def check_answer(self, word: Word, user_answer: str) -> bool:
        is_correct = False
        if self.mode == "mode1":
            is_correct = user_answer.strip().lower() == word.meanings_english.lower()
        elif self.mode == "mode2":
            is_correct = user_answer.strip().lower() == word.meanings_vietnamese.lower()
        elif self.mode == "mode3":
            is_correct = user_answer.strip().lower() == word.pos.lower()
        
        if is_correct:
            self.correct_count += 1
            self.score += self.config.get("points_per_correct", 10)
            self.stats_tracker.record_correct(word.word)
            self.logger.log_info(f"Correct answer: {user_answer} for word {word.word}")
        else:
            self.wrong_count += 1
            self.stats_tracker.record_wrong(word.word, user_answer)
            self.logger.log_info(f"Wrong answer: {user_answer} for word {word.word}")
        return is_correct

    def end_session(self) -> Session:
        duration = self.timer.stop()
        self.logger.log_info(f"Session {self.session_id} ended. Duration: {duration}s, Score: {self.score}")
        
        session = Session(
            session_id=self.session_id,
            mode=self.mode,
            timestamp=datetime.now(),
            player_name=self.player_name,
            score=self.score,
            duration=duration,
            words_used=[word.word for word in self.words_in_session],
            correct_count=self.correct_count,
            wrong_count=self.wrong_count
        )
        self.history_manager.save_session(session)
        self.stats_tracker.update_stats(
            correct=self.correct_count,
            wrong=self.wrong_count,
            duration=duration
        )
        return session

    def get_session_stats(self) -> dict:
        return {
            "session_id": self.session_id,
            "mode": self.mode,
            "player_name": self.player_name,
            "score": self.score,
            "correct_count": self.correct_count,
            "wrong_count": self.wrong_count,
            "duration": self.timer.get_elapsed_time()
        }