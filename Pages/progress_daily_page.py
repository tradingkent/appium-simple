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


class ProgDaily(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    patient_tab = (By.XPATH, "//android.widget.TextView[@text='PATIENTS']")
    progress_tab = (By.XPATH, "//android.widget.TextView[@text='PROGRESS']")
    sync_btn = (By.ID, "org.simple.clinic.staging:id/statusImageView")
    back_btn = (By.XPATH, "//android.view.View[@text='BACK']")

    daily_btn = (By.XPATH, "//android.view.View[@text='Daily']")
    daily_period_drp = (By.XPATH, "//android.widget.Spinner[@bounds='[44,748][1039,869]']")
    daily_date_rad_btn = (By.XPATH, f"//android.widget.CheckedTextView[@text='{progress_date_sel.get('daily')}']")
    reg_pat_daily_verif = (By.XPATH, "//android.view.View[@index='5']")
    follow_pat_daily_verif = (By.XPATH, "//android.view.View[@index='32']")

    reg_patients_verif = (By.XPATH, "//android.view.View[@index='4']")
    follow_patients_verif = (By.XPATH, "//android.view.View[@index='31']")

    ##Elements##

    def get_patient_tab(self):
        return self.wait.until(EC.element_to_be_clickable(self.patient_tab))

    def get_progress_tab(self):
        return self.wait.until(EC.element_to_be_clickable(self.progress_tab))

    def get_sync_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.sync_btn))

    def get_daily_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.daily_btn))

    def get_back_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.back_btn))

    def get_daily_period_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.daily_period_drp))

    def get_daily_date_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.daily_date_rad_btn))

    def get_reg_pat_daily_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.reg_pat_daily_verif))

    def get_follow_pat_daily_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.follow_pat_daily_verif))

    def get_reg_patients_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.reg_patients_verif))

    def get_follow_patients_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.follow_patients_verif))

    ##Methods##

    def click_progress_tab(self):
        self.get_progress_tab().click()

    def click_daily_btn(self):
        time.sleep(2)
        self.get_daily_btn().click()

    def click_daily_period_drp(self):
        self.get_daily_period_drp().click()

    def click_daily_date_rad_btn(self):
        time.sleep(2)
        for i in range(5):
            end_ycor = 806
            try:
                value = self.get_daily_date_rad_btn().is_displayed()
                if value is True:
                    break
            except:
                self.driver.swipe(540, 1584, 522, end_ycor, 300)
                continue

        self.get_daily_date_rad_btn().click()

    def verif_daily(self):
        time.sleep(2)
        for i in range(2):
            self.driver.swipe(551, 1634, 533, 1406, 200)

        reg_patients = self.get_reg_patients_verif()
        reg_daily = self.get_reg_pat_daily_verif()
        fol_patients = self.get_follow_patients_verif()
        fol_daily = self.get_follow_pat_daily_verif()

        assert reg_patients.text == 'Registered patients', 'Registered Patients not displayed'
        assert int(reg_daily.text) != 0, 'No Registered Patients'
        print('Daily Registered Patient Success')

        assert fol_patients.text == 'Follow-up patients', 'Follow-up patients not displayed'
        assert int(fol_daily.text) != 0, 'No Follow-up Patients'
        print('Daily Follow-up Patient Success')

    def click_back_btn(self):
        for i in range(3):
            self.get_scroll(533, 1406, 551, 1634, 200)

        time.sleep(2)
        self.get_back_btn().click()
