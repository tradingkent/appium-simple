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
class TestOverdueNoVisit():

    @pytest.mark.tags('All', 'TC19')
    def test_overdue_no_visit(self):
        # Overdue tab validation of patients no visit

        overdue_details = OverdueDetails(self.driver, self.wait)
        overdue_details.click_no_visit_drp()






