import time

from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Config.config import desired_cap

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
wait = WebDriverWait(driver, 20)


class LandingPage():

    def __init__(self, driver, wait):  # driver,
        self.driver = driver
        self.wait = wait

    ##Locators##

    next_button = (By.ID, "org.simple.clinic.staging:id/nextButton")
    get_started_button = (By.ID, "org.simple.clinic.staging:id/getStartedButton")

    rad_btn_demo_country = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget."
                                      "LinearLayout/android.widget.FrameLayout/android.widget"
                                      ".LinearLayout/android.widget.FrameLayout/android.view."
                                      "ViewGroup/androidx.cardview.widget.CardView/android."
                                      "widget.ViewFlipper/android.widget.LinearLayout/androidx"
                                      ".recyclerview.widget.RecyclerView/android.widget."
                                      "LinearLayout[5]/android.widget.RadioButton")

    rad_btn_tripura = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.Linear"
                                 "Layout/android.widget.FrameLayout/android.widget.LinearLayout"
                                 "/android.widget.FrameLayout/android.view.ViewGroup/androidx."
                                 "cardview.widget.CardView/android.view.ViewGroup/androidx."
                                 "recyclerview.widget.RecyclerView/android.view.ViewGroup[9]"
                                 "/android.widget.RadioButton")

    phone_number_field = (By.ID, "org.simple.clinic.staging:id/phoneNumberEditText")
    role_name_field = (By.ID, "org.simple.clinic.staging:id/fullNameEditText")

    ##Elements##

    def get_next_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.next_button))

    def get_get_started_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.get_started_button))

    def get_rad_btn_demo_country(self):
        return self.wait.until(EC.element_to_be_clickable(self.rad_btn_demo_country))

    def get_rad_btn_tripura(self):
        return self.wait.until(EC.element_to_be_clickable(self.rad_btn_tripura))

    def get_phone_number_field(self):
        return self.driver.find_element(*self.phone_number_field)

    def get_role_name_field(self):
        time.sleep(6)
        return self.driver.find_element(*self.role_name_field)

    ##Methods##

    def click_next_button(self):
        self.get_next_button().click()

    def click_get_started_button(self):
        self.get_get_started_button().click()

    def click_rad_btn_demo_country(self):
        self.get_rad_btn_demo_country().click()

    def click_rad_btn_tripura(self):
        self.get_rad_btn_tripura().click()

    def enter_phone_number_field(self, number):
        self.get_phone_number_field().send_keys(number)

    def enter_role_name_field(self, role_name):
        self.get_role_name_field().send_keys(role_name)



