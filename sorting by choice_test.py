import unittest
from selection_sort import selection_sort

class SelectionSortTestCase(unittest.TestCase):
    def test_selection_sort(self):
        arr = [64, 25, 12, 22, 11]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [11, 12, 22, 25, 64])

        arr = [5, 2, 8, 1, 9]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [1, 2, 5, 8, 9])

        arr = [10, 20, 30, 40, 50]
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [10, 20, 30, 40, 50])

    def test_selection_sort_empty_input(self):
        arr = []
        sorted_arr = selection_sort(arr)
        self.assertEqual(sorted_arr, [])

if __name__ == "__main__":
    unittest.main()