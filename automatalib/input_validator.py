import os


class InputValidator:
    def __init__(self, file_path) -> None:
        self.file_path = file_path
        self.sigma = set()
        self.states = set()
        self.transitions = []
        self.start_state = None
        self.final_states = set()

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

    def parse_sigma(self, lines):
        sigma_lines = self.parse_section(lines, "Sigma")
        for line in sigma_lines:
            line = line.strip()
            if line and not line.startswith("#"):
                self.sigma.add(line)

    def parse_states(self, lines):
        state_lines = self.parse_section(lines, "States")
        start_state_count = 0
        for line in state_lines:
            line = line.strip()
            if line and not line.startswith("#"):
                tokens = [p.strip() for p in line.split(",")]
                self.states.add(tokens[0])
                if len(tokens) > 1:
                    for token in tokens[1:]:
                        if token == "S":
                            start_state_count += 1
                            if start_state_count > 1:
                                raise ValueError("There must be only one start state!")
                            self.start_state = tokens[0]
                        if token == "F":
                            self.final_states.add(tokens[0])

    def parse_transitions(self, lines):
        transition_lines = self.parse_section(lines, "Transitions")
        for line in transition_lines:
            line = line.strip()
            if line and not line.startswith("#"):
                tokens = [p.strip() for p in line.split(",")]
                if len(tokens) != 3:
                    raise ValueError("A transition must have 3 parts!")
                self.transitions.append((tokens[0], tokens[1], tokens[2]))

    def validate_transitions(self):
        for src, letter, dest in self.transitions:
            if src not in self.states:
                raise ValueError(f"Source state invalid: {src}")
            if dest not in self.states:
                raise ValueError(f"Destination state invalid: {dest}")
            if letter not in self.sigma:
                raise ValueError(f"Letter invalid: {letter}")

    def validate(self):
        lines = self.load_file()
        self.parse_sigma(lines)
        self.parse_states(lines)
        self.parse_transitions(lines)
        self.validate_transitions()
        # print("valid")
        # print(
        #     self.final_states,
        #     self.sigma,
        #     self.start_state,
        #     self.states,
        #     self.transitions,
        #     sep="\n",
        # )


# for manual testing
# if __name__ == "__main__":
#     validator = InputValidator(
#         os.path.join(
#             os.path.dirname(
#                 "/home/sig/Projects/theory-of-computation/tests/test_inputs"
#             ),
#             "test_inputs",
#             "input.txt",
#         )
#     )
#     try:
#         validator.validate()
#     except Exception as e:
#         print(f"invalid, {e}")
