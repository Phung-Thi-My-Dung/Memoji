from base import BaseStatistic

class Statistic(BaseStatistic):
    def __init__(self):
        """
        Initializes the Statistic instance with data.
        """
        super().__init__()

        self.id = None
        self.play_time = 0
        self.score = 0
        self.mode = None
        self.status = None
        self.datetime = None
        self.session_id = None
    
    def set_id(self, id: str):
        """
        Set the ID for the statistic.
        
        Args:
            id (str): The ID to be set.
        """
        self.id = id    
    def get_id(self) -> str:
        """
        Get the ID for the statistic.
        
        Returns:
            str: The ID of the statistic.
        """
        return self.id 
    
    def set_session_id(self, session_id: str):
        """
        Set the session ID for the statistic.
        
        Args:
            session_id (str): The session ID to be set.
        """
        self.session_id = session_id
    
    def get_session_id(self) -> str:
        """
        Get the session ID for the statistic.
        
        Returns:
            str: The session ID of the statistic.
        """
        return self.session_id
