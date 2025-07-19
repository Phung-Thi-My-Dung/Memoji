import time

class Timer:
    def __init__(self):
        self.start_time = None

    def start(self):
        self.start_time = time.time()

    def stop(self) -> float:
        if self.start_time is None:
            return 0.0
        duration = time.time() - self.start_time
        self.start_time = None
        return duration

    def get_elapsed_time(self) -> float:
        if self.start_time is None:
            return 0.0
        return time.time() - self.start_time