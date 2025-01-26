from random import choice
from string import ascii_letters, digits

def generate_random_string(limit: int = 15):
    return ''.join(choice(ascii_letters + digits) for _ in range(limit))