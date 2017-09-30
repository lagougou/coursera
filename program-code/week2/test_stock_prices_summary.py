import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """

    # Add your test methods for a1.stock_price_summary here.
    def test_stock_price_summary_exam1(self):
        actual = a1.stock_price_summary([0, 0, 0, 0, 0, 0, 0, 0])
        expected = (0, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_exam2(self):
        actual = a1.stock_price_summary([0.1, 0.15, 0.02, 0.001, 0.11, 0.03])
        expected = (0.411, 0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_exam3(self):
        actual = a1.stock_price_summary([-0.01, -0.13, -0.012, -0.1, -0.02, -0.05])
        expected = (0, -0.322)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_exam4(self):
        actual = a1.stock_price_summary([0.01, 0.03, -0.02, -0.14, 0, 0, 0.10, -0.01])
        expected = (0.14, -0.17)
        self.assertEqual(expected,actual)

    def test_stock_price_summary_exam5(self):
        actual = a1.stock_price_summary([])
        expected = (0,0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_exam6(self):
        actual = a1.stock_price_summary([0.12])
        expected = (0.12,0)
        self.assertEqual(expected, actual)

    def test_stock_price_summary_exam7(self):
        actual = a1.stock_price_summary([-0.11])
        expected = (0,-0.11)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)