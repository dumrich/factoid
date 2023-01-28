import unittest

class TestComplicatedCases(unittest.TestCase):
    def test_float_comparison(self):
        a = 0.1
        b = 0.3
        self.assertAlmostEqual(a + a + a, b, delta=1e-9)

    def test_list_subset(self):
        list_a = [1, 2, 3]
        list_b = [1, 2, 3, 4, 5]
        self.assertListEqual(list_a, list_b[:3])

    def test_regex_match(self):
        import re
        self.assertIsNotNone(re.match(r'^\d{3}-\d{2}-\d{4}$', '123-45-6789'))

    def test_exception_raised(self):
        self.assertRaises(ValueError, int, 'a')

    def test_dict_contains(self):
        dict_a = {'a': 1, 'b': 2}
        self.assertIn('a', dict_a)

if __name__ == '__main__':
    unittest.main()
