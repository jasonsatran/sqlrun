import unittest
from sqlrun.redshift.redshift_process import RedshiftProcess

class MainTest(unittest.TestCase):

    def test_constructor_command_text(self):
        x = RedshiftProcess("select 1;")
        self.assertEqual(x.command_text, "select 1;")

if __name__ == '__main__':
    unittest.main()


