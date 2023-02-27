import time
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.base_driver import BaseDriver
from Utilities.common import LogFunc
from Utilities.data import verif, country_list_verif, region_clinic_list_verif, facility_name_list_verif, details, \
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif, change_fac_verif

lg = LogFunc()
logger = lg.get_log()

class ChangeFac(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    change_fac_btn = (By.ID, "org.simple.clinic.staging:id/changeAssignedFacilityButton")
    new_fac_uhc_rees = (By.XPATH, "//android.widget.TextView[@text='UHC Rees']")
    new_fac_hwc_desai = (By.XPATH, "//android.widget.TextView[@text='HWC Desaiganj']")
    new_fac_verif = (By.ID, "org.simple.clinic.staging:id/assignedFacilityTextView")

    fac_sel_btn = (By.ID, "org.simple.clinic.staging:id/facilitySelectButton")
    facility_name_list = (By.XPATH, "//android.widget.LinearLayout/android.widget.TextView")
    yes_btn = (By.ID, "org.simple.clinic.staging:id/yesButton")
    sync_btn = (By.ID, "org.simple.clinic.staging:id/statusImageView")

    ##Elements##

    def get_change_fac_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.change_fac_btn))

    def get_new_fac_uhc_rees(self):
        return self.wait.until(EC.element_to_be_clickable(self.new_fac_uhc_rees))

    def get_new_fac_hwc_desai(self):
        return self.wait.until(EC.element_to_be_clickable(self.new_fac_hwc_desai))

    def get_new_fac_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.new_fac_verif))

    def get_fac_sel_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.fac_sel_btn))

    def get_facility_name_list(self):
        return self.driver.find_elements(*self.facility_name_list)

    def get_yes_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.yes_btn))

    def get_sync_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.sync_btn))

    ##Methods##

    def click_change_fac_btn(self):
        self.get_change_fac_btn().click()

    def click_new_fac_uhc_rees(self):
        self.get_new_fac_uhc_rees().click()
        time.sleep(2)
        new_fac_verif = self.get_new_fac_verif()
        assert new_fac_verif.text == change_fac_verif.get('new_faci'), 'Facility not changed'
        logger.info('Facility change success')

    def click_fac_sel_btn(self):
        self.get_fac_sel_btn().click()
        time.sleep(2)
        facility_name_list = self.get_facility_name_list()

        empty_facility_name_list = []
        for facility_name in facility_name_list:
            empty_facility_name_list.append(facility_name.text)
        assert empty_facility_name_list == facility_name_list_verif, 'Expected Facility Name list not the same'
        logger.info(empty_facility_name_list)
        logger.info(facility_name_list_verif)
        logger.info('Facility Name List Success')

    def click_new_fac(self):
        self.get_new_fac_uhc_rees().click()

    def click_new_fac_hwc(self):
        self.get_new_fac_hwc_desai().click()

    def click_yes_btn(self):
        self.get_yes_btn().click()
        time.sleep(2)

        new_fac = self.get_fac_sel_btn()
        assert new_fac.text == change_fac_verif.get('new_faci'), 'Facility not changed'
        logger.info('Facility change success')

    def click_yess_btn(self):
        self.get_yes_btn().click()
        time.sleep(2)


