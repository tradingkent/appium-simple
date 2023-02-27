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


list_a = ['apple', 'banana', 'orange']

assert 'apple' in list_a, 'Not found'
print('Success')
'''

'''
# Take input from the user
numbers = []
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Sort the list in descending order
numbers.sort(reverse=True)

# Print the top highest numbers in descending order
print("Top highest numbers in descending order:")
for i in range(3):
    print(numbers[i])
    
'''








'''
# Question #1
emp_list = []
for i in range(8):
    user_input = int(input(f'Please enter digit {i+1} : '))
    emp_list.append(user_input)


emp_list.sort() #reverse=True

print('The lowest three numbers are: ')
for i in range(3):
    print(emp_list[i])
'''

'''
# Take input text from the user
text = input("Enter text: ")

# Split the text into a list of words
words = text.split()


# Count the frequency of each word and store in a dictionary
word_freq = {}
for word in words:
    if word.isalpha():  # Consider only alphabetical words
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

# Find the most frequent word
most_frequent_word = max(word_freq, key=word_freq.get)

# Find the longest word
longest_word = max(words, key=len)

# Print the results
print("Most frequent word:", most_frequent_word)
print("Longest word:", longest_word)
print(word_freq)

'''

'''
def reverse_vowels(input_str):
    vowels = 'aeiouAEIOU'
    str_list = list(input_str)
    vowels_list = []
    for i in range(len(str_list)):
        if str_list[i] in vowels:
            vowels_list.append(str_list[i])
            str_list[i] = None
    vowels_list.reverse()
    for i in range(len(str_list)):
        if str_list[i] is None:
            str_list[i] = vowels_list.pop(0)
    return ''.join(str_list)


input_str = input('Enter a word:')
reversed_vowels = reverse_vowels(input_str)
print(reversed_vowels)  # Output: "hollo werld"
'''




















