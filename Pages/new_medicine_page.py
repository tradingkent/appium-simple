import time
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.data import verif, country_list_verif, region_clinic_list_verif, facility_name_list_verif, details, \
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif, meds_new_check_verif


class NewMedicine():

    def __init__(self, driver, wait):  # driver,
        self.driver = driver
        self.wait = wait

    ##Locators##

    search_field_home = (By.ID, "org.simple.clinic.staging:id/searchPatientsButton")
    search_patient_box = (By.ID, "org.simple.clinic.staging:id/searchQueryTextInputLayout")
    search_new_patient = (By.ID, "org.simple.clinic.staging:id/patientNameAgeGenderLabel")

    medicine_btn = (By.ID, "org.simple.clinic.staging:id/updateButton")
    medicine_list = (By.XPATH, "//android.widget.LinearLayout/android.widget.CheckBox")
    add_anthr_med = (By.ID, "org.simple.clinic.staging:id/prescribeddrug_item_addnewprescription")
    search_med = (By.ID, "org.simple.clinic.staging:id/searchQueryEditText")
    aspirin_od = (By.XPATH, "//android.widget.TextView[@text='Aspirin, OD']")
    med_dos = (By.ID, "org.simple.clinic.staging:id/drugDosageEditText")
    frequency_drp = (By.ID, "org.simple.clinic.staging:id/drugFrequencyEditText")
    freq_bd = (By.XPATH, "//android.widget.CheckedTextView[@text='BD']")
    add_btn = (By.ID, "org.simple.clinic.staging:id/saveButton")
    save_btn = (By.ID, "org.simple.clinic.staging:id/prescribeddrugs_done")

    # Verif
    meds_selected_verif = (By.XPATH, "//android.widget.TextView[@index='1']")

    ##Elements##

    def get_search_field_home(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_field_home))

    def get_search_patient_box(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_patient_box))

    def get_search_new_patient(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_new_patient))

    def get_medicine_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.medicine_btn))

    def get_medicine_list(self):
        return self.driver.find_elements(*self.medicine_list)

    def get_add_anthr_med(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_anthr_med))

    def get_search_med(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_med))

    def get_aspirin_od(self):
        return self.wait.until(EC.element_to_be_clickable(self.aspirin_od))

    def get_med_dos(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_dos))

    def get_frequency_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.frequency_drp))

    def get_freq_bd(self):
        return self.wait.until(EC.element_to_be_clickable(self.freq_bd))

    def get_add_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.add_btn))

    def get_save_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_btn))

    # Verif

    def get_meds_selected_verif(self):
        return self.driver.find_elements(*self.meds_selected_verif)

    ##Methods##

    def click_search_add_patient(self):
        self.get_search_field_home().click()

    def enter_search_patient_box(self, pat_name):
        self.get_search_patient_box().click()
        user_action = ActionChains(self.driver)
        user_action.send_keys(pat_name).perform()

    def click_search_new_patient(self):
        time.sleep(2)
        self.get_search_new_patient().click()

    def click_medicine_btn(self):
        self.get_medicine_btn().click()
        time.sleep(2)
        for i in range(2):
            self.driver.swipe(493, 1613, 500, 721, 300)

    def click_add_anthr_med(self):
        self.get_add_anthr_med().click()

    def enter_search_med(self, new_med):
        self.get_search_med().send_keys(new_med)

    def click_aspirin_od(self):
        self.get_aspirin_od().click()

    def enter_med_dos(self, new_dos):
        self.get_med_dos().send_keys(new_dos)

    def click_frequency_drp(self):
        self.get_frequency_drp().click()

    def click_freq_bd(self):
        self.get_freq_bd().click()

    def click_add_btn(self):
        self.get_add_btn().click()
        time.sleep(2)

        med_list = self.get_medicine_list()
        emp_med_list = []
        for meds in med_list:
            emp_med_list.append(meds.text)

        print(emp_med_list)
        assert medical_data.get('added_new_med') in emp_med_list, 'New Medicine not added'
        print('Success: New medicine added')

    def click_save_btn(self):
        self.get_save_btn().click()
        time.sleep(2)

        med_check_verif = self.get_meds_selected_verif()
        emp_meds_verif = []
        for meds_verif in med_check_verif:
            emp_meds_verif.append(meds_verif.text)
        emp_meds_verif.pop(0)
        emp_meds_verif.pop(-1)
        assert emp_meds_verif == meds_new_check_verif, 'Added New Medicine is not located'
        print(emp_meds_verif)
        print(meds_new_check_verif)
        print('Success: Add Medicine')






