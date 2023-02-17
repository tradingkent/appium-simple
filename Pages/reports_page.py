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
from Utilities.data import verif, country_list_verif, region_clinic_list_verif, facility_name_list_verif, details, \
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif, removal_verif, progress_date_sel


class ReportsHyper(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    hyper_btn = (By.XPATH, "//android.view.View[@text='Hypertension']")
    back_btn = (By.XPATH, "//android.view.View[@text='BACK']")


    hyper_verif = (By.XPATH, "//android.view.View[@text='Hypertension report']")
    assigned_verif = (By.XPATH, "//android.view.View[@text='Assigned patients']")
    assigned_val_verif = (By.XPATH, "//android.view.View[@index='4']")
    total_reg_verif = (By.XPATH, "//android.view.View[@text='Total registered patients']")
    monthly_fol_verif = (By.XPATH, "//android.view.View[@text='Monthly follow-up patients']")


    ##Elements##

    def get_patient_tab(self):
        return self.wait.until(EC.element_to_be_clickable(self.patient_tab))

    ##Methods##

    def click_progress_tab(self):
        self.get_progress_tab().click()

