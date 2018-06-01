from sqlrun.process_result import ProcessResult

class GenericProcess:

    def __init__(self, command_text):
        self.process_result = None
        self._description = None
        self._command_text = command_text

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, value):
        self._description = value

    @property
    def process_result(self):
        return self._process_result

    @process_result.setter
    def process_result(self, value):
        self._process_result = value

    def run(self, abstract_processor):
        self.process_result = abstract_processor.execute_process(self)

    @property
    def command_text(self):
        return self._command_text
