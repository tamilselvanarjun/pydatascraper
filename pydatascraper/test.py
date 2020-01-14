import unittest
from pyscraper import get_options, locations

class TestGetOptions(unittest.TestCase):
    def test_get_options_with_valid_input(self):
        scrambled = "etcbat"
        flag = False
        totals = []
        last = ''
        result = get_options(scrambled, flag, totals, last)
        self.assertEqual(result, ['etc', 'bat'])

    def test_get_options_with_invalid_input(self):
        scrambled = "xyz"
        flag = False
        totals = []
        last = ''
        result = get_options(scrambled, flag, totals, last)
        self.assertEqual(result, [])

class TestLocations(unittest.TestCase):
    def test_child_tree1_with_valid_input(self):
        url = "https://www.marianilandscape.com/where-we-are/"
        # Replace get_soup_function with actual function to get soup object
        soup = get_soup_function(url)  
        td = "Some TD"
        branches = "Some Branches"
        result = locations.child_tree1(url, soup, td, branches)
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

    def test_child_tree2_with_valid_input(self):
        url = "https://landscapedevelopment.com/contact/"
        # Replace get_soup_function with actual function to get soup object
        soup = get_soup_function(url)  
        td = "Some TD"
        branches = "Some Branches"
        result = locations.child_tree2(url, soup, td, branches)
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

    def test_child_tree3_with_valid_input(self):
        url = "https://www.yellowstonelandscape.com/locations"
        # Replace get_soup_function with actual function to get soup object
        soup = get_soup_function(url)  
        td = "Some TD"
        branches = "Some Branches"
        result = locations.child_tree3(url, soup, td, branches)
        self.assertIsNotNone(result)
        self.assertGreater(len(result), 0)

if __name__ == "__main__":
    unittest.main()
