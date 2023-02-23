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
class TestMedDetails():

    @pytest.mark.tags('All', 'TC4')
    def test_add_med_details(self):
        # Adding of Medicine details in Patient profile (Existing)

        medical_details = MedDetails(self.driver, self.wait)
        medical_details.click_medicine_btn()
        medical_details.click_choose_meds()
        medical_details.click_save_btn_add_drug()

        doc_creator.gen_documentation(29, 33, 4)

    @pytest.mark.tags('All', 'TC5')
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

    @pytest.mark.tags('All', 'TC6')
    def test_switch_diff_facility(self):
        # Switch to a different facility (Medical Facilitator)

        medical_details = MedDetails(self.driver, self.wait)
        change_fac = ChangeFac(self.driver, self.wait)
        change_fac.click_change_fac_btn()
        change_fac.click_new_fac_uhc_rees()
        medical_details.click_save_btn()
        medical_details.click_done_btn()

    @pytest.mark.tags('All', 'TC7')
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

    @pytest.mark.tags('All', 'TC8')
    def test_remove_existing_meds(self):
        # Removal of existing medicine

        rem_details = RemDetails(self.driver, self.wait)
        rem_details.click_medicine_btn()
        rem_details.click_uncheck_meds()
        rem_details.click_save_btn()

    @pytest.mark.tags('All', 'TC9')
    def test_update_bp_details(self):
        # Update existing Blood pressure details

        rem_details = RemDetails(self.driver, self.wait)
        rem_details.click_bp_edit()
        rem_details.enter_sys_dia_edit(medical_data.get('sys_new'),
                                       medical_data.get('dia_new'))

    @pytest.mark.tags('All', 'TC10')
    def test_remove_bp_details(self):
        # Remove existing blood pressure details

        rem_details = RemDetails(self.driver, self.wait)
        rem_details.click_bp_edit_remove()
        rem_details.click_remove_bp_btn()
        rem_details.click_remove_prompt_bp_btn()

    @pytest.mark.tags('All', 'TC11')
    def test_update_med_history(self):
        # Update medical history

        rem_details = RemDetails(self.driver, self.wait)
        rem_details.click_edit_save_btn()
        rem_details.click_not_now_prompt()
        rem_details.click_done_btn()
        rem_details.click_search_new_patient()
