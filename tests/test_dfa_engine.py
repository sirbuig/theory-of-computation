import unittest
import os
from automatalib.dfa_engine import DFA
from automatalib.input_validator import InputValidator


class TestDFA(unittest.TestCase):
    def get_file_path(self, filename):
        return os.path.join(os.path.dirname(__file__), "test_inputs", filename)

    def test_dfa_string_1(self):
        file_path = self.get_file_path("dfa_input.txt")
        validator = InputValidator(file_path)
        validator.validate()
        dfa = DFA(validator)

        self.assertTrue(dfa.accepts("bbabbabba"))

    def test_dfa_string_2(self):
        file_path = self.get_file_path("dfa_input.txt")
        validator = InputValidator(file_path)
        validator.validate()
        dfa = DFA(validator)

        self.assertTrue(dfa.accepts("abbabba"))

    def test_dfa_string_3(self):
        file_path = self.get_file_path("dfa_input.txt")
        validator = InputValidator(file_path)
        validator.validate()
        dfa = DFA(validator)

        self.assertFalse(dfa.accepts("ababababababaaaaaba"))

    def test_dfa_string_4(self):
        file_path = self.get_file_path("dfa_input.txt")
        validator = InputValidator(file_path)
        validator.validate()
        dfa = DFA(validator)

        self.assertTrue(dfa.accepts("bbbbbbaaaaabbbabbaaaaaaab"))


if __name__ == "__main__":
    unittest.main()
