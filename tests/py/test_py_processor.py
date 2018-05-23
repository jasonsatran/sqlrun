import unittest
import os
from duckrun.py.py_processor import PyProcessor
from duckrun.generic_process import GenericProcess
from duckrun.process_result import ProcessResult

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

    def test_it_write_result_to_stdout(self):
        processor = PyProcessor()
        process = PyProcessTest.test_python_process()
        processor.execute_process(process)
        result_output = process.process_result.output
        self.assertEqual("hello world\n", result_output)

    def test_graceful_handles_no_std_out(self):
        processor = PyProcessor()
        command = "x=1"
        process = GenericProcess(command)
        processor.execute_process(process)
        result_output = process.process_result.output
        self.assertEqual("", result_output)
