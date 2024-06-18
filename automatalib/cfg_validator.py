from ast import Break
import os
import re


class CFGValidator:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.variables = set()
        self.terminals = set()
        self.productions = {}
        self.start_variable = None

    def load_file(self):
        with open(self.file_path, "r") as file:
            lines = file.readlines()
        return lines

    def parse_section(self, lines, section):
        start = end = None
        for i, line in enumerate(lines):
            if line.strip().startswith(section):
                start = i
            if line.strip() == "End" and start is not None:
                end = i
                break
        return lines[start + 1 : end]

    def parse_variables(self, lines):
        variable_lines = self.parse_section(lines, "Variables")
        for line in variable_lines:
            line = line.strip()
            if line and not line.startswith("#"):
                self.variables.add(line)

    def parse_terminals(self, lines):
        terminal_lines = self.parse_section(lines, "Terminals")
        for line in terminal_lines:
            line = line.strip()
            if line and not line.startswith("#"):
                self.terminals.add(line)

    def parse_productions(self, lines):
        production_lines = self.parse_section(lines, "Productions")
        for line in production_lines:
            line = line.strip()
            if line and not line.startswith("#"):
                left, right = line.split("->")
                left = left.strip()
                right = [r.strip() for r in right.split("|")]
                if left in self.productions:
                    self.productions[left].extend(right)
                else:
                    self.productions[left] = right

    def parse_start_variable(self, lines):
        start_variable_lines = self.parse_section(lines, "Start")
        for line in start_variable_lines:
            line = line.strip()
            if line and not line.startswith("#"):
                self.start_variable = line
                break

    def validate(self):
        lines = self.load_file()
        self.parse_variables(lines)
        self.parse_terminals(lines)
        self.parse_productions(lines)
        self.parse_start_variable(lines)

        if not self.start_variable:
            return False

        if self.start_variable not in self.variables:
            return False

        for left, rights in self.productions.items():
            if left not in self.variables:
                return False

            for right in rights:
                for symbol in right.split():
                    if symbol not in self.variables and symbol not in self.terminals:
                        return False

        return True


# # for manual testing
# if __name__ == "__main__":
#     validator = CFGValidator(
#         os.path.join(
#             os.path.dirname(
#                 "/home/sirbuig/Projects/theory-of-computation/tests/test_inputs"
#             ),
#             "test_inputs",
#             "cfg_input.txt",
#         )
#     )
#     try:
#         validator.validate()
#     except Exception as e:
#         print(f"invalid, {e}")
