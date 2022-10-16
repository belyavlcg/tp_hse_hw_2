import unittest
from tp_2 import main


class Test_Exception(unittest.TestCase):
    def test_name_file_except(self):
        self.assertEqual(main("test_file_0"), '')


if __name__ == '__main__':
    unittest.main()
