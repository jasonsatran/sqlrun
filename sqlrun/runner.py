import psycopg2

class Runner:

    def __init__(self, file_list, connection):
        self._file_list = file_list
        self._connection = connection

    def run(self):
        """runs a sql file
        returns a Stat object
        """
        pass
