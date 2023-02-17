import base64
import os
import time
import pytest

from Pages.landing_page import LandingPage
from Pages.medical_details_page import MedDetails
from Pages.modify_patient_page import ModDetails
from Pages.new_medicine_page import NewMedicine
from Pages.removal_page import RemDetails
from Utilities.common import RandomNumberGenerator, DocumentCreator
from Utilities.common import NameGenerator
from Utilities.data import details, medical_data, new_details_edit

# Patient page
from Pages.patient_page import PatientPage

generator = RandomNumberGenerator()
name_generator = NameGenerator()
doc_creator = DocumentCreator()


@pytest.mark.usefixtures('setup')
class TestModDetails():

    def test_update_pat_profile(self):
        # Update of Patient  profile

        mod_details = ModDetails(self.driver, self.wait)
        mod_details.click_edit_patient_btn()
        mod_details.click_edit_phone_number(new_details_edit.get('number'))
        mod_details.click_edit_age(new_details_edit.get('age'))
        mod_details.click_female_rad_btn()
        mod_details.click_edit_address(new_details_edit.get('address'))
        mod_details.click_edit_village(new_details_edit.get('village'))
        mod_details.click_save_edit()

    def test_delete_pat_profile(self):
        # Deletion of Patient profile

        mod_details = ModDetails(self.driver, self.wait)
        mod_details.click_edit_del_patient_btn()
        mod_details.click_del_patient()
        mod_details.click_reason_duplicate_rad()
        mod_details.click_prompt_del()
        mod_details.click_search_add_patient()
        mod_details.enter_search_patient_box(name_generator.names[0])






