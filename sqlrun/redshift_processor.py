import psycopg2
from sqlrun.stat import Stat
import time

class RedshiftProcessor:

    def execute_process(self, redshift_process):
        process_result = None

        # ToDo:  
            # - call actual redshift processing
            # - construct process result

        redshift_process.process_result = process_result

    def __init__(self, host, port, user, password, ssl_mode, database):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._ssl_mode = ssl_mode
        self._database = database
