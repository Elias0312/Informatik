import time

class StopWatch:
    def __init__(self):
        self.start = time.perf_counter()

    def elapsed(self):
        return time.perf_counter() - self.start
    
    def reset(self):
        self.start = time.perf_counter()

    "lol"