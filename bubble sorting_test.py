import unittest

class BubbleSortTest(unittest.TestCase):
    def test_bubble_sort(self):
        arr = [5, 2, 8, 12, 4, 9]
        expected_result = [2, 4, 5, 8, 9, 12]
        self.assertEqual(bubble_sort(arr), expected_result)

        arr = [1, 2, 3, 4, 5]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected_result)

        arr = [5, 4, 3, 2, 1]
        expected_result = [1, 2, 3, 4, 5]
        self.assertEqual(bubble_sort(arr), expected_result)

if __name__ == '__main__':
    unittest.main()


