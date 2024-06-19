# theory-of-computation

![Python package](https://img.shields.io/github/actions/workflow/status/sirbuig/theory-of-computation/python-package.yml?label=Python%20package&style=for-the-badge)
![GitHub License](https://img.shields.io/github/license/sirbuig/theory-of-computation?style=for-the-badge)
![GitHub Issues or Pull Requests](https://img.shields.io/github/issues/sirbuig/theory-of-computation?style=for-the-badge)

## Description

This is my homework for the theory of computation class @fmi-unibuc.

This library implements and tests the following:

- [x] an input validator that checks if a given configuration file is valid or not
- [x] a program that loads and then generates a DFA based on an input file and checks if it accepts a given string
- [x] a program that creates a NFA and converts it to a DFA
- [x] a program that loads a validates a CFG configuration file
- [ ] ~a program that creates a PDA and converts it to a CFG~

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.9, 3.10, 3.11 or 3.12
- `pip`, the Python package installer

### Setting up the Environment

1. **Clone the Repository**
   ```
   https://github.com/sirbuig/theory-of-computation.git
   cd theory-of-computation
   ```
2. **Create and activate a virtual environment**

   ```
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```
   pip install -r requirements.txt
   ```

## Usage

From the root of the folder run `pytest`.
