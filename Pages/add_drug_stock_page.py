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
    med_list_verif, meds_check_verif, medical_data, blood_sugars_verif, removal_verif, progress_date_sel, \
    progress_drug_date_sel, progress_drug_num


lg = LogFunc()
logger = lg.get_log()

class AddDrugStock(BaseDriver):

    def __init__(self, driver, wait):  # driver,
        super().__init__(driver)
        self.driver = driver
        self.wait = wait

    ##Locators##

    patient_tab = (By.XPATH, "//android.widget.TextView[@text='PATIENTS']")
    progress_tab = (By.XPATH, "//android.widget.TextView[@text='PROGRESS']")
    sync_btn = (By.ID, "org.simple.clinic.staging:id/statusImageView")
    back_btn = (By.XPATH, "//android.view.View[@text='Go back to progress']")
    toggle_btn = (By.XPATH, "//android.view.View[@index='38']")
    save_btn = (By.XPATH, "//android.widget.Button[@text='SAVE']")
    done_btn = (By.XPATH, "//android.view.View[@index='0']")

    enter_drug_stock_btn = (By.XPATH, "//android.view.View[@text='ENTER DRUG STOCK']")
    end_month_drp = (By.XPATH, "//android.widget.Spinner[@index='1']")
    month_rad_btn = (By.XPATH, f"//android.widget.CheckedTextView[@text='{progress_drug_date_sel.get('month')}']")

    # 522,1678, 507, 1008

    # Drugs field
    drug_zero_received = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_0__received']")
    drug_one_received = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_1__received']")
    drug_two_received = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_2__received']")
    drug_three_received = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_3__received']")
    drug_four_received = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_4__received']")
    drug_five_received = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_5__received']")
    drug_six_received = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_6__received']")

    drug_zero_stock = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_0__in_stock']")
    drug_one_stock = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_1__in_stock']")
    drug_two_stock = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_2__in_stock']")
    drug_three_stock = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_3__in_stock']")
    drug_four_stock = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_4__in_stock']")
    drug_five_stock = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_5__in_stock']")
    drug_six_stock = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_6__in_stock']")

    drug_zero_redis = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_0__redistributed']")
    drug_one_redis = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_1__redistributed']")
    drug_two_redis = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_2__redistributed']")
    drug_three_redis = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_3__redistributed']")
    drug_four_redis = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_4__redistributed']")
    drug_five_redis = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_5__redistributed']")
    drug_six_redis = (By.XPATH, "//android.widget.EditText[@resource-id='_drug_stocks_6__redistributed']")

    # Verif
    verif_complete = (By.XPATH, "//android.view.View[@text='Complete!']")
    verif_drug_five_stock = (By.XPATH, "//android.view.View[@index='7']")
    verif_drug_six_stock = (By.XPATH, "//android.view.View[@index='9']")
    verif_drug_zero_stock = (By.XPATH, "//android.view.View[@index='13']")
    verif_drug_one_stock = (By.XPATH, "//android.view.View[@index='15']")
    verif_drug_three_stock = (By.XPATH, "//android.view.View[@index='19']")
    verif_drug_four_stock = (By.XPATH, "//android.view.View[@index='21']")
    verif_drug_two_stock = (By.XPATH, "//android.view.View[@index='25']")

    verif_drug_prog_five_stock = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                            "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                            ".FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget"
                                            ".ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget"
                                            ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                            "android.webkit.WebView/android.webkit.WebView/android.view.View[6]")
    verif_drug_prog_six_stock = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                           "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                           ".FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget"
                                           ".ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget"
                                           ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                           "android.webkit.WebView/android.webkit.WebView/android.view.View[8]")
    verif_drug_prog_zero_stock = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                            "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                            ".FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget"
                                            ".ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget"
                                            ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                            "android.webkit.WebView/android.webkit.WebView/android.view.View[12]")
    verif_drug_prog_one_stock = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                           "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                           ".FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget"
                                           ".ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget"
                                           ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                           "android.webkit.WebView/android.webkit.WebView/android.view.View[14]")
    verif_drug_prog_three_stock = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                             "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                             ".FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget"
                                             ".ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget"
                                             ".FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                             "android.webkit.WebView/android.webkit.WebView/android.view.View[18]")
    verif_drug_prog_four_stock = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                            "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                            ".FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget"
                                            ".ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget."
                                            "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                            "android.webkit.WebView/android.webkit.WebView/android.view.View[20]")
    verif_drug_prog_two_stock = (By.XPATH, "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/"
                                           "android.widget.FrameLayout/android.widget.LinearLayout/android.widget"
                                           ".FrameLayout/android.widget.RelativeLayout/androidx.viewpager.widget"
                                           ".ViewPager/androidx.recyclerview.widget.RecyclerView/android.widget."
                                           "FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/"
                                           "android.webkit.WebView/android.webkit.WebView/android.view.View[23]")

    ##Elements##

    def get_patient_tab(self):
        return self.wait.until(EC.element_to_be_clickable(self.patient_tab))

    def get_progress_tab(self):
        return self.wait.until(EC.element_to_be_clickable(self.progress_tab))

    def get_sync_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.sync_btn))

    def get_back_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.back_btn))

    def get_toggle_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.toggle_btn))

    def get_save_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.save_btn))

    def get_done_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.done_btn))

    def get_enter_drug_stock_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.enter_drug_stock_btn))

    def get_end_month_drp(self):
        return self.wait.until(EC.element_to_be_clickable(self.end_month_drp))

    def get_month_rad_btn(self):
        return self.wait.until(EC.element_to_be_clickable(self.month_rad_btn))

    # Drugs field

    def get_drug_zero_received(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_zero_received))

    def get_drug_one_received(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_one_received))

    def get_drug_two_received(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_two_received))

    def get_drug_three_received(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_three_received))

    def get_drug_four_received(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_four_received))

    def get_drug_five_received(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_five_received))

    def get_drug_six_received(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_six_received))

    ###

    def get_drug_zero_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_zero_stock))

    def get_drug_one_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_one_stock))

    def get_drug_two_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_two_stock))

    def get_drug_three_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_three_stock))

    def get_drug_four_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_four_stock))

    def get_drug_five_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_five_stock))

    def get_drug_six_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_six_stock))

    ####

    def get_drug_zero_redis(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_zero_redis))

    def get_drug_one_redis(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_one_redis))

    def get_drug_two_redis(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_two_redis))

    def get_drug_three_redis(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_three_redis))

    def get_drug_four_redis(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_four_redis))

    def get_drug_five_redis(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_five_redis))

    def get_drug_six_redis(self):
        return self.wait.until(EC.element_to_be_clickable(self.drug_six_redis))

    # Verif

    def get_verif_complete(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_complete))

    def get_verif_drug_five_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_five_stock))

    def get_verif_drug_six_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_six_stock))

    def get_verif_drug_zero_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_zero_stock))

    def get_verif_drug_one_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_one_stock))

    def get_verif_drug_three_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_three_stock))

    def get_verif_drug_four_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_four_stock))

    def get_verif_drug_two_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_two_stock))

    def get_verif_drug_prog_five_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_prog_five_stock))

    def get_verif_drug_prog_six_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_prog_six_stock))

    def get_verif_drug_prog_zero_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_prog_zero_stock))

    def get_verif_drug_prog_one_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_prog_one_stock))

    def get_verif_drug_prog_three_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_prog_three_stock))

    def get_verif_drug_prog_four_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_prog_four_stock))

    def get_verif_drug_prog_two_stock(self):
        return self.wait.until(EC.element_to_be_clickable(self.verif_drug_prog_two_stock))

    ##Methods##

    def click_patient_tab(self):
        self.get_patient_tab().click()

    def click_progress_tab(self):
        self.get_progress_tab().click()

    def click_sync_btn(self):
        self.get_sync_btn().click()

    def click_back_btn(self):
        self.get_back_btn().click()

    def click_toggle_btn(self):
        for i in range(2):
            self.get_toggle_btn().click()

    def click_save_btn(self):
        self.get_save_btn().click()

    def click_done_btn(self):
        time.sleep(2)
        complete_verif = self.get_verif_complete()
        assert complete_verif.text == 'Complete!', 'Add Drug Stock not complete!'
        for i in range(2):
            self.driver.swipe(522, 1678, 507, 1008, 300)
        ver_drug_five_stock = self.get_verif_drug_five_stock()
        ver_drug_six_stock = self.get_verif_drug_six_stock()
        ver_drug_zero_stock = self.get_verif_drug_zero_stock()
        ver_drug_one_stock = self.get_verif_drug_one_stock()
        ver_drug_three_stock = self.get_verif_drug_three_stock()
        ver_drug_four_stock = self.get_verif_drug_four_stock()
        ver_drug_two_stock = self.get_verif_drug_two_stock()
        ver_drug_five_stock_sliced = int(ver_drug_five_stock.text[0:1])
        ver_drug_six_stock_sliced = int(ver_drug_six_stock.text[0:1])
        ver_drug_zero_stock_sliced = int(ver_drug_zero_stock.text[0:1])
        ver_drug_one_stock_sliced = int(ver_drug_one_stock.text[0:1])
        ver_drug_three_stock_sliced = int(ver_drug_three_stock.text[0:1])
        ver_drug_four_stock_sliced = int(ver_drug_four_stock.text[0:1])
        ver_drug_two_stock_sliced = int(ver_drug_two_stock.text[0:1])

        assert ver_drug_five_stock_sliced == int(progress_drug_num.get('five_stock')), 'Drug not reflected'
        assert ver_drug_six_stock_sliced == int(progress_drug_num.get('six_stock')), 'Drug not reflected'
        assert ver_drug_zero_stock_sliced == int(progress_drug_num.get('zero_stock')), 'Drug not reflected'
        assert ver_drug_one_stock_sliced == int(progress_drug_num.get('one_stock')), 'Drug not reflected'
        assert ver_drug_three_stock_sliced == int(progress_drug_num.get('three_stock')), 'Drug not reflected'
        assert ver_drug_four_stock_sliced == int(progress_drug_num.get('four_stock')), 'Drug not reflected'
        assert ver_drug_two_stock_sliced == int(progress_drug_num.get('two_stock')), 'Drug not reflected'

        logger.info('Success Drug Report')
        time.sleep(2)
        self.get_done_btn().click()

    def click_enter_drug_stock_btn(self):
        self.get_enter_drug_stock_btn().click()

    def click_end_month_drp(self):
        self.get_end_month_drp().click()

    def click_month_rad_btn(self):
        time.sleep(2)
        for i in range(5):
            end_ycor = 1008
            try:
                value = self.get_month_rad_btn().is_displayed()
                if value is True:
                    break
            except:
                # 522, 1678, 507, 1008
                self.driver.swipe(522, 1678, 507, end_ycor, 300)
                continue

        self.get_month_rad_btn().click()

    def enter_initial_drugs(self, zero_rec, one_rec, two_rec, three_rec, four_rec, five_rec, six_rec,
                            zero_stock, one_stock, two_stock, three_stock, four_stock, five_stock, six_stock):
        time.sleep(2)
        self.driver.swipe(522, 1678, 507, 1008, 300)

        self.get_drug_zero_received().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_zero_received().send_keys(zero_rec)
        self.get_drug_zero_stock().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_zero_stock().send_keys(zero_stock)
        self.get_drug_one_received().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_one_received().send_keys(one_rec)
        self.get_drug_one_stock().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_one_stock().send_keys(one_stock)
        self.get_drug_two_received().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_two_received().send_keys(two_rec)
        self.get_drug_two_stock().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_two_stock().send_keys(two_stock)
        self.driver.swipe(522, 1678, 507, 1008, 300)
        self.get_drug_three_received().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_three_received().send_keys(three_rec)
        self.get_drug_three_stock().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_three_stock().send_keys(three_stock)
        self.get_drug_four_received().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_four_received().send_keys(four_rec)
        self.get_drug_four_stock().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_four_stock().send_keys(four_stock)
        self.driver.swipe(522, 1678, 507, 1008, 300)
        self.get_drug_five_received().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_five_received().send_keys(five_rec)
        self.get_drug_five_stock().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_five_stock().send_keys(five_stock)
        self.get_drug_six_received().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_six_received().send_keys(six_rec)
        self.get_drug_six_stock().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_six_stock().send_keys(six_stock)

    def enter_addtnl_drugs(self, zero_redis, one_redis, two_redis,
                           three_redis, four_redis, five_redis, six_redis):
        time.sleep(2)
        self.driver.swipe(522, 1678, 507, 1008, 300)

        self.get_drug_zero_redis().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_zero_redis().send_keys(zero_redis)
        self.get_drug_one_redis().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_one_redis().send_keys(one_redis)
        self.driver.swipe(522, 1678, 507, 1008, 300)
        self.get_drug_two_redis().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_two_redis().send_keys(two_redis)
        self.get_drug_three_redis().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_three_redis().send_keys(three_redis)
        self.get_drug_four_redis().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_four_redis().send_keys(four_redis)
        self.driver.swipe(522, 1678, 507, 1008, 300)
        self.get_drug_five_redis().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_five_redis().send_keys(five_redis)
        self.get_drug_six_redis().send_keys(Keys.BACKSPACE * 5)
        self.get_drug_six_redis().send_keys(six_redis)

    def click_refresh(self):
        self.get_patient_tab().click()
        self.get_sync_btn().click()
        time.sleep(3)
        self.get_progress_tab().click()

    def verif_drug_report_progress_tab(self):
        time.sleep(2)
        for i in range(5):
            self.driver.swipe(522, 1678, 507, 1008, 300)

        ver_drug_five_stock = self.get_verif_drug_prog_five_stock()
        ver_drug_six_stock = self.get_verif_drug_prog_six_stock()
        ver_drug_zero_stock = self.get_verif_drug_prog_zero_stock()
        ver_drug_one_stock = self.get_verif_drug_prog_one_stock()
        ver_drug_three_stock = self.get_verif_drug_prog_three_stock()
        ver_drug_four_stock = self.get_verif_drug_prog_four_stock()
        ver_drug_two_stock = self.get_verif_drug_prog_two_stock()

        ver_drug_five_stock_sliced = int(ver_drug_five_stock.text[0:1])
        ver_drug_six_stock_sliced = int(ver_drug_six_stock.text[0:1])
        ver_drug_zero_stock_sliced = int(ver_drug_zero_stock.text[0:1])
        ver_drug_one_stock_sliced = int(ver_drug_one_stock.text[0:1])
        ver_drug_three_stock_sliced = int(ver_drug_three_stock.text[0:1])
        ver_drug_four_stock_sliced = int(ver_drug_four_stock.text[0:1])
        ver_drug_two_stock_sliced = int(ver_drug_two_stock.text[0:1])

        assert ver_drug_five_stock_sliced == int(progress_drug_num.get('five_stock')), 'Drug not reflected'
        assert ver_drug_six_stock_sliced == int(progress_drug_num.get('six_stock')), 'Drug not reflected'
        assert ver_drug_zero_stock_sliced == int(progress_drug_num.get('zero_stock')), 'Drug not reflected'
        assert ver_drug_one_stock_sliced == int(progress_drug_num.get('one_stock')), 'Drug not reflected'
        assert ver_drug_three_stock_sliced == int(progress_drug_num.get('three_stock')), 'Drug not reflected'
        assert ver_drug_four_stock_sliced == int(progress_drug_num.get('four_stock')), 'Drug not reflected'
        assert ver_drug_two_stock_sliced == int(progress_drug_num.get('two_stock')), 'Drug not reflected'

        logger.info('Success Drug Report in Progress Page')
