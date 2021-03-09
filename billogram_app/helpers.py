import string
import random

def generate_discount_codes(no_of_codes = 10):
    codes = []
    for _ in range(no_of_codes):
        codes.append(code_generator())
    return codes

def code_generator(size=6):
    chars = string.ascii_uppercase + string.digits
    return ''.join(random.choice(chars) for _ in range(size))