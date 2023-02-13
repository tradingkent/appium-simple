import time
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.base_driver import BaseDriver
from Utilities.common import NameGenerator
from Utilities.data import verif, country_list_verif, region_clinic_list_verif, facility_name_list_verif, details, \
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif, removal_verif, new_details_verif, \
    new_details_edit

name_generator = NameGenerator()


class ModDetails(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    edit_patient_btn = (By.ID, "org.simple.clinic.staging:id/editPatientButton")
    edit_phone_number = (By.ID, "org.simple.clinic.staging:id/phoneNumberEditText")
    edit_age = (By.ID, "org.simple.clinic.staging:id/ageEditText")
    female_rad_btn = (By.ID, "org.simple.clinic.staging:id/femaleRadioButton")
    edit_address = (By.ID, "org.simple.clinic.staging:id/streetAddressEditText")
    edit_village = (By.ID, "org.simple.clinic.staging:id/colonyOrVillageEditText")
    edit_district = (By.ID, "org.simple.clinic.staging:id/districtEditText")
    edit_state = (By.ID, "org.simple.clinic.staging:id/stateEditText")
    del_patient = (By.ID, "org.simple.clinic.staging:id/deletePatient")
    save_edit = (By.ID, "org.simple.clinic.staging:id/saveButton")
    clear_text = (By.ID, "org.simple.clinic.staging:id/text_input_end_icon")

    reason_duplicate_rad = (By.XPATH, "//android.widget.RadioButton[@text='This is a duplicate patient']")
    reason_mistake_rad = (By.XPATH, "//android.widget.RadioButton[@text='Patient registered by mistake']")
    reason_died_rad = (By.XPATH, "//android.widget.RadioButton[@text='Died']")

    prompt_del = (By.ID, "android:id/button1")
    prompt_cancel = (By.ID, "android:id/button2")

    search_field_home = (By.ID, "org.simple.clinic.staging:id/searchPatientsButton")
    search_patient_box = (By.ID, "org.simple.clinic.staging:id/searchQueryTextInputLayout")

    #Verif
    name_verif = (By.ID, "org.simple.clinic.staging:id/fullNameTextView")
    address_verif = (By.ID, "org.simple.clinic.staging:id/addressTextView")
    contact_verif = (By.ID, "org.simple.clinic.staging:id/contactTextView")
    search_verif_no_res = (By.ID, "org.simple.clinic.staging:id/noSearchResultsTextView")

    # 515,1261, 558,518

    ##Elements##

    def get_edit_patient_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_patient_btn))

    def get_edit_phone_number(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_phone_number))

    def get_edit_age(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_age))

    def get_female_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.female_rad_btn))

    def get_edit_address(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_address))

    def get_edit_village(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_village))

    def get_edit_district(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_district))

    def get_edit_state(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_state))

    def get_del_patient(self):
        return self.wait.until(EC.element_to_be_clickable(self.del_patient))

    def get_save_edit(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_edit))

    def get_clear_text(self):
        return self.wait.until(EC.element_to_be_clickable(self.clear_text))

    def get_reason_duplicate_rad(self):
        return self.wait.until(EC.element_to_be_clickable(self.reason_duplicate_rad))

    def get_prompt_del(self):
        return self.wait.until(EC.element_to_be_clickable(self.prompt_del))

    def get_search_field_home(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_field_home))

    def get_search_patient_box(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_patient_box))

    def get_name_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.name_verif))

    def get_address_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.address_verif))

    def get_contact_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.contact_verif))

    def get_search_verif_no_res(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_verif_no_res))

    ##Methods##

    def click_edit_patient_btn(self):
        self.get_edit_patient_btn().click()

    def click_edit_phone_number(self, new_number):
        self.get_edit_phone_number().click()
        time.sleep(2)
        self.get_clear_text().click()
        self.get_edit_phone_number().send_keys(new_number)

    def click_edit_age(self, new_age):
        self.get_edit_age().click()
        time.sleep(2)
        self.get_clear_text().click()
        self.get_edit_age().send_keys(new_age)

    def click_female_rad_btn(self):
        self.get_female_rad_btn().click()
        for i in range(2):
            self.get_scroll(515, 1261, 558, 518, 300)

    def click_edit_address(self, new_address):
        self.get_edit_address().click()
        time.sleep(2)
        self.get_clear_text().click()
        self.get_edit_address().send_keys(new_address)

    def click_edit_village(self, new_village):
        self.get_edit_village().click()
        time.sleep(2)
        self.get_clear_text().click()
        self.get_edit_village().send_keys(new_village)

    def click_save_edit(self):
        self.get_save_edit().click()
        time.sleep(2)

        new_name_verif = self.get_name_verif()
        new_address_verif = self.get_address_verif()
        new_contact_verif = self.get_contact_verif()

        assert new_name_verif.text == name_generator.names[0]+new_details_verif.get('name_verif'), 'Name not updated'
        assert new_address_verif.text == new_details_verif.get('address_verif'), 'Address not updated'
        assert new_contact_verif.text == new_details_edit.get('number')
        print('Success Edit Patient Details')

    def click_edit_del_patient_btn(self):
        self.get_edit_patient_btn().click()

    def click_del_patient(self):
        self.get_del_patient().click()

    def click_reason_duplicate_rad(self):
        self.get_reason_duplicate_rad().click()

    def click_prompt_del(self):
        self.get_prompt_del().click()

    def click_search_add_patient(self):
        self.get_search_field_home().click()

    def enter_search_patient_box(self, pat_name):
        self.get_search_patient_box().click()
        user_action = ActionChains(self.driver)
        user_action.send_keys(pat_name).perform()
        time.sleep(2)

        search_result_del = self.get_search_verif_no_res()
        assert search_result_del.text == new_details_verif.get('no_search'), 'Patient record not deleted'
        print('Success Patient Record Deletion')

        for i in range(2):
            self.driver.back()







