from setuptools import find_packages, setup

setup(
    name="automatalib",
    packages=find_packages(include=["automatalib"]),
    version="0.1.0",
    description="A Python library using Formal Languages & Automata Theory",
    author="sirbuig",
    author_email="sirbuig@proton.me",
    install_requires=[],
    setup_requires=["pytest-runner"],
    tests_require=["pytest==8.2.2"],
    test_suite="tests",
)
