'''
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {"appium:deviceName": "Android Emulator",
               "platformName": "Android",
               "appium:appPackage": "org.simple.clinic.staging",
               "appium:appWaitActivity": "org.simple.clinic.setup.SetupActivity",
               "appium:app": "C:\\python-appium\\simple-demo\\APK\\Demo Simple.apk",
               "newCommandTimeout": "600"}


driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

'''


'''
from faker import Faker

class NameGenerator:
    def __init__(self):
        self.fake = Faker()
        self.names = []

    def generate_name(self):
        name = self.fake.name()
        self.names.append(name)
        return name

name_generator = NameGenerator()
print(name_generator.generate_name())
print(name_generator.names[0])

'''

'''
import os
from datetime import datetime

def create_folder():
    date = datetime.now().strftime("%d-%m-%Y")
    directory = "C:\\python-appium\\simple-demo\\Screenshot" + date

    if not os.path.exists(directory):
        os.makedirs(directory)

    print("Directory '%s' created" % directory)

create_folder()
'''

import os
import shutil

def create_folder():

    for i in range(1, 23):
        directory = f"C:\\python-appium\\simple-demo\\Screenshot\\TC_{str(i)}"
        shutil.rmtree(directory)
        os.makedirs(directory)


create_folder()








#len = 25

#print(type(len))
''''
sample = '28 days'
sam_slice = sample[0:2]
print(sam_slice)
sam_cast = int(sam_slice)
print(type(sam_cast))
'''

list_a = ['apple', 'banana', 'orange']

assert 'apple' in list_a, 'Not found'
print('Success')
