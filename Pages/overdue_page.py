import time
import pytest
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Utilities.base_driver import BaseDriver
from Utilities.data import verif, country_list_verif, region_clinic_list_verif, facility_name_list_verif, details, \
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif, change_fac_verif

#import sl4a

empty_list = []

class OverdueDetails(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    overdue_btn = (By.XPATH, "//android.widget.TextView[@text='OVERDUE']")

    pending_call_drp = (By.XPATH, "//android.widget.TextView[@bounds='[876,611][1036,677]']")
    agreed_visit_drp = (By.XPATH, "//android.widget.TextView[@bounds='[924,812][1036,878]']")
    remind_call_drp = (By.XPATH, "//android.widget.TextView[@bounds='[924,1013][1036,1079]']")
    removed_list_drp = (By.XPATH, "//android.widget.TextView[@bounds='[924,1214][1036,1280]']")
    no_visit_drp = (By.XPATH, "//android.widget.TextView[@bounds='[924,1415][1036,1481]']")

    pending_call_check = (By.XPATH, "//android.widget.TextView[@text='Ankit Ankit, 59']") #Priya Tanvi, 29

    call_btn = (By.XPATH, "//android.widget.ImageView[@bounds='[904,808][1014,918]']")

    agreed_visit_rad_btn = (By.ID, "org.simple.clinic.staging:id/agreedToVisitTextView")
    call_later_rad_btn = (By.ID, "org.simple.clinic.staging:id/remindToCallLaterTextView")
    overdue_list_rad_btn = (By.ID, "org.simple.clinic.staging:id/removeFromOverdueListTextView")
    reason_rad_btn = (By.XPATH, "//android.widget.RadioButton[@text='Other reason']")
    done_btn = (By.ID, "org.simple.clinic.staging:id/removeAppointmentDone")
    done_btn_call_later = (By.ID, "org.simple.clinic.staging:id/saveReminder")

    ##Elements##

    def get_pending_call_check(self):
        return self.wait.until(EC.element_to_be_clickable(self.pending_call_check))

    def get_overdue_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.overdue_btn))

    def get_pending_call_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.pending_call_drp))

    def get_agreed_visit_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.agreed_visit_drp))

    def get_remind_call_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.remind_call_drp))

    def get_removed_list_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.removed_list_drp))

    def get_no_visit_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.no_visit_drp))

    def get_call_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.call_btn))

    def get_agreed_visit_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.agreed_visit_rad_btn))

    def get_call_later_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.call_later_rad_btn))

    def get_overdue_list_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.overdue_list_rad_btn))

    def get_reason_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.reason_rad_btn))

    def get_done_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.done_btn))

    def get_done_btn_call_later(self):
        return self.wait.until(EC.element_to_be_clickable(self.done_btn_call_later))

    ##Methods##

    def click_overdue_btn(self):
        self.get_overdue_btn().click()
        time.sleep(3)
        self.get_keys_keycode(3)
        time.sleep(2)
        #self.get_tap_screen(540, 1161)
        self.get_tap_screen(544, 1798)
        self.get_overdue_btn().click()

    def scroll(self):
        time.sleep(2)
        for i in range(10):
            end_ycor = 1051
            try:
                value = self.get_pending_call_check().is_displayed()
                if value is True:
                    print('Overdue Patient Found')
                    break
            except:
                #self.driver.swipe(544, 1866, 522, 870, 300)
                self.driver.swipe(507, 1740, 515, end_ycor, 300)
                continue


    def scroll_up(self):
        time.sleep(2)
        for i in range(5):
            end_ycor = 1740
            try:
                value = self.get_pending_call_drp().is_displayed()
                if value is True:
                    break
            except:
                #self.driver.swipe(522, 870, 544, 1866, 300)
                self.driver.swipe(515, 1051, 507, end_ycor, 300)
                continue

        self.get_pending_call_drp().click()
        time.sleep(2)

        ag_visit = int(self.get_agreed_visit_drp().text)
        call_later = int(self.get_remind_call_drp().text)
        remove_li = int(self.get_removed_list_drp().text)

        empty_list.insert(0, ag_visit)
        empty_list.insert(1, call_later)
        empty_list.insert(2, remove_li)

        time.sleep(2)
        self.get_pending_call_drp().click()

    def click_call_btn_one(self):
        self.get_call_btn().click()

    def click_agreed_visit_rad_btn(self):
        self.get_agreed_visit_rad_btn().click()

    def click_call_later_rad_btn(self):
        self.get_call_later_rad_btn().click()

    def click_overdue_list_rad_btn(self):
        self.get_overdue_list_rad_btn().click()

    def click_pending_call_drp(self):
        self.get_pending_call_drp().click()

    def click_agreed_visit_drp(self):
        self.get_agreed_visit_drp().click()

    def click_remind_call_drp(self):
        self.get_remind_call_drp().click()

    def click_removed_list_drp(self):
        self.get_removed_list_drp().click()

    def click_no_visit_drp(self):
        self.get_no_visit_drp().click()

        no_visit = self.get_no_visit_drp()
        value = int(no_visit.text)
        print(value)
        assert value != 0, 'No visit is empty'
        print('Success')

    def verif_agreed_visit_drp(self):
        agreed_visit = self.get_agreed_visit_drp()
        value = int(agreed_visit.text)
        assert value == empty_list[0] + 1, 'Not Added'
        print('Success')

    def click_pending_call_drp_remind(self):
        self.get_pending_call_drp().click()
        self.get_call_btn().click()
        self.get_call_later_rad_btn().click()
        self.get_done_btn_call_later().click()
        self.get_pending_call_drp().click()

    def verif_remind_call_drp(self):
        remind_call = self.get_remind_call_drp()
        value = int(remind_call.text)
        assert value == empty_list[1] + 1, 'Not Added'
        print('Success')

    def click_reason_rad_btn(self):
        self.get_reason_rad_btn().click()

    def click_done_btn(self):
        self.get_done_btn().click()
        self.get_pending_call_drp().click()

        remove_list = self.get_removed_list_drp()
        value = int(remove_list.text)
        print(value)
        assert value == empty_list[2] + 1, 'Not Added'
        print('Success')

    def click_pending_call_drp_remove(self):
        self.get_pending_call_drp().click()
        self.get_call_btn().click()
        self.get_overdue_list_rad_btn().click()



