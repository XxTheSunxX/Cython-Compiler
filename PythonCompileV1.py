"""Python Compiler V.1, By Lawrence Evans (Copy of PythonCompile333.py)"""

import py_compile
import sys

code_to_compile = input("Input file to compile: ")

compiled_py_file = py_compile.compile(code_to_compile)

print("File is now compiled as: ", compiled_py_file)

sys.exit()