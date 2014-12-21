# coding=utf-8
import unittest
from Dataset import Dataset


class DatasetTest(unittest.TestCase):
    
    def test_read_data_points(self):
        set = Dataset()
        set.read_data_points("flueaeg.txt")

        data = set.get_data

        self.assertEqual(data[100.0], 16.6)

        # here we should see an error printet
        set.read_data_points("findes-ikke.txt")
    
if __name__ == '__main__':
    unittest.main()