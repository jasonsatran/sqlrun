import unittest
from sqlrun.process_result import ProcessResult
from sqlrun.redshift_process import RedshiftProcess
from sqlrun.process_report import ProcessReport

class MainTest(unittest.TestCase):

    def test_result_report_runs(self):
        result1 = ProcessResult()
        result2 = ProcessResult()

        #_start_time is private and is accessed here only for testing purposes
        result1._start_time = 100
        result1._end_time = 200
        result2._start_time = 100
        result2._end_time = 400

        process1 = RedshiftProcess("select 1;")
        process2 = RedshiftProcess("select 2;")

        process1.description = "a select statement"
        process2.description = "another select statement"

        process1.process_result = result1
        process2.process_result = result2

        processes = [process1, process2]

        reporter = ProcessReport(processes)

        report = reporter.get_report()
        
        self.assertEqual(report[0],  "step      process desc                            running_time (seconds)")
        self.assertEqual(report[2].strip(),  "1         a select statement                      100")
        self.assertEqual(report[3].strip(),  "2         another select statement                300")


if __name__ == '__main__':
    unittest.main()

