from datetime import datetime, timedelta
import time

class Timer():
    def __init__(self, start_time=None):
        """
        Initialize a Timer object.

        Attributes:
            - start_time (datetime): the time when the timer started
            - end_time (datetime): the time when the timer ended
            - elapsed_time (timedelta): the duration of the timer
        """
        self.start_time = start_time if start_time else datetime.now()
        self.elapsed_time = 0
        self._is_pause = None
    

    def start(self):
        pass

    def get_elapsed_time(self):
        """
        Returns the elapsed time since the timer started.
        """
        if self._is_pause:
            return self.elapsed_time
        else:
            return datetime.now() - self.start_time
    
