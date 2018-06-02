import unittest
import os
from sqlrun.py.py_processor import PyProcessor
from sqlrun.generic_process import GenericProcess
from sqlrun.process_result import ProcessResult

class PyProcessTest(unittest.TestCase):

    @staticmethod
    def test_python_process():
        command = "print('hello world')"
        process = GenericProcess(command)
        return process

    def test_it_executes_arbitrary_command(self):
        processor = PyProcessor()
        process = PyProcessTest.test_python_process()
        processor.execute_process(process)

    def test_it_mutates_process_result(self):
        processor = PyProcessor()
        process = PyProcessTest.test_python_process()
        processor.execute_process(process)
        self.assertIsNotNone(process.process_result.start_time)
        self.assertIsNotNone(process.process_result.end_time)
