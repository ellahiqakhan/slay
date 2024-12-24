import unittest

# Function to test
def add_numbers(a, b):
    return a + b

# Test class
class TestMathFunctions(unittest.TestCase):

    def test_add_numbers(self):
        self.assertEqual(add_numbers(2, 3), 5)  # Test with positive numbers
        self.assertEqual(add_numbers(-1, 1), 0)  # Test with negative and positive numbers
        self.assertEqual(add_numbers(0, 0), 0)  # Test with zeros
        self.assertEqual(add_numbers(-5, -5), -10)  # Test with negative numbers

if __name__ == "__main__":
    unittest.main()
