import unittest
from .app import categorize_expenses


class TestCategorizeExpenses(unittest.TestCase):

    def test_basic_case(self):
        data = [
            {"category": "food", "amount": 100},
            {"category": "transport", "amount": 50},
            {"category": "food", "amount": 150}
        ]
        expected = {
            "food": 250,
            "transport": 50,
            "total": 300
        }
        self.assertEqual(categorize_expenses(data), expected)

    def test_empty(self):
        self.assertEqual(categorize_expenses([]), {"total": 0})

    def test_one_category(self):
        data = [
            {"category": "food", "amount": 100},
            {"category": "food", "amount": 200}
        ]
        expected = {
            "food": 300,
            "total": 300
        }
        self.assertEqual(categorize_expenses(data), expected)

    def test_zero_amount(self):
        data = [
            {"category": "food", "amount": 0}
        ]
        expected = {
            "food": 0,
            "total": 0
        }
        self.assertEqual(categorize_expenses(data), expected)


if __name__ == "__main__":
    unittest.main()
