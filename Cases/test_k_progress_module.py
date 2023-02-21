import base64
import os
import time
import pytest

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
from Utilities.data import details, medical_data

# Patient page
from Pages.patient_page import PatientPage

generator = RandomNumberGenerator()
name_generator = NameGenerator()
doc_creator = DocumentCreator()


@pytest.mark.usefixtures('setup')
class TestProgressModule():

    def test_registration_followup_daily(self):
        # Check Daily Option of Registration and Followups

        prog_reg_daily = ProgDaily(self.driver, self.wait)
        prog_reg_daily.click_progress_tab()
        prog_reg_daily.click_daily_btn()
        prog_reg_daily.click_daily_period_drp()
        prog_reg_daily.click_daily_date_rad_btn()
        prog_reg_daily.verif_daily()
        prog_reg_daily.click_back_btn()

    def test_registration_followup_monthly(self):
        # Check Monthly Option of Registration and Followups

        prog_reg_monthly = ProgMonthly(self.driver, self.wait)
        prog_reg_monthly.click_monthly_btn()
        prog_reg_monthly.click_monthly_period_drp()
        prog_reg_monthly.click_monthly_date_rad_btn()
        prog_reg_monthly.verif_monthly()
        prog_reg_monthly.click_back_btn()

    def test_registration_followup_yearly(self):
        # Check Yearly Option of Registration and Followups

        prog_reg_yearly = ProgYearly(self.driver, self.wait)
        prog_reg_yearly.click_yearly_btn()
        prog_reg_yearly.click_yearly_period_drp()
        prog_reg_yearly.click_yearly_date_rad_btn()
        prog_reg_yearly.verif_yearly()
        prog_reg_yearly.click_back_btn()

    def test_check_reports(self):
        # Check Reports

        reports_hyper = ReportsHyper(self.driver, self.wait)
        reports_hyper.click_hyper_btn()
        reports_hyper.verif_hyper_page()
        reports_hyper.click_back_btn()



