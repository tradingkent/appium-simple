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
from Utilities.common import LogFunc
from Utilities.data import verif, country_list_verif, region_clinic_list_verif, facility_name_list_verif, details, \
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif, removal_verif

lg = LogFunc()
logger = lg.get_log()


class RemDetails(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    medicine_btn = (By.ID, "org.simple.clinic.staging:id/updateButton")

    med_amlo = (By.XPATH, "//android.widget.CheckBox[@text='Amlodipine']")
    med_ateno = (By.XPATH, "//android.widget.CheckBox[@text='Atenolol']")
    med_chlor = (By.XPATH, "//android.widget.CheckBox[@text='Chlorthalidone']")
    med_aspirin = (By.XPATH, "//android.widget.CheckBox[@text='Aspirin']")

    rem_btn = (By.XPATH, "//android.widget.TextView[@text='Remove']")
    remove_btn = (By.ID, "org.simple.clinic.staging:id/removeButton")
    save_btn = (By.ID, "org.simple.clinic.staging:id/prescribeddrugs_done")

    bp_edit = (By.ID, "org.simple.clinic.staging:id/editButton")
    systolic_field = (By.ID, "org.simple.clinic.staging:id/systolicEditText")
    diastolic_field = (By.ID, "org.simple.clinic.staging:id/diastolicEditText")
    remove_bp_btn = (By.ID, "org.simple.clinic.staging:id/removeBloodPressureButton")
    prompt_remove_btn = (By.ID, "android:id/button1")
    prompt_cancel_btn = (By.ID, "android:id/button2")

    edit_save_btn = (By.ID, "org.simple.clinic.staging:id/doneButton")
    not_now_prompt = (By.ID, "android:id/button2")

    search_field_home = (By.ID, "org.simple.clinic.staging:id/searchPatientsButton")
    search_patient_box = (By.ID, "org.simple.clinic.staging:id/searchQueryTextInputLayout")
    search_new_patient = (By.ID, "org.simple.clinic.staging:id/patientNameAgeGenderLabel")
    done_btn = (By.ID, "org.simple.clinic.staging:id/doneButton")

    # verif
    med_removed_verif = (By.ID, "org.simple.clinic.staging:id/emptyMedicinesTextView")
    bp_edit_readings = (By.ID, "org.simple.clinic.staging:id/readingsTextView")
    bp_remove_verif = (By.ID, "org.simple.clinic.staging:id/placeHolderMessageTextView")

    ##Elements##

    def get_medicine_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.medicine_btn))

    def get_med_amlo(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_amlo))

    def get_med_ateno(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_ateno))

    def get_med_chlor(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_chlor))

    def get_med_aspirin(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_aspirin))

    def get_rem_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.rem_btn))

    def get_remove_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.remove_btn))

    def get_save_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_btn))

    def get_med_removed_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_removed_verif))

    def get_bp_edit(self):
        return self.wait.until(EC.element_to_be_clickable(self.bp_edit))

    def get_remove_bp_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.remove_bp_btn))

    def get_prompt_remove_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.prompt_remove_btn))

    def get_systolic_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.systolic_field))

    def get_diastolic_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.diastolic_field))

    def get_bp_edit_readings(self):
        return self.wait.until(EC.element_to_be_clickable(self.bp_edit_readings))

    def get_bp_remove_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.bp_remove_verif))

    def get_edit_save_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.edit_save_btn))

    def get_not_now_prompt(self):
        return self.wait.until(EC.element_to_be_clickable(self.not_now_prompt))

    def get_search_field_home(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_field_home))

    def get_search_patient_box(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_patient_box))

    def get_search_new_patient(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_new_patient))

    def get_done_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.done_btn))

    ##Methods##

    def click_medicine_btn(self):
        self.get_medicine_btn().click()

    def click_uncheck_meds(self):
        self.get_med_aspirin().click()
        self.get_remove_btn().click()
        self.get_med_amlo().click()
        self.get_rem_btn().click()
        self.get_med_ateno().click()
        self.get_rem_btn().click()
        self.get_med_chlor().click()
        self.get_rem_btn().click()
        time.sleep(2)

        uncheck_amlo = self.get_med_amlo().get_attribute('checked')
        uncheck_ateno = self.get_med_ateno().get_attribute('checked')
        uncheck_chlor = self.get_med_chlor().get_attribute('checked')

        assert uncheck_amlo == 'false', 'Medicine not unchecked'
        assert uncheck_ateno == 'false', 'Medicine not unchecked'
        assert uncheck_chlor == 'false', 'Medicine not unchecked'

        logger.info('Uncheck of meds success')

    def click_save_btn(self):
        self.get_save_btn().click()
        time.sleep(2)

        rem_meds_verif = self.get_med_removed_verif()
        assert rem_meds_verif.text == removal_verif.get('med_removed'), 'Meds still exist'
        logger.info('Success removal of Meds')

    def click_bp_edit(self):
        self.get_bp_edit().click()

    def enter_sys_dia_edit(self, sys_edit, dia_edit):
        self.get_systolic_field().click()
        for i in range(2):
            self.get_keys_keycode(22)
        for i in range(3):
            self.get_keys_keycode(67)
        self.get_systolic_field().send_keys(sys_edit)

        for i in range(3):
            self.get_keys_keycode(67)
        self.get_diastolic_field().send_keys(dia_edit)
        time.sleep(2)
        # self.get_tap_screen(931, 2048) # emulator
        self.get_tap_screen(932, 2209)  # real device

        bp_edit_readings = self.get_bp_edit_readings()
        assert bp_edit_readings.text == removal_verif.get('new_bp_edit'), 'New BP not detected'
        logger.info('New BP detected')

    def click_bp_edit_remove(self):
        self.get_bp_edit().click()

    def click_remove_bp_btn(self):
        self.get_remove_bp_btn().click()

    def click_remove_prompt_bp_btn(self):
        self.get_prompt_remove_btn().click()
        time.sleep(2)

        bp_removed = self.get_bp_remove_verif()
        assert bp_removed.text == removal_verif.get('bp_removed'), 'BP not removed'
        logger.info('BP removal success')

    def click_edit_save_btn(self):
        self.get_edit_save_btn().click()

    def click_not_now_prompt(self):
        self.get_not_now_prompt().click()

    def click_search_add_patient(self):
        self.get_search_field_home().click()

    def enter_search_patient_box(self, pat_name):
        self.get_search_patient_box().click()
        user_action = ActionChains(self.driver)
        user_action.send_keys(pat_name).perform()

    def click_search_new_patient(self):
        time.sleep(2)
        self.get_search_new_patient().click()

        meds_verif_search = self.get_med_removed_verif()
        bp_verif_search = self.get_bp_remove_verif()

        assert meds_verif_search.text == removal_verif.get('med_removed'), 'Meds still exist'
        assert bp_verif_search.text == removal_verif.get('bp_removed'), 'BP not removed'
        logger.info('Search Update Meds Success')

    def click_done_btn(self):
        self.get_done_btn().click()
