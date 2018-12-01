import time


class ProcessResult:

    all_process_total_running_time = 0

    def __init__(self):
        self.start_time = time.time()
        self._end_time_set = False
        self._running_time = None
        self._end_time = None
        self.output = None

    @property
    def output(self):
        return self._output

    @output.setter
    def output(self, value):
        self._output = value

    def percent_of_total(self):
        return self._running_time/ProcessResult.all_process_total_running_time * 100

    @property
    def running_time(self):
        return self._running_time

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def end_time(self):
        return self._end_time

    @end_time.setter
    def end_time(self, value):
        if self._end_time_set == False:
            self._end_time = value
            self._running_time = self._end_time - self._start_time
            ProcessResult.all_process_total_running_time += self._running_time
        else:
            self._end_time_set = True

    def set_end_time(self):
        self.end_time = time.time()

    @property
    def start_time(self):
        return self._start_time

    @start_time.setter
    def start_time(self, value):
        self._start_time = value
