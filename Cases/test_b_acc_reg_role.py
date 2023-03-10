import base64
import os
import time
import pytest

from Pages.landing_page import LandingPage
from Utilities.common import RandomNumberGenerator, DocumentCreator
from Utilities.common import NameGenerator
from Utilities.data import details

# Patient page
from Pages.patient_page import PatientPage

generator = RandomNumberGenerator()
name_generator = NameGenerator()
doc_creator = DocumentCreator()


@pytest.mark.usefixtures('setup')
class TestAccReg():
    @pytest.mark.tags('All', 'TC2')
    def test_acc_reg(self):

        # Account registration - Medical facilitator

        landing_page = LandingPage(self.driver, self.wait)
        landing_page.click_rad_btn_demo_country()
        landing_page.click_rad_btn_tripura()
        landing_page.enter_phone_number_field(generator.generate_random_number())
        landing_page.click_next_button_two()
        landing_page.enter_role_name_field(details.get('name'))
        landing_page.click_next_button_three()
        landing_page.enter_sec_pin_one(details.get('pin'))
        landing_page.enter_sec_pin_two(details.get('pin'))
        landing_page.click_allow_access_btn()
        landing_page.click_allow_prompt()
        landing_page.click_search_facility(details.get('fac_name'))
        landing_page.click_yes_button()
        landing_page.click_skip_button()

        doc_creator.gen_documentation(5, 18, 2)

    @pytest.mark.tags('All', 'TC3')
    def test_add_patient(self):

        # Register a new patient

        patient_page = PatientPage(self.driver, self.wait)
        patient_page.click_search_patient()
        patient_page.click_reg_new_patient()
        patient_page.enter_patient_name_field(name_generator.generate_name())  # details.get('pat_name')
        patient_page.enter_age_field(details.get('age'))
        patient_page.click_trans_rad_btn()
        patient_page.click_female_rad_btn()
        patient_page.click_male_rad_btn()
        patient_page.enter_phone_field(generator.generate_random_number())
        patient_page.enter_address_field(details.get('address'))
        patient_page.enter_village_field(details.get('village'))
        patient_page.click_scroll()
        patient_page.click_next_btn()
        patient_page.click_no_rad_btn()
        patient_page.click_no_rad_btn_two()
        patient_page.click_yes_rad_btn()
        patient_page.click_yes_rad_btn_two()
        patient_page.click_next_button()
        patient_page.click_save_button()
        patient_page.click_prompt_not_now()
        patient_page.click_search_add_patient()
        patient_page.enter_search_patient_box(name_generator.names[0])
        patient_page.click_search_new_patient()

        doc_creator.gen_documentation(19, 28, 3)



