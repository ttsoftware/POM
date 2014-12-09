import unittest
from Dataset import Dataset


class DatasetTest(unittest.TestCase):
    
    def test_read_data_points(self):
        set = Dataset()
        set.read_data_points("flueaeg.txt")

        print set.get_data()
    
if __name__ == '__main__':
    unittest.main()