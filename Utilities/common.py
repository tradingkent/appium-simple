import base64
import random
import os
import pytest

from faker import Faker


class RandomNumberGenerator:
    def generate_random_number(self):
        random_number = "".join([str(random.randint(0, 9)) for _ in range(10)])
        return random_number




class NameGenerator:

    names = []
    def __init__(self):
        self.fake = Faker()
        #self.names = []

    def generate_name(self):
        name = self.fake.name()
        self.names.append(name)
        return name


#print(name_generator.generate_name())
#print(name_generator.names[0])

