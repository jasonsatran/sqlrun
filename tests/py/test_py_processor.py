import unittest
import os
from sqlrun.py.py_processor import PyProcessor
from sqlrun.generic_process import GenericProcess
from sqlrun.process_result import ProcessResult



class MainTest(unittest.TestCase):

    # is the relative path the path to this file or the path where python was started

    def test_it_sets_result_times(self):
        processor = PyProcessor()
        command = "print('hello world')"
        process = GenericProcess(command)
        processor.execute_process(process)
        self.assertIsNotNone(process.process_result.start_time)
        self.assertIsNotNone(process.process_result.end_time)

if __name__ == '__main__':
    unittest.main()


