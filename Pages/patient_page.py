import time
import pytest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.data import verif, country_list_verif, region_clinic_list_verif, facility_name_list_verif, details


class PatientPage():

    def __init__(self, driver, wait):  # driver,
        self.driver = driver
        self.wait = wait

    ##Locators##

    search_patient = (By.XPATH, "//android.widget.Button[@text='Enter name, phone or ID']")
    reg_new_patient = (By.ID, "org.simple.clinic.staging:id/newPatientButton")
    patient_name_field = (By.ID, "org.simple.clinic.staging:id/fullNameEditText")
    age_field = (By.ID, "org.simple.clinic.staging:id/ageEditText")
    dob_field = (By.ID, "org.simple.clinic.staging:id/dateOfBirthEditText")
    male_rad_btn = (By.ID, "org.simple.clinic.staging:id/maleRadioButton")
    female_rad_btn = (By.ID, "org.simple.clinic.staging:id/femaleRadioButton")
    trans_rad_btn = (By.ID, "org.simple.clinic.staging:id/transgenderRadioButton")
    phone_field = (By.ID, "org.simple.clinic.staging:id/phoneNumberEditText")
    address_field = (By.ID, "org.simple.clinic.staging:id/streetAddressEditText")
    village_field = (By.ID, "org.simple.clinic.staging:id/colonyOrVillageEditText")
    next_btn = (By.ID, "org.simple.clinic.staging:id/saveButton")

    illness_list = (By.XPATH, "//android.view.ViewGroup/android.widget.TextView")

    next_button = (By.ID, "org.simple.clinic.staging:id/nextButton")
    save_button = (By.ID, "org.simple.clinic.staging:id/doneButton")
    prompt_not_now = (By.ID, "android:id/button2")

    search_field_home = (By.ID, "org.simple.clinic.staging:id/searchPatientsButton")

    search_patient_box = (By.ID, "org.simple.clinic.staging:id/searchQueryTextInputLayout")

    search_patient_verif = (By.ID, "org.simple.clinic.staging:id/patientNameAgeGenderLabel")

    search_new_patient = (By.ID, "org.simple.clinic.staging:id/patientNameAgeGenderLabel")

    ##Elements##

    def get_search_patient(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_patient))

    def get_reg_new_patient(self):
        return self.wait.until(EC.element_to_be_clickable(self.reg_new_patient))

    def get_patient_name_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.patient_name_field))
        # return self.driver.find_element(*self.patient_name_field)

    def get_age_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.age_field))
        # return self.driver.find_element(*self.age_field)

    def get_dob_field(self):
        return self.driver.find_element(*self.dob_field)

    def get_male_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.male_rad_btn))

    def get_female_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.female_rad_btn))

    def get_trans_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.trans_rad_btn))

    def get_phone_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.phone_field))

    def get_address_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.address_field))

    def get_village_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.village_field))

    def get_next_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.next_btn))

    def get_illness_list(self):
        return self.driver.find_element(*self.illness_list)

    def get_yes_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.yes_rad_btn))

    def get_next_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.next_button))

    def get_save_button(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_button))

    def get_prompt_not_now(self):
        return self.wait.until(EC.element_to_be_clickable(self.prompt_not_now))

    def get_search_field_home(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_field_home))

    def get_search_patient_box(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_patient_box))

    def get_search_patient_verif(self):
        return self.driver.find_element(*self.search_patient_verif)

    def get_search_new_patient(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_new_patient))

    # def get_no_rad_btn(self):
    # return self.wait.until(EC.element_to_be_clickable(self.no_rad_btn))

    ##Methods##

    def click_search_patient(self):
        user_action = TouchAction(self.driver)
        user_action.tap(x=547, y=488).perform()

    def click_reg_new_patient(self):
        self.get_reg_new_patient().click()

    def enter_patient_name_field(self, patient_name):
        self.get_patient_name_field().send_keys(patient_name)

    def enter_age_field(self, age):
        self.get_age_field().send_keys(age)

    def enter_dob_field(self, dob):
        self.get_dob_field().send_keys(dob)

    def click_male_rad_btn(self):
        self.get_male_rad_btn().click()

    def click_female_rad_btn(self):
        self.get_female_rad_btn().click()

    def click_trans_rad_btn(self):
        self.get_trans_rad_btn().click()

    def enter_phone_field(self, phone):
        self.get_phone_field().send_keys(phone)

    def enter_address_field(self, address):
        self.get_address_field().send_keys(address)

    def enter_village_field(self, village):
        self.get_village_field().send_keys(village)

    def click_next_btn(self):
        self.get_next_btn().click()

    def click_scroll(self):
        for i in range(3):
            self.driver.swipe(554, 1152, 526, 428, 300)

    def check_illness_list(self):
        illness_list = self.get_illness_list()
        print(illness_list.text)

    def click_yes_rad_btn(self):
        start = 0
        while start < 2:
            start += 1
            no_rad_btn = (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                    "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                                    "FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/"
                                    f"android.widget.LinearLayout/androidx.cardview.widget.CardView[{start}]/"
                                    "android.view.ViewGroup/android.view.ViewGroup/android.widget.RadioButton[1]")
            self.wait.until(EC.element_to_be_clickable(no_rad_btn)).click()

    def click_yes_rad_btn_two(self):
        start = 0
        while start < 3:
            start += 1
            no_rad_btn = (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                    f"android.widget.FrameLayout/android.widget.LinearLayout/android."
                                    f"widget.FrameLayout/android.widget.RelativeLayout/android.widget"
                                    f".ScrollView/android.widget.LinearLayout/androidx.cardview.widget"
                                    f".CardView[3]/android.widget.LinearLayout/android.widget.FrameLayout[{start}]"
                                    f"/android.widget.RelativeLayout/android.widget.LinearLayout/android."
                                    f"view.ViewGroup/android.widget.RadioButton[1]")
            self.wait.until(EC.element_to_be_clickable(no_rad_btn)).click()

    def click_no_rad_btn_two(self):
        start = 0
        while start < 3:
            start += 1
            no_rad_btn = (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                    f"android.widget.FrameLayout/android.widget.LinearLayout/android."
                                    f"widget.FrameLayout/android.widget.RelativeLayout/android.widget"
                                    f".ScrollView/android.widget.LinearLayout/androidx.cardview.widget"
                                    f".CardView[3]/android.widget.LinearLayout/android.widget.FrameLayout[{start}]"
                                    f"/android.widget.RelativeLayout/android.widget.LinearLayout/android."
                                    f"view.ViewGroup/android.widget.RadioButton[2]")
            self.wait.until(EC.element_to_be_clickable(no_rad_btn)).click()

    def click_no_rad_btn(self):
        start = 0
        while start < 2:
            start += 1
            no_rad_btn = (By.XPATH, f"/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout"
                                    "/android.widget.FrameLayout/android.widget.LinearLayout/android.widget."
                                    "FrameLayout/android.widget.RelativeLayout/android.widget.ScrollView/"
                                    f"android.widget.LinearLayout/androidx.cardview.widget.CardView[{start}]/"
                                    "android.view.ViewGroup/android.view.ViewGroup/android.widget.RadioButton[2]")
            self.wait.until(EC.element_to_be_clickable(no_rad_btn)).click()

    def click_next_button(self):
        self.get_next_button().click()

    def click_save_button(self):
        self.get_save_button().click()

    def click_prompt_not_now(self):
        self.get_prompt_not_now().click()

    def click_search_add_patient(self):
        self.get_search_field_home().click()

    def enter_search_patient_box(self, pat_name):
        self.get_search_patient_box().click()
        user_action = ActionChains(self.driver)
        user_action.send_keys(pat_name).perform()
        time.sleep(4)
        pat_name_verif = self.get_search_patient_verif()
        assert pat_name_verif.text == pat_name + ', M, 25', 'Search of patient failed'
        print('Search of patient success')

    def click_search_new_patient(self):
        self.get_search_new_patient().click()
