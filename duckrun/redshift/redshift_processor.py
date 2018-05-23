import psycopg2
import time

from duckrun.process_result import ProcessResult

class RedshiftProcessor:

    def execute_process(self, redshift_process):
        process_result = ProcessResult()
        redshift_process.process_result = process_result

        try:
            conn = psycopg2.connect(host=self._host,  port=self._port , user=self._user,  password=self._password, sslmode=self._ssl_mode, database=self._database)
            cur = conn.cursor()
            cur.execute(redshift_process.command_text)
            process_result.result_description = cur.fetchall()[0][0]
            process_result.set_end_time()
        except:
            raise
        finally:
            #print("Closing Connection")
            cur.close()


    def __init__(self, host, port, user, password, ssl_mode, database):
        self._host = host
        self._port = port
        self._user = user
        self._password = password
        self._ssl_mode = ssl_mode
        self._database = database

        self._connection = psycopg2.connect(host=self._host,  port=self._port , user=self._user,  password=self._password, sslmode=self._ssl_mode, database=self._database)
