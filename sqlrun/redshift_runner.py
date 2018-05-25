import psycopg2
from sqlrun.stat import Stat
import time

class RedshiftRunner:

    def execute_sql(self, sql):
        """Implements the runner public interface"""
        return True

    def __init__(self, host, port, user, password, sslmode, database):
        pass
