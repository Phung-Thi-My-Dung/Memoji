class StatsTracker:
    def __init__(self):
        self.correct = 0
        self.incorrect = 0
        self.total_time = 0.0

    def record(self, is_correct, time_taken):
        if is_correct:
            self.correct += 1
        else:
            self.incorrect += 1
        self.total_time += time_taken

    def summary(self):
        return {
            "Correct": self.correct,
            "Incorrect": self.incorrect,
            "Total time": self.total_time,
        }
