import unittest
from sqlrun.process_report import ProcessReport



class MainTest(unittest.TestCase):

    # is the relative path the path to this file or the path where python was started

    def test_it_formats_seconds(self):

        test_cases = [1.112e-03, 12.1232, 0, 100.12]
        results = [ProcessReport.format_second(test_case) for test_case in test_cases]
        self.assertEqual(results, ['0.0011', '12.1232', '0.0000', '100.1200'])

