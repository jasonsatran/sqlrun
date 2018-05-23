import unittest

from sqlrun.redshift_runner import RedshiftRunner
# from unittest.mock import MagicMock
# wip:  https://docs.python.org/3/library/unittest.mock.html

class MainTest(unittest.TestCase):


    def test_it_returns_stats(self):
        rs_runner = RedshiftRunner("host", "port","user", "password","true","master")

        stat = rs_runner.run_file("/path/to/file")

