import unittest
from binary_search import binary_search_fun
from binary_search import find_middle_index


class TestBinarySearch(unittest.TestCase):

    def test_non_element(self):
        A = [1,2,3,4,5,6,7,8]
        targetA = 28
        self.assertEqual(binary_search_fun(A, targetA), -1) 

    
    def test_element(self):
        B = [1,2,3,4,5,6,7,8]
        targetB = 8
        self.assertEqual(binary_search_fun(B,targetB), 7)


if __name__ == "__main__":
    unittest.main()