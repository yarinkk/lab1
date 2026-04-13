import unittest
from app import calculate_weight_cost, add_express_fee, calculate_total_cost


class TestDelivery(unittest.TestCase):

    def test_weight_cost(self):
        self.assertEqual(calculate_weight_cost(2), 40)
        self.assertEqual(calculate_weight_cost(0), 0)

    def test_weight_negative(self):
        with self.assertRaises(ValueError):
            calculate_weight_cost(-1)

    def test_express_fee(self):
        self.assertEqual(add_express_fee(100, True), 150)
        self.assertEqual(add_express_fee(100, False), 100)

    def test_total_cost(self):
        self.assertEqual(calculate_total_cost(2, True), 90)
        self.assertEqual(calculate_total_cost(3, False), 60)


if __name__ == "__main__":
    unittest.main()