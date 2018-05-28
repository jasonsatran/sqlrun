class ProcessResult:

    def __init__(self, sql):
        self._sql = sql
        self._start_time = None
        self._end_time = None

    @property
    def sql(self):
        return self._sql

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
