import time
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
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

    medicine_btn = (By.ID, "org.simple.clinic.staging:id/updateButton")
    bp_btn = (By.ID, "org.simple.clinic.staging:id/addNewBP")
    diabetes_btn = (By.ID, "org.simple.clinic.staging:id/addNewBloodSugar")
    teleconsult_btn = (By.ID, "org.simple.clinic.staging:id/teleconsultButton")
    save_btn = (By.ID, "org.simple.clinic.staging:id/doneButton")

    #After click medecine
    medicine_list = (By.XPATH, "//android.widget.LinearLayout/android.widget.CheckBox")
    add_anthr_med = (By.ID, "org.simple.clinic.staging:id/prescribeddrug_item_addnewprescription")
    search_med = (By.ID, "org.simple.clinic.staging:id/searchQueryEditText")
    aspirin_od = (By.XPATH, "//android.widget.TextView[@text='Aspirin, 150 mg, OD']")
    add_btn = (By.ID, "org.simple.clinic.staging:id/saveButton")
    save_btn_add_drug = (By.ID, "org.simple.clinic.staging:id/prescribeddrugs_done")

    #After click of BP
    systolic_field = (By.ID, "org.simple.clinic.staging:id/systolicEditText")
    diastolic_field = (By.ID, "org.simple.clinic.staging:id/diastolicEditText")

    #After click of Diabetes
    rbs_option = (By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text='Random blood sugar (RBS)']")
    rbs_field = (By.XPATH, "org.simple.clinic.staging:id/bloodSugarReadingEditText")








    ##Elements##

    def get_search_patient(self):
        return self.wait.until(EC.element_to_be_clickable(self.search_patient))

    def get_reg_new_patient(self):
        return self.wait.until(EC.element_to_be_clickable(self.reg_new_patient))

    ##Methods##

    def click_search_patient(self):
        user_action = TouchAction(self.driver)
        user_action.tap(x=547, y=488).perform()

    def click_reg_new_patient(self):
        self.get_reg_new_patient().click()

