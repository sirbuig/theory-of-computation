import unittest
import os
from automatalib.cfg_validator import CFGValidator


class TestCFGValidator(unittest.TestCase):
    def get_file_path(self, filename):
        return os.path.join(os.path.dirname(__file__), "test_inputs", filename)

    def test_input(self):
        file_path = self.get_file_path("cfg_input.txt")
        validator = CFGValidator(file_path)
        self.assertTrue(validator.validate())

    def test_wrong_input(self):
        file_path = self.get_file_path("cfg_input_wrong.txt")
        validator = CFGValidator(file_path)
        self.assertFalse(validator.validate())


if __name__ == "__main__":
    unittest.main()
