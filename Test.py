import unittest
from TowerOfHanoi import Issue


class Testing(unittest.TestCase):
    def test_right_operation(self):
        obj = Issue()
        self.assertEqual(obj.get_awaited_number(2, 5, 1, 3, 5), 60)

    def test_right_operation_for_null(self):
        obj = Issue()
        self.assertEqual(obj.get_awaited_number(1, 3, 2, 4, 5), None)

    def test_right_operation_for_string(self):
        obj = Issue()
        self.assertEqual(obj.get_awaited_number(1, 3, 2, 4, 5), "")

    def test_right_operation_for_float(self):
        obj = Issue()
        self.assertEqual(obj.get_awaited_number(1, 3, 2, 4, 5), 60.0)


if __name__ == '__main__':
    unittest.main()
