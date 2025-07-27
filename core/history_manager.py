import pandas as pd
from typing import List
from model.session import Session

class HistoryManager:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def save_session(self, session: Session):
        try:
            df = pd.read_excel(self.file_path) if pd.exists(self.file_path) else pd.DataFrame()
            new_row = {
                "session_id": session.session_id,
                "mode": session.mode,
                "timestamp": session.timestamp,
                "player_name": session.player_name,
                "score": session.score,
                "duration": session.duration,
                "words_used": ",".join(session.words_used),
                "correct_count": session.correct_count,
                "wrong_count": session.wrong_count
            }
            df = df.append([new_row], ignore_index=True)
            df.to_excel(self.file_path, index=False)

        except Exception as e:
            print(e)

    def load_history(self, start_date: str = None, end_date: str = None) -> List[Session]:
        try:
            df = pd.read_excel(self.file_path)
            if start_date and end_date:
                df = df[(df["timestamp"] >= start_date) & (df["timestamp"] <= end_date)]
            sessions = []
            for _, row in df.iterrows():
                session = Session(
                    session_id=row["session_id"],
                    mode=row["mode"],
                    timestamp=pd.to_datetime(row["timestamp"]),
                    player_name=row["player_name"],
                    score=row["score"],
                    duration=row["duration"],
                    words_used=row["words_used"].split(",") if pd.notna(row["words_used"]) else [],
                    correct_count=row["correct_count"],
                    wrong_count=row["wrong_count"]
                )
                sessions.append(session)
            return sessions
        except Exception as e:
            print(f"Error loading history from {self.file_path}: {str(e)}")
            return []