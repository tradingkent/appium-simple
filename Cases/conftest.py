import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.config import *



@pytest.fixture(scope="session", autouse=True)
def setup(request):
    driver = webdriver.Remote(host, desired_cap)
    wait = WebDriverWait(driver, 20)

    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
        setattr(cls.obj, "wait", wait)


