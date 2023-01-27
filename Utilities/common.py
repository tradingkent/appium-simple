
import random

class RandomNumberGenerator:
    def generate_random_number(self):
        random_number = "".join([str(random.randint(0, 9)) for _ in range(10)])
        return random_number
