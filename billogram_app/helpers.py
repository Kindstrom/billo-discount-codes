from typing import List
import string
import random


def generate_discount_codes(no_of_codes: int = 10) -> List[str]:
    """Function used for creating n number of discount code

    Args:
        no_of_codes (int, optional): Number of codes to create. Defaults to 10.

    Returns:
        List[str]: A list of randomized strings
    """
    codes = []
    for _ in range(no_of_codes):
        codes.append(code_generator())
    return codes


def code_generator(size: int = 6):
    """Creates a randomized string to be used as a discount code

    Args:
        size (int, optional): Number of characters to make up the code.
        Defaults to 6.

    Returns:
        str: The generated code of n characters
    """
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))