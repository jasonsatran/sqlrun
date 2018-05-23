class Runner:

    def __init__(self, file_list, db_specific_runner):
        self._file_list = file_list
        self._db_specific_runner = db_specific_runner

    def run_file(self, file):
        """runs a sql file
        returns a Stat object
        """

        stat = self._db_specific_runner.run(file)
        return stat
