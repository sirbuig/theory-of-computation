from automatalib.input_validator import InputValidator
from automatalib.dfa_engine import DFA
import sys


class NFA:
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
            if letter not in self.transitions[src]:
                self.transitions[src][letter] = set()
            self.transitions[src][letter].add(dest)

    def to_dfa(self):
        dfa_states = {}
        dfa_start_state = frozenset([self.start_state])
        dfa_final_states = set()
        dfa_transitions = {}
        unmarked_states = [dfa_start_state]
        dfa_states[dfa_start_state] = dfa_start_state

        while unmarked_states:
            current_dfa_state = unmarked_states.pop()
            if current_dfa_state not in dfa_transitions:
                dfa_transitions[current_dfa_state] = {}

            for letter in self.sigma:
                next_nfa_states = set()
                for nfa_state in current_dfa_state:
                    if (
                        nfa_state in self.transitions
                        and letter in self.transitions[nfa_state]
                    ):
                        next_nfa_states.update(self.transitions[nfa_state][letter])

                next_dfa_state = frozenset(next_nfa_states)
                if next_dfa_state not in dfa_states:
                    dfa_states[next_dfa_state] = next_dfa_state
                    unmarked_states.append(next_dfa_state)

                dfa_transitions[current_dfa_state][letter] = next_dfa_state

                if next_dfa_state & self.final_states:
                    dfa_final_states.add(next_dfa_state)

        dfa = InputValidator("")
        dfa.sigma = self.sigma
        dfa.states = set(dfa_states.keys())
        dfa.start_state = dfa_start_state
        dfa.final_states = dfa_final_states
        dfa.transitions = [
            (src, letter, dest)
            for src, trans in dfa_transitions.items()
            for letter, dest in trans.items()
        ]

        return dfa

    def save_to_file(self, file_path, dfa_validator):
        with open(file_path, "w") as f:
            f.write("Sigma:\n")
            for symbol in dfa_validator.sigma:
                f.write(f"    {symbol}\n")
            f.write("End\n\n")

            f.write("States:\n")
            for state in dfa_validator.states:
                state_str = f"    {'_'.join(sorted(state))}"
                if state == dfa_validator.start_state:
                    state_str += ", S"
                if state in dfa_validator.final_states:
                    state_str += ", F"
                f.write(state_str + "\n")
            f.write("End\n\n")

            f.write("Transitions:\n")
            for src, letter, dest in dfa_validator.transitions:
                src_str = "_".join(sorted(src))
                dest_str = "_".join(sorted(dest))
                f.write(f"    {src_str}, {letter}, {dest_str}\n")
            f.write("End\n")


# manual testing
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("The accepted usage is: nfa_engine.py nfa_config_file dfa_config_file")
        sys.exit(1)

    nfa_config_file = sys.argv[1]
    dfa_config_file = sys.argv[2]

    try:
        validator = InputValidator(nfa_config_file)
        validator.validate()
    except Exception as e:
        print(f"failed, {e}")
        sys.exit(1)

    nfa = NFA(validator)
    dfa_validator = nfa.to_dfa()
    nfa.save_to_file(dfa_config_file, dfa_validator)
    print(f"DFA configuration saved to {dfa_config_file}")
