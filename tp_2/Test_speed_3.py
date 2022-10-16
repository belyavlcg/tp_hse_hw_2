import unittest
import time
from tp_2 import _sum, get_num_base


class Test_Speed(unittest.TestCase):
    def test_mult_speed_1(self):
        test_base = get_num_base("test_file_100000")
        start_time = int(round(time.time() * 1000))
        _sum(test_base)
        stop_time = int(round(time.time() * 1000))
        self.assertLess(stop_time - start_time, 6)
        print(stop_time - start_time)

    def test_mult_speed_2(self):
        test_base = get_num_base("test_file_1000000")
        start_time = int(round(time.time() * 1000))
        _sum(test_base)
        stop_time = int(round(time.time() * 1000))
        self.assertLess(stop_time - start_time, 55)

        
if __name__ == '__main__':
    unittest.main()
