from datetime import datetime
from typing import List
from base import BaseSession
from datetime import datetime

class Session(BaseSession):
    def __init__(self, session_id: str, mode: str, timestamp: datetime, player_name: str, 
                 score: int, duration: float, words_used: List[str], wrong_count: int):
        """"
        Session class kế thừa từ BaseSession, định nghĩa các thuộc tính và phương thức
        cụ thể cho một phiên chơi game.
        Phiên chơi gảm được định nghĩa bởi các thuộc tính như mode, timestamp, player_name,
        score, duration, words_used, correct_count và wrong_count.
        Attributes:
            - session_id (str): ID duy nhất của phiên chơi
            - mode (str): chế độ chơi game
            - timestamp (datetime): thời gian bắt đầu phiên chơi
            - player_name (str): tên người chơi
            - score (int): điểm số của người chơi trong phiên
            - duration (float): thời gian phiên chơi tính bằng giây
            - words_used (List[str]): danh sách các từ đã sử dụng trong phiên

        Sử dụng phiên chơi trong việc lưu trữ và quản lý lịch sử chơi game.
        Nó được sử dụng từ lúc bắt đầu nhấn vào nút chơi game cho đến khi kết thúc phiên chơi.
        Nếu chơi tiếp tục nó sẽ được ghi ở phiên chơi mới.
        """
        super().__init__(session_id)
        self.mode = mode
        self.timestamp = timestamp
        self.player_name = player_name
        self.score = score
        self.duration = duration
        self.words_used = words_used
        self.wrong_count = wrong_count
        self.datetime = self._get_datetime()

    def _get_datetime(self) -> str:
        """
        Trả về chuỗi định dạng ngày giờ hiện tại.
        """
        return datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    
    def set_mode(self, mode: str):
        self.mode = mode.strip() if isinstance(mode, str) else None 

    def get_mode(self) -> str:
        return self.mode  
      
    def set_timestamp(self, timestamp: datetime):
        if isinstance(timestamp, datetime):
            self.timestamp = timestamp
        else:
            raise TypeError("Timestamp must be a datetime object.")
        
    def get_timestamp(self) -> datetime:
        return self.timestamp
    
    def set_player_name(self, player_name: str):
        self.player_name = player_name.strip() if isinstance(player_name, str) else None

    def get_player_name(self) -> str:
        return self.player_name
    
    def set_score(self, score: int):
        if isinstance(score, int):
            self.score = score
        else:
            raise TypeError("Score must be an integer.")
        
    def get_score(self) -> int:
        return self.score
    
    def set_duration(self, duration: float):
        if isinstance(duration, (int, float)):
            self.duration = duration
        else:
            raise TypeError("Duration must be a number.")
        
    def get_duration(self) -> float:
        return self.duration   
     
    def set_words_used(self, words: List[str]):
        if isinstance(words, list) and all(isinstance(word, str) for word in words):
            self.words_used = [word.strip() for word in words]
        else:
            raise TypeError("Words used must be a list of strings.")

    def get_words_used(self) -> List[str]:
        return self.words_used


