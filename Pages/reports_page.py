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
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif, removal_verif, progress_date_sel

lg = LogFunc()
logger = lg.get_log()


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

    def get_hyper_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.hyper_btn))

    def get_back_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.back_btn))

    def get_hyper_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.hyper_verif))

    def get_assigned_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.assigned_verif))

    def get_assigned_val_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.assigned_val_verif))

    def get_total_reg_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.total_reg_verif))

    def get_monthly_fol_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.monthly_fol_verif))

    ##Methods##

    def click_hyper_btn(self):
        self.get_hyper_btn().click()

    def click_back_btn(self):
        self.get_back_btn().click()

    # Verif

    def verif_hyper_page(self):
        hyper_verif = self.get_hyper_verif()
        assigned_verif = self.get_assigned_verif()
        assigned_value = self.get_assigned_val_verif()
        total_reg = self.get_total_reg_verif()
        monthly_verif = self.get_monthly_fol_verif()

        assert hyper_verif.text == 'Hypertension report', 'Not Exist'
        assert assigned_verif.text == 'Assigned patients', 'Not Exist'
        assert int(assigned_value.text) != 0, 'Not Exist'
        assert total_reg.text == 'Total registered patients', 'Not Exist'
        assert monthly_verif.text == 'Monthly follow-up patients', 'Not Exist'

        logger.info('Progress Reports Success')
