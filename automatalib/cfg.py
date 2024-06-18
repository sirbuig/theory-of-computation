from cfg_validator import CFGValidator


class CFG:
    def __init__(self, validator: CFGValidator) -> None:
        self.variables = validator.variables
        self.terminals = validator.terminals
        self.productions = validator.productions
        self.start_variable = validator.start_variable

    def display(self):
        print("Variables:", self.variables)
        print("Terminals:", self.terminals)
        print("Productions:")
        for left, rights in self.productions.items():
            for right in rights:
                print(f"  {left} -> {right}")
        print("Start Variable:", self.start_variable)


# for manual testing
if __name__ == "__main__":
    cfg_file = (
        "/home/sirbuig/Projects/theory-of-computation/tests/test_inputs/cfg_input.txt"
    )
    validator = CFGValidator(cfg_file)
    try:
        validator.validate()
        cfg = CFG(validator)
        cfg.display()
    except Exception as e:
        print(f"Invalid CFG configuration: {e}")
