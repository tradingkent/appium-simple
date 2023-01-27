import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#from Config.config import desired_cap
from Utilities.data import verif, country_list_verif, region_clinic_list_verif



class LandingPage():

    def __init__(self, driver, wait):  # driver,
        self.driver = driver
        self.wait = wait

    ##Locators##

    next_button = (By.ID, "org.simple.clinic.staging:id/nextButton")
    get_started_button = (By.ID, "org.simple.clinic.staging:id/getStartedButton")
    rad_btn_demo_country = (By.XPATH, "//android.widget.RadioButton[@text='Demo Country']")
    rad_btn_tripura = (By.XPATH, "//android.widget.RadioButton[@text='Tripura']")
    phone_number_field = (By.ID, "org.simple.clinic.staging:id/phoneNumberEditText")
    role_name_field = (By.ID, "org.simple.clinic.staging:id/fullNameEditText")


    # New code here
    sec_pin_one = (By.ID, "org.simple.clinic.staging:id/pinEditText")
    sec_pin_two = (By.ID, "org.simple.clinic.staging:id/confirmPinEditText")
    skip_button = (By.ID, "org.simple.clinic.staging:id/skipButton")
    allow_access_btn = (By.ID, "org.simple.clinic.staging:id/allowAccessButton")
    allow_prompt = (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    facility_name = (By.XPATH, "//android.widget.LinearLayout[@bounds='[22,259][1058,525]']")
    yes_button = (By.ID, "org.simple.clinic.staging:id/yesButton")

    country_list = (By.XPATH, "//android.widget.LinearLayout/android.widget.RadioButton")
    region_clinic_list = (By.XPATH, "//android.view.ViewGroup/android.widget.RadioButton")

    landing_verif = (By.XPATH, "//android.widget.TextView[@text='PATIENTS']")

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

    def get_sec_pin_one(self):
        return self.driver.find_element(*self.sec_pin_one)

    def get_sec_pin_two(self):
        return self.driver.find_element(*self.sec_pin_two)

    def get_allow_access_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.allow_access_btn))

    def get_allow_prompt(self):
        return self.wait.until(EC.element_to_be_clickable(self.allow_prompt))

    def get_facility_name(self):
        return self.wait.until(EC.element_to_be_clickable(self.facility_name))

    def get_yes_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.yes_button))

    def get_skip_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.skip_button))

    def get_country_list(self):
        return self.driver.find_elements(*self.country_list)

    def get_region_clinic_list(self):
        return self.driver.find_elements(*self.region_clinic_list)

    def get_landing_verif(self):
        return self.driver.find_element(*self.landing_verif)

    ##Methods##

    def click_next_button(self):
        self.get_next_button().click()

    def click_get_started_button(self):
        self.get_get_started_button().click()

    def click_rad_btn_demo_country(self):
        time.sleep(2)
        country_list = self.get_country_list()

        empty_country_list = []
        for country in country_list:
            empty_country_list.append(country.text)
        assert empty_country_list == country_list_verif, 'Expected Country list not the same'
        print(empty_country_list)
        print(country_list_verif)
        print('Country List Success')
        self.get_rad_btn_demo_country().click()

    def click_rad_btn_tripura(self):
        time.sleep(2)
        region_clinic_list = self.get_region_clinic_list()

        empty_region_clinic_list = []
        for region_clinic in region_clinic_list:
            empty_region_clinic_list.append(region_clinic.text)
        assert empty_region_clinic_list == region_clinic_list_verif, 'Expected Region Clinic list not the same'
        print(empty_region_clinic_list)
        print(region_clinic_list_verif)
        print('Region Clinic List Success')
        self.get_rad_btn_tripura().click()

    def enter_phone_number_field(self, number):
        self.get_phone_number_field().send_keys(number)

    def enter_role_name_field(self, role_name):
        self.get_role_name_field().send_keys(role_name)

    def enter_sec_pin_one(self, pin_one):
        self.get_sec_pin_one().send_keys(pin_one)

    def enter_sec_pin_two(self, pin_two):
        time.sleep(2)
        self.get_sec_pin_two().send_keys(pin_two)

    def click_allow_access_btn(self):
        self.get_allow_access_btn().click()

    def click_allow_prompt(self):
        self.get_allow_prompt().click()

    def click_facility_name(self):
        self.get_facility_name().click()

    def click_yes_button(self):
        self.get_yes_button().click()

    def click_skip_button(self):
        self.get_skip_button().click()
        time.sleep(5)
        home_page = self.get_landing_verif()
        assert home_page.text == verif.get('lan_to_home_verif'), 'Failed to proceed to Homepage'
        print('Landing Page Success')


