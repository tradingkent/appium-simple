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
class TestOverdueRemove():

    @pytest.mark.tags('All', 'TC18')
    def test_overdue_removed_list(self):
        # Add new patient under REMOVED FROM LIST

        overdue_details = OverdueDetails(self.driver, self.wait)
        overdue_details.click_pending_call_drp_remove()
        overdue_details.click_reason_rad_btn()
        overdue_details.click_done_btn()






