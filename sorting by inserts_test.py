import unittest

class TestInsertionSort(unittest.TestCase):
    def test_insertion_sort(self):
        arr = [4, 2, 5, 7, 1, 3]
        sorted_arr = insertion_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 3, 4, 5, 7])

if __name__ == '__main__':
    unittest.main()