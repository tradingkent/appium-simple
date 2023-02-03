import base64
import os
import time
import pytest

from Pages.landing_page import LandingPage
from Pages.medical_details_page import MedDetails
from Pages.new_medicine_page import NewMedicine
from Utilities.common import RandomNumberGenerator
from Utilities.common import NameGenerator
from Utilities.data import details, medical_data

# Patient page
from Pages.patient_page import PatientPage

generator = RandomNumberGenerator()
name_generator = NameGenerator()


@pytest.mark.usefixtures('setup')
class TestMedDetails():

    def test_add_med_details(self):
        # Adding of Medicine details in Patient profile (Existing)

        medical_details = MedDetails(self.driver, self.wait)
        medical_details.click_medicine_btn()
        medical_details.click_choose_meds()
        medical_details.click_save_btn_add_drug()

    def test_add_bp_details(self):
        # Adding of Blood pressure readings in Patient profile

        medical_details = MedDetails(self.driver, self.wait)
        medical_details.click_bp_btn()
        medical_details.enter_systolic_field(medical_data.get('sys'))
        medical_details.enter_diastolic_field(medical_data.get('dia'))
        medical_details.click_change_btn()
        medical_details.click_bp_day_field(medical_data.get('days'))
        medical_details.click_diabetes_btn()
        medical_details.click_rbs_option()
        medical_details.enter_rbs_field(medical_data.get('rbs'))
        medical_details.click_save_btn()
        medical_details.click_done_btn()

    def test_add_new_meds(self):
        # Adding of Medicine details in Patient profile (New)

        new_meds = NewMedicine(self.driver, self.wait)
        new_meds.click_search_add_patient()
        new_meds.enter_search_patient_box(name_generator.names[0])
        new_meds.click_search_new_patient()
        new_meds.click_medicine_btn()
        new_meds.click_add_anthr_med()
        new_meds.enter_search_med(medical_data.get('new_meds'))
        new_meds.click_aspirin_od()
        new_meds.enter_med_dos(medical_data.get('new_dos'))
        new_meds.click_frequency_drp()
        new_meds.click_freq_bd()
        new_meds.click_add_btn()
        new_meds.click_save_btn()
