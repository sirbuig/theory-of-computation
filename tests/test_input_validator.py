import unittest
import os
from automatalib.input_validator import InputValidator


class TestInputValidator(unittest.TestCase):
    def get_file_path(self, filename):
        return os.path.join(os.path.dirname(__file__), "test_inputs", filename)

    def test_input(self):
        file_path = self.get_file_path("dfa_input.txt")
        validator = InputValidator(file_path)
        try:
            validator.validate()
        except Exception as e:
            self.fail(f"invalid, {e}")


if __name__ == "__main__":
    unittest.main()
