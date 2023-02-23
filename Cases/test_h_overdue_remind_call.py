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
class TestOverdueRemind():

    @pytest.mark.tags('All', 'TC17')
    def test_overdue_remind_call(self):
        # Add new patient under REMIND TO CALL LATER

        overdue_details = OverdueDetails(self.driver, self.wait)
        overdue_details.click_pending_call_drp_remind()
        overdue_details.verif_remind_call_drp()






