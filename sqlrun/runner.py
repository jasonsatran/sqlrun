class Runner:

    def __init__(self, file_list, db_specific_runner):
        self._file_list = file_list
        self._db_specific_runner = db_specific_runner

    # @staticmethod
    # def load_file(f):
        # with open(f):
            # s = f.read()
        # return s

    def run_sql(self, sql):
        stat = self._db_specific_runner.execute_sql(sql)
        return stat


    def run_file(self, file_path):
        """runs a sql file
        returns a Stat object
        """

        with open(file_path) as f:
            sql = f.read()

        return self.run_sql(sql)
