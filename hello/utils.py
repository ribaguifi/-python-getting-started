def calculator(a, b, operation="divide"):
    """
    Usage: calculator(4, 2) -> 2
    """
    if operation == "divide":
        return a / b

    raise NotImplementedError("Sorry, but this operation is not implemented yet.")


"""
# How to call calculator:

from hello import utils
utils.calculator(1, 2)
utils.calculator(1, 0)
"""
