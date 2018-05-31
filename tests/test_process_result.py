import unittest
from sqlrun.process_result import ProcessResult
from sqlrun.redshift_process import RedshiftProcess
from sqlrun.process_report import ProcessReport

class MainTest(unittest.TestCase):

    def test_result_report_runs(self):
        result1 = ProcessResult()
        result2 = ProcessResult()

        result1._start_time = 100  #accessing a private member for the purpose of testing
        result1._end_time = 200
        result2._start_time = 100  #accessing a private member for the purpose of testing
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

        # print('\n\n', report, '\n\n')

        expected = """
 step      process desc                            running_time (seconds)
------------------------------------------------------------------------
1         a select statement                      None
2         another select statement                None
        """

        # self.assertEqual(report.strip(), expected.strip())


if __name__ == '__main__':
    unittest.main()

