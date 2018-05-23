import psycopg2
from sqlrun.stat import Stat
import time

class RedshiftRunner:

    def run_file(self, file):
        """Implements the connection public interface"""
        
        stat = Stat()
        stat.set_start_time = int(time.time())
        stat.set_end_time = int(time.time())
        return stat

    def __init__(self, host, port, user, password, sslmode, database):
        pass
