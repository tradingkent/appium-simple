import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.base_driver import BaseDriver
from Utilities.common import LogFunc
from Utilities.data import verif, country_list_verif, region_clinic_list_verif, facility_name_list_verif, details

lg = LogFunc()
logger = lg.get_log()


class LandingPage(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    next_button = (By.ID, "org.simple.clinic.staging:id/nextButton")
    next_btn_verif = (By.XPATH, "//android.widget.Button[@text='NEXT']")
    get_started_button = (By.ID, "org.simple.clinic.staging:id/getStartedButton")
    rad_btn_demo_country = (By.XPATH, "//android.widget.RadioButton[@text='Demo Country']")
    rad_btn_tripura = (By.XPATH, "//android.widget.RadioButton[@text='Tripura']")
    phone_number_field = (By.ID, "org.simple.clinic.staging:id/phoneNumberEditText")
    role_name_field = (By.ID, "org.simple.clinic.staging:id/fullNameEditText")

    sec_pin_one = (By.ID, "org.simple.clinic.staging:id/pinEditText")
    sec_pin_two = (By.ID, "org.simple.clinic.staging:id/confirmPinEditText")
    skip_button = (By.ID, "org.simple.clinic.staging:id/skipButton")
    allow_access_btn = (By.ID, "org.simple.clinic.staging:id/allowAccessButton")
    allow_prompt = (By.ID, "com.android.permissioncontroller:id/permission_allow_foreground_only_button")
    facility_name = (By.XPATH, "//android.widget.LinearLayout[@bounds='[22,259][1058,525]']")
    yes_button = (By.ID, "org.simple.clinic.staging:id/yesButton")
    search_facility = (By.ID, "org.simple.clinic.staging:id/searchEditText")
    fac_name = (By.ID, "org.simple.clinic.staging:id/facilityNameTextView")

    country_list = (By.XPATH, "//android.widget.LinearLayout/android.widget.RadioButton")
    region_clinic_list = (By.XPATH, "//android.view.ViewGroup/android.widget.RadioButton")
    facility_name_list = (By.XPATH, "//android.widget.LinearLayout/android.widget.TextView")

    landing_verif = (By.XPATH, "//android.widget.TextView[@text='PATIENTS']")
    search_fac_name_verif = (By.ID, "org.simple.clinic.staging:id/facilityNameTextView")

    #trial
    overdue_btn = (By.XPATH, "//android.widget.TextView[@text='OVERDUE']")
    patient_btn = (By.XPATH, "//android.widget.TextView[@text='PATIENTS']")

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
        return self.wait.until(EC.element_to_be_clickable(self.phone_number_field))

    def get_role_name_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.role_name_field))

    def get_sec_pin_one(self):
        return self.wait.until(EC.element_to_be_clickable(self.sec_pin_one))

    def get_sec_pin_two(self):
        return self.wait.until(EC.element_to_be_clickable(self.sec_pin_two))

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

    def get_search_facility(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_facility))

    def get_country_list(self):
        return self.driver.find_elements(*self.country_list)

    def get_region_clinic_list(self):
        return self.driver.find_elements(*self.region_clinic_list)

    def get_facility_name_list(self):
        return self.driver.find_elements(*self.facility_name_list)

    def get_landing_verif(self):
        return self.driver.find_element(*self.landing_verif)

    def get_search_fac_name_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_fac_name_verif))

    def get_fac_name(self):
        return self.wait.until(EC.element_to_be_clickable(self.fac_name))

    def get_next_btn_verif(self):
        return self.driver.find_element(*self.next_button)

    #trial
    def get_overdue_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.overdue_btn))

    def get_patients_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.patient_btn))

    ##Methods##

    def click_next_button(self):
        time.sleep(3)
        next_button_verif = self.get_next_btn_verif()
        assert next_button_verif.text == verif.get('startup_verif'), 'App did not load successfully'
        #trial only
        #assert next_button_verif.text == 'hehe', 'App did not load successfully'
        #assert next_button_verif.text == 'haha', 'App did not load successfully'

        logger.info('App Launch Successfully')
        self.get_next_button().click()

        self.cap_screenshot('1', '1')

    def click_next_button_two(self):

        self.get_next_button().click()

        self.cap_screenshot('2', '5')

    def click_next_button_three(self):

        self.get_next_button().click()

        self.cap_screenshot('2', '7')

    def click_get_started_button(self):
        self.get_get_started_button().click()

        self.cap_screenshot('1', '2')

    def click_rad_btn_demo_country(self):
        time.sleep(2)
        self.cap_screenshot('2', '1')
        country_list = self.get_country_list()

        empty_country_list = []
        for country in country_list:
            empty_country_list.append(country.text)
        assert empty_country_list == country_list_verif, 'Expected Country list not the same'
        print(empty_country_list)
        print(country_list_verif)
        print('Country List Success')
        self.get_rad_btn_demo_country().click()
        self.cap_screenshot('2', '2')

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
        self.cap_screenshot('2', '3')

    def enter_phone_number_field(self, number):
        self.get_phone_number_field().send_keys(number)
        self.cap_screenshot('2', '4')

    def enter_role_name_field(self, role_name):
        self.get_role_name_field().send_keys(role_name)
        self.cap_screenshot('2', '6')

    def enter_sec_pin_one(self, pin_one):
        self.get_sec_pin_one().send_keys(pin_one)
        self.cap_screenshot('2', '8')

    def enter_sec_pin_two(self, pin_two):
        self.get_sec_pin_two().send_keys(pin_two)
        self.cap_screenshot('2', '9')

    def click_allow_access_btn(self):
        self.get_allow_access_btn().click()
        self.cap_screenshot('2', '10')

    def click_allow_prompt(self):
        self.get_allow_prompt().click()
        self.cap_screenshot('2', '11')
        time.sleep(3)
        facility_name_list = self.get_facility_name_list()

        empty_facility_name_list = []
        for facility_name in facility_name_list:
            empty_facility_name_list.append(facility_name.text)
        assert empty_facility_name_list == facility_name_list_verif, 'Expected Facility Name list not the same'
        print(empty_facility_name_list)
        print(facility_name_list_verif)
        print('Facility Name List Success')

    def click_facility_name(self):
        self.get_facility_name().click()

    def click_search_facility(self, search_fac):
        self.get_search_facility().send_keys(search_fac)
        time.sleep(2)

        self.cap_screenshot('2', '12')
        search_fac_name_verif = self.get_search_fac_name_verif()
        assert search_fac_name_verif.text == details.get('fac_name'), 'Unable to search facility name'
        print('Search Facility Success')
        self.get_fac_name().click()

    def click_yes_button(self):
        self.get_yes_button().click()
        self.cap_screenshot('2', '13')

    def click_skip_button(self):
        self.get_skip_button().click()
        self.cap_screenshot('2', '14')
        time.sleep(5)
        home_page = self.get_landing_verif()
        assert home_page.text == verif.get('lan_to_home_verif'), 'Failed to proceed to Homepage'
        print('Landing Page Success')


