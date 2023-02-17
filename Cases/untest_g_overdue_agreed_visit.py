import base64
import os
import time
import pytest

from Pages.change_facility_page import ChangeFac
from Pages.landing_page import LandingPage
from Pages.medical_details_page import MedDetails
from Pages.new_medicine_page import NewMedicine
from Pages.overdue_page import OverdueDetails
from Pages.removal_page import RemDetails
from Utilities.common import RandomNumberGenerator, DocumentCreator
from Utilities.common import NameGenerator
from Utilities.data import details, medical_data

# Patient page
from Pages.patient_page import PatientPage

generator = RandomNumberGenerator()
name_generator = NameGenerator()
doc_creator = DocumentCreator()


@pytest.mark.usefixtures('setup')
class TestOverdueAgreed():

    def test_overdue_agreed_visit(self):
        # Add new patient under AGREED TO VISIT

        overdue_details = OverdueDetails(self.driver, self.wait)
        overdue_details.scroll_up()
        overdue_details.click_call_btn_one()
        overdue_details.click_agreed_visit_rad_btn()
        overdue_details.click_pending_call_drp()
        overdue_details.verif_agreed_visit_drp()











    '''
    def test_overdue_remind_call(self):
        # Add new patient under REMIND TO CALL LATER

        overdue_details = OverdueDetails(self.driver, self.wait)
        overdue_details.click_pending_call_drp_remind()
        overdue_details.verif_remind_call_drp()

    def test_overdue_removed_list(self):
        # Add new patient under REMOVED FROM LIST

        overdue_details = OverdueDetails(self.driver, self.wait)
        overdue_details.click_pending_call_drp_remove()
        overdue_details.click_reason_rad_btn()
        overdue_details.click_done_btn()

    def test_overdue_no_visit(self):
        # Overdue tab validation of patients no visit

        overdue_details = OverdueDetails(self.driver, self.wait)
        overdue_details.click_no_visit_drp()

    '''





