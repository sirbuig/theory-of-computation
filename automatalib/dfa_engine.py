import sys
from input_validator import InputValidator


class DFA:
    def __init__(self, validator: InputValidator) -> None:
        self.sigma = validator.sigma
        self.states = validator.states
        self.start_state = validator.start_state
        self.final_states = validator.final_states
        self.transitions = {}
        self.build_transitions(validator.transitions)

    def build_transitions(self, transitions):
        for src, letter, dest in transitions:
            if src not in self.transitions:
                self.transitions[src] = {}
            self.transitions[src][letter] = dest

    def accepts(self, input_string):
        current_state = self.start_state
        for letter in input_string:
            if letter not in self.sigma:
                return False
            if letter in self.transitions.get(current_state, {}):
                current_state = self.transitions[current_state][letter]
            else:
                return False
        return current_state in self.final_states


# manual testing
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("The accepted usage is: dfa_validator.py dfa_config_file input_string")
        sys.exit(1)

    dfa_config_file = sys.argv[1]
    input_string = sys.argv[2]

    try:
        validator = InputValidator(dfa_config_file)
        validator.validate()
    except Exception as e:
        print(f"failed, {e}")
        sys.exit(1)

    dfa = DFA(validator)
    if dfa.accepts(input_string):
        print("accept")
    else:
        print("reject")
