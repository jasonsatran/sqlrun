import time

class ProcessResult:

    def __init__(self):
        self._start_time = time.time()
        self._end_time = None
        self._description = None

    def set_end_time(self):
        self._end_time = time.time()

    def running_time(self):
        return self.end_time - self.start_time

    @property 
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def start_time(self):
        return self._start_time

    @property
    def end_time(self):
        return self._end_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value

    @end_time.setter
    def end_time(self, value):
        self._end_time = value
