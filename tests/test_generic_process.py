import unittest 
from duckrun.generic_process import GenericProcess

class MainTest(unittest.TestCase):

    def test_constructor_command_text(self):
        x = GenericProcess("select 1;")
        self.assertEqual(x.command_text, "select 1;")

if __name__ == '__main__':
    unittest.main()
