import sys
import os.path
parent_dir = (os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(parent_dir)

print("location: " + os.path.dirname(__file__))

# # import the module name only.
# import test_import.test # package_name.module_name
# test_import.test.function_a()

# # import and rename modules for easy use.
# import test_import.test as my_test
# my_test.function_a()

# ****Recommended****###
# import what you only need
from test_import.test import function_a, function_b  # noqa: E402
function_a()
function_b()

# # import everything at once
# from test_import.test import *
# function_a()
# function_b()

# does not import "_" functions


def greet(name):
    """
    Function which Greets the name provided to it

    Args:
        name (str): Name of a person to greet
    """
    print("Hello " + name)
    # print("Hello " + name + "!")


greet("Jerry")

# greet("Bob")
