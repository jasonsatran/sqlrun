import unittest
import os

from sqlrun.redshift_runner import RedshiftRunner

from sqlrun.stat import Stat
# from unittest.mock import MagicMock
# wip:  https://docs.python.org/3/library/unittest.mock.html

class MainTest(unittest.TestCase):

    resource_path = "../"
    runner = RedshiftRunner("host", "port","user", "password","true","master")

    # def get_resource_file(self,resource_file):
        # full_path = os.path.join(self.resource_path, resource_file)
        # with open(full_path) as f:
            # s = f.read()
        # return s

    def test_it_returns_stats(self):
        stat = self.runner.run_file("/path/to/file")
        assert(type(stat) is Stat)

    def test_reads_file_text(self):
        full_path = os.path.join(self.resource_path, "file1.sql")
        stat = self.runner.run_file(full_path)
        expected = "abc"
        self.assertEqual(expected, stat.sql)

if __name__ == "__main__":
    unittest.main()

