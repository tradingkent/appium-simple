import base64
import os
import time
import pytest

from Pages.add_drug_stock_page import AddDrugStock
from Pages.change_facility_page import ChangeFac
from Pages.landing_page import LandingPage
from Pages.medical_details_page import MedDetails
from Pages.new_medicine_page import NewMedicine
from Pages.overdue_page import OverdueDetails
from Pages.progress_daily_page import ProgDaily
from Pages.progress_monthly_page import ProgMonthly
from Pages.progress_yearly_page import ProgYearly
from Pages.removal_page import RemDetails
from Pages.reports_page import ReportsHyper
from Utilities.common import RandomNumberGenerator, DocumentCreator
from Utilities.common import NameGenerator
from Utilities.data import details, medical_data, progress_drug_num

# Patient page
from Pages.patient_page import PatientPage

generator = RandomNumberGenerator()
name_generator = NameGenerator()
doc_creator = DocumentCreator()


@pytest.mark.usefixtures('setup')
class TestProgressModule():

    @pytest.mark.tags('All', 'TC20')
    def test_registration_followup_daily(self):
        # Check Daily Option of Registration and Followups

        prog_reg_daily = ProgDaily(self.driver, self.wait)
        prog_reg_daily.click_progress_tab()
        prog_reg_daily.click_daily_btn()
        prog_reg_daily.click_daily_period_drp()
        prog_reg_daily.click_daily_date_rad_btn()
        prog_reg_daily.verif_daily()
        prog_reg_daily.click_back_btn()

    @pytest.mark.tags('All', 'TC21')
    def test_registration_followup_monthly(self):
        # Check Monthly Option of Registration and Followups

        prog_reg_monthly = ProgMonthly(self.driver, self.wait)
        prog_reg_monthly.click_monthly_btn()
        prog_reg_monthly.click_monthly_period_drp()
        prog_reg_monthly.click_monthly_date_rad_btn()
        prog_reg_monthly.verif_monthly()
        prog_reg_monthly.click_back_btn()

    @pytest.mark.tags('All', 'TC22')
    def test_registration_followup_yearly(self):
        # Check Yearly Option of Registration and Followups

        prog_reg_yearly = ProgYearly(self.driver, self.wait)
        prog_reg_yearly.click_yearly_btn()
        prog_reg_yearly.click_yearly_period_drp()
        prog_reg_yearly.click_yearly_date_rad_btn()
        prog_reg_yearly.verif_yearly()
        prog_reg_yearly.click_back_btn()

    @pytest.mark.tags('All', 'TC23')
    def test_check_reports(self):
        # Check Reports

        reports_hyper = ReportsHyper(self.driver, self.wait)
        reports_hyper.click_hyper_btn()
        reports_hyper.verif_hyper_page()
        reports_hyper.click_back_btn()

    @pytest.mark.tags('All', 'TC24')
    def test_drug_stock_report(self):
        # Add drug stock under Drug stock report

        add_drug_stock = AddDrugStock(self.driver, self.wait)
        add_drug_stock.click_enter_drug_stock_btn()
        add_drug_stock.click_end_month_drp()
        add_drug_stock.click_month_rad_btn()
        add_drug_stock.enter_initial_drugs(progress_drug_num.get('zero_received'),
                                           progress_drug_num.get('one_received'),
                                           progress_drug_num.get('two_received'),
                                           progress_drug_num.get('three_received'),
                                           progress_drug_num.get('four_received'),
                                           progress_drug_num.get('five_received'),
                                           progress_drug_num.get('six_received'),
                                           progress_drug_num.get('zero_stock'),
                                           progress_drug_num.get('one_stock'),
                                           progress_drug_num.get('two_stock'),
                                           progress_drug_num.get('three_stock'),
                                           progress_drug_num.get('four_stock'),
                                           progress_drug_num.get('five_stock'),
                                           progress_drug_num.get('six_stock'))
        add_drug_stock.click_toggle_btn()
        add_drug_stock.enter_addtnl_drugs(progress_drug_num.get('zero_redis'),
                                          progress_drug_num.get('one_redis'),
                                          progress_drug_num.get('two_redis'),
                                          progress_drug_num.get('three_redis'),
                                          progress_drug_num.get('four_redis'),
                                          progress_drug_num.get('five_redis'),
                                          progress_drug_num.get('six_redis'))
        add_drug_stock.click_save_btn()
        add_drug_stock.click_done_btn()
        add_drug_stock.click_refresh()
        add_drug_stock.verif_drug_report_progress_tab()






