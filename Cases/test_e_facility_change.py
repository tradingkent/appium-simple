import base64
import os
import time
import pytest

from Pages.change_facility_page import ChangeFac
from Pages.landing_page import LandingPage
from Pages.medical_details_page import MedDetails
from Pages.new_medicine_page import NewMedicine
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
class TestFacChange():

    def test_facility_change(self):
        # Switch to a different facility (Medical Facilitator)

        change_fac = ChangeFac(self.driver, self.wait)
        change_fac.click_fac_sel_btn()
        change_fac.click_new_fac()
        change_fac.click_yes_btn()

