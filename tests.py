import unittest
from functions.get_files_info import get_files_info


class TestGetFilesInfo(unittest.TestCase):
    def test_calculator_directory(self):
        result = get_files_info("calculator", ".")
        print(result)
        self.assertIsInstance(result, str)
        
    def test_calculator_pkg_directory(self):
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertIsInstance(result, str)
        
    def test_calculator_bin_directory(self):
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertIsInstance(result, str)
        
    def test_calculator_parent_directory(self):
        result = get_files_info("calculator", "../")
        print(result)
        self.assertIsInstance(result, str)


if __name__ == "__main__":
    unittest.main()