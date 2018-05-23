import unittest
from duckrun.process_result import ProcessResult
from duckrun.generic_process import GenericProcess
from duckrun.process_report import ProcessReport

class MainTest(unittest.TestCase):

    def test_result_report_runs(self):
        result1 = ProcessResult()
        result2 = ProcessResult()

        #_start_time is private and is accessed here only for testing purposes
        result1._start_time = 100
        result1.end_time = 200
        result2._start_time = 100
        result2.end_time = 400

        process1 = GenericProcess("select 1;")
        process2 = GenericProcess("select 2;")

        process1.description = "a select statement"
        process2.description = "another select statement"

        process1.process_result = result1
        process2.process_result = result2

        processes = [process1, process2]

        reporter = ProcessReport(processes)

        report = reporter.get_report()

        self.assertEqual(report[0].strip(),  "step      process desc                            running_time (seconds)                  percent of total time")


        self.assertEqual(report[2].strip(),  "1         a select statement                      100.0000                                25.0")

        self.assertEqual(report[3].strip(),  "2         another select statement                300.0000                                75.0")

    def test_calling_set_end_time_sets_end_time_and_percent_of_total(self):
        result1 = ProcessResult()
        initial_rt = result1.running_time
        self.assertIsNone(initial_rt)
        result1.set_end_time()
        final_rt = result1.running_time
        final_rt_type = type(final_rt)
        self.assertEqual(str(final_rt_type), "<class 'float'>")
        percent_of_total_type = type(result1.percent_of_total())
        self.assertEqual(str(percent_of_total_type), "<class 'float'>")

if __name__ == '__main__':
    unittest.main()

