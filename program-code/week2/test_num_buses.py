import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses. """

    # Add your test methods for a1.num_buses here.
    def test_numBus_example1(self):
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(expected,actual)

    def test_numBus_example2(self):
        actual = a1.num_buses(23)
        expected = 1
        self.assertEqual(expected,actual)

    def test_numBus_example3(self):
        actual = a1.num_buses(50)
        expected = 1
        self.assertEqual(expected,actual)

    def test_numBus_example4(self):
        actual = a1.num_buses(51)
        expected = 2
        self.assertEqual(expected,actual)

    def test_numBus_example5(self):
        actual = a1.num_buses(100)
        expected = 2
        self.assertEqual(expected,actual)

    def test_numBus_example6(self):
        actual = a1.num_buses(101)
        expected = 3
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main(exit=False)