import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

desired_cap = {"appium:deviceName": "4cdda091",
               "platformName": "Android",
               "appium:appPackage": "org.simple.clinic.staging",
               "appium:appWaitActivity": "org.simple.clinic.setup.SetupActivity",
               "appium:app": "C:\\python-appium\\simple-demo\\APK\\Demo Simple.apk",
               "newCommandTimeout": "600"}

@pytest.fixture(scope="class", autouse=True)
def setup(request):
    driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
    wait = WebDriverWait(driver, 20)
    request.cls.driver = driver
    request.cls.wait = wait
