import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    # Add your test methods for a1.swap_k here.
    def test_swap_k_example1(self):
        nums = [1, 2, 3, 4, 5, 6]

        actual = a1.swap_k(nums,0)
        expected = [1, 2, 3, 4, 5, 6]
        self.assertEqual(expected, actual)

    def test_swap_k_example2(self):
        nums = [1, 2, 3, 4, 5, 6]

        actual = a1.swap_k(nums, 1)
        expected = [6, 2, 3, 4, 5, 1]
        self.assertEqual(expected, actual)

    def testtest_swap_k_example3(self):
        nums = [1, 2, 3, 4, 5, 6]
        actual = a1.swap_k(nums, 3)
        expected = [4, 5, 6, 1, 2, 3]
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)