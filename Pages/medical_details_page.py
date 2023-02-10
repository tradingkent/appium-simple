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
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif


class MedDetails(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    medicine_btn = (By.ID, "org.simple.clinic.staging:id/updateButton")
    bp_btn = (By.ID, "org.simple.clinic.staging:id/addNewBP")
    diabetes_btn = (By.ID, "org.simple.clinic.staging:id/addNewBloodSugar")
    teleconsult_btn = (By.ID, "org.simple.clinic.staging:id/teleconsultButton")
    save_btn = (By.ID, "org.simple.clinic.staging:id/doneButton")
    done_btn = (By.ID, "org.simple.clinic.staging:id/doneButton")

    # After click medecine
    medicine_list = (By.XPATH, "//android.widget.LinearLayout/android.widget.CheckBox")
    save_btn_add_drug = (By.ID, "org.simple.clinic.staging:id/prescribeddrugs_done")

    med_amlo = (By.XPATH, "//android.widget.CheckBox[@text='Amlodipine']")
    med_ateno = (By.XPATH, "//android.widget.CheckBox[@text='Atenolol']")
    med_chlor = (By.XPATH, "//android.widget.CheckBox[@text='Chlorthalidone']")

    dos_med_amlo = (By.XPATH, "//android.widget.TextView[@text='5 mg BD']")
    dos_med_ateno = (By.XPATH, "//android.widget.TextView[@text='50 mg BID']")
    dos_med_chlor = (By.XPATH, "//android.widget.TextView[@text='12.5 mg']")

    # After click of BP
    systolic_field = (By.ID, "org.simple.clinic.staging:id/systolicEditText")
    diastolic_field = (By.ID, "org.simple.clinic.staging:id/diastolicEditText")
    change_btn = (By.ID, "org.simple.clinic.staging:id/changeDateButton")

    bp_day_field = (By.ID, "org.simple.clinic.staging:id/dayEditText")
    bp_month_field = (By.ID, "org.simple.clinic.staging:id/monthEditText")
    bp_year_field = (By.ID, "org.simple.clinic.staging:id/yearEditText")

    # After click of Diabetes
    rbs_option = (By.XPATH, "//android.view.ViewGroup/android.widget.TextView[@text='Random blood sugar (RBS)']")
    rbs_field = (By.ID, "org.simple.clinic.staging:id/bloodSugarReadingEditText")

    # Counter Verif

    sched_date = (By.ID, "org.simple.clinic.staging:id/currentDateTextView")
    sched_minus = (By.ID, "org.simple.clinic.staging:id/decrementDateButton")
    sched_add = (By.ID, "org.simple.clinic.staging:id/incrementDateButton")

    # Verif
    meds_selected_verif = (By.XPATH, "//android.widget.TextView[@index='1']")
    bp_result_verif = (By.ID, "org.simple.clinic.staging:id/readingsTextView")
    bp_visit_date_verif = (By.ID, "org.simple.clinic.staging:id/dateTimeTextView")
    blood_sugar_verif = (By.XPATH, "//android.widget.TextView[@resource-id='org.simple.clinic.staging:id/itemName']")
    diabetes_verif = (By.ID, "org.simple.clinic.staging:id/readingTextView")
    landing_verif = (By.XPATH, "//android.widget.TextView[@text='PATIENTS']")

    ##Elements##

    def get_medicine_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.medicine_btn))

    def get_bp_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.bp_btn))

    def get_diabetes_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.diabetes_btn))

    def get_teleconsult_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.teleconsult_btn))

    def get_save_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_btn))

    def get_done_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.done_btn))

    # After click medecine

    def get_medicine_list(self):
        return self.driver.find_elements(*self.medicine_list)

    def get_save_btn_add_drug(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_btn_add_drug))

    def get_med_amlo(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_amlo))

    def get_med_ateno(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_ateno))

    def get_med_chlor(self):
        return self.wait.until(EC.element_to_be_clickable(self.med_chlor))

    def get_dos_med_amlo(self):
        return self.wait.until(EC.element_to_be_clickable(self.dos_med_amlo))

    def get_dos_med_ateno(self):
        return self.wait.until(EC.element_to_be_clickable(self.dos_med_ateno))

    def get_dos_med_chlor(self):
        return self.wait.until(EC.element_to_be_clickable(self.dos_med_chlor))

    # After click of BP

    def get_systolic_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.systolic_field))

    def get_diastolic_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.diastolic_field))

    def get_change_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.change_btn))

    def get_bp_day_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.bp_day_field))

    # After click of Diabetes

    def get_rbs_option(self):
        return self.wait.until(EC.element_to_be_clickable(self.rbs_option))

    def get_rbs_field(self):
        return self.wait.until(EC.element_to_be_clickable(self.rbs_field))

    # Verif

    def get_meds_selected_verif(self):
        return self.driver.find_elements(*self.meds_selected_verif)

    def get_bp_result_verif(self):
        return self.driver.find_element(*self.bp_result_verif)

    def get_bp_visit_date_verif(self):
        return self.driver.find_element(*self.bp_visit_date_verif)

    def get_blood_sugar_verif(self):
        return self.driver.find_elements(*self.blood_sugar_verif)

    def get_diabetes_verif(self):
        return self.driver.find_element(*self.diabetes_verif)

    def get_landing_verif(self):
        return self.wait.until(EC.element_to_be_clickable(self.landing_verif))

    # Counter Verif

    def get_sched_date(self):
        return self.wait.until(EC.element_to_be_clickable(self.sched_date))

    def get_sched_minus(self):
        return self.wait.until(EC.element_to_be_clickable(self.sched_minus))

    def get_sched_add(self):
        return self.wait.until(EC.element_to_be_clickable(self.sched_add))

    ##Methods##

    def click_medicine_btn(self):
        self.get_medicine_btn().click()
        self.cap_screenshot('4', '1')
        time.sleep(2)
        self.driver.swipe(518, 1254, 507, 1196, 300)

        med_list = self.get_medicine_list()
        emp_med_list = []
        for meds in med_list:
            emp_med_list.append(meds.text)

        assert emp_med_list == med_list_verif, 'Medicine List is not the same'
        print(emp_med_list)
        print(med_list_verif)

    def click_choose_meds(self):
        self.get_med_amlo().click()
        self.get_dos_med_amlo().click()
        self.get_med_ateno().click()
        self.get_dos_med_ateno().click()
        self.get_med_chlor().click()
        self.get_dos_med_chlor().click()

        self.cap_screenshot('4', '2')

    def click_bp_btn(self):
        self.get_bp_btn().click()

    def click_diabetes_btn(self):
        self.get_diabetes_btn().click()
        time.sleep(2)

        blood_sugar_list = self.get_blood_sugar_verif()
        emp_blood_sugar = []
        for blood_sugar in blood_sugar_list:
            emp_blood_sugar.append(blood_sugar.text)

        assert emp_blood_sugar == blood_sugars_verif, 'Blood Sugar Category not the same'
        print(emp_blood_sugar)
        print(blood_sugars_verif)
        print('Success: Blood Sugar Category')

    def click_teleconsult_btn(self):
        self.get_teleconsult_btn().click()

    def click_done_btn(self):
        self.get_done_btn().click()
        time.sleep(2)

        home_page = self.get_landing_verif()
        assert home_page.text == verif.get('lan_to_home_verif'), 'Failed to proceed to Homepage'
        print('Success Add Medical Details')

    def click_save_btn(self):
        self.get_save_btn().click()
        time.sleep(2)

        number_of_days = self.get_sched_date()
        number_of_days_sliced = number_of_days.text[0:2]
        number_of_days_cast = int(number_of_days_sliced)

        click = 3
        for i in range(click):
            self.get_sched_minus().click()

        num_of_days_minus = self.get_sched_date()
        num_of_days_minus_sliced = num_of_days_minus.text[0:2]
        num_of_days_minus_cast = int(num_of_days_minus_sliced)

        total = number_of_days_cast - click
        print(total)
        print(num_of_days_minus_cast)

        assert total == num_of_days_minus_cast, 'Minus counter calculation is wrong'
        print('Success Minus Counter check')

        for i in range(click):
            self.get_sched_add().click()

        num_of_days_add = self.get_sched_date()
        num_of_days_add_sliced = num_of_days_add.text[0:2]
        num_of_days_add_cast = int(num_of_days_add_sliced)

        print(number_of_days_cast)
        print(num_of_days_add_cast)

        assert number_of_days_cast == num_of_days_add_cast, 'Add counter calculation is wrong'
        print('Success Add Counter check')

    def click_medicine_list(self):
        self.get_medicine_list().click()

    def click_save_btn_add_drug(self):
        self.get_save_btn_add_drug().click()
        self.cap_screenshot('4', '3')
        time.sleep(2)

        med_check_verif = self.get_meds_selected_verif()
        emp_meds_verif = []
        for meds_verif in med_check_verif:
            emp_meds_verif.append(meds_verif.text)
        emp_meds_verif.pop(0)
        assert emp_meds_verif == meds_check_verif, 'Selected Medicine is not located'
        print(emp_meds_verif)
        print(meds_check_verif)
        self.cap_screenshot('4', '4')

    # Add BP
    def enter_systolic_field(self, systolic):
        self.get_systolic_field().send_keys(systolic)

    def enter_diastolic_field(self, diastolic):
        self.get_diastolic_field().send_keys(diastolic)

    def click_change_btn(self):
        self.get_change_btn().click()

    def click_bp_day_field(self, day):
        self.get_bp_day_field().click()
        self.driver.press_keycode(22)  # right arrow

        for i in range(2):
            self.driver.press_keycode(67)  # backspace

        self.get_bp_day_field().send_keys(day)
        user_action = TouchAction(self.driver)
        user_action.tap(x=928, y=2051).perform()

        time.sleep(2)

        bp_result = self.get_bp_result_verif()
        bp_date_visit = self.get_bp_visit_date_verif()
        assert bp_result.text == medical_data.get('bp_res'), 'Blood Pressure Readings not reflected'
        print('Success: Blood Pressure readings reflected')
        assert bp_date_visit.text == medical_data.get('bp_date_visit'), 'Visit date not reflected'
        print('Success: Visit date reflected')

    # Diabetes

    def click_rbs_option(self):
        self.get_rbs_option().click()

    def enter_rbs_field(self, rbs):
        time.sleep(2)
        self.get_rbs_field().send_keys(rbs)
        time.sleep(2)

        user_action = TouchAction(self.driver)
        user_action.tap(x=928, y=2051).perform()

        diabetes_result = self.get_diabetes_verif()
        assert diabetes_result.text == medical_data.get('diabetes_verif'), 'Blood Sugar not reflected'
        print('Success: Blood Sugar reflected')
