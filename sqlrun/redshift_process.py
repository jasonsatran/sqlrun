class RedshiftProcess:

    def __init__(self, command_text, redshift_processor):
        self._process_result = None
        self._command_text = command_text
        self._redshift_processor = redshift_processor

    # @staticmethod
    # def load_file(f):
        # with open(f):
            # s = f.read()
        # return s

    @property
    def process_result(self):
        return self._process_result

    @process_result.setter
    def process_result(self, value):
        self._process_result = value


    def run(self):
        self.process_result = self._redshift_processor.process(self)


    # def run_file(self, file_path):
        # """runs a sql file
        # returns a Stat object
        # """

        # with open(file_path) as f:
            # sql = f.read()

        # return self.run_sql(sql)
