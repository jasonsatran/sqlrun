import unittest
import os
from sqlrun.redshift_process_factory import RedshiftFileProcessFactory



class MainTest(unittest.TestCase):

    # is the relative path the path to this file or the path where python was started
    def test_it_loads_from_dir(self):

        relative_resource_path = "../tests/resources"
        this_file_dir = os.path.dirname(__file__)
        test_file_path = os.path.join(this_file_dir, relative_resource_path)
        abs_path = os.path.abspath(test_file_path)
        processes = RedshiftFileProcessFactory.load_from_dir(abs_path)
        self.assertEqual(2, len(processes))
        self.assertEqual(processes[0].command_text, "select 1;\n")
        self.assertEqual(processes[0].description, "file1.sql")

if __name__ == '__main__':
    unittest.main()

