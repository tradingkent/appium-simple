import time
import pytest

from Pages.landing_page import LandingPage
from Utilities.common import RandomNumberGenerator
from Utilities.data import details

generator = RandomNumberGenerator()


@pytest.mark.usefixtures('setup')
class TestLanPage():
    def test_country_list(self):
        # Landing Page
        landing_page = LandingPage(self.driver, self.wait)
        landing_page.click_next_button()
        landing_page.click_get_started_button()
        landing_page.click_rad_btn_demo_country()

    def test_clinic_region_list(self):

        landing_page = LandingPage(self.driver, self.wait)
        landing_page.click_rad_btn_tripura()
        landing_page.enter_phone_number_field(generator.generate_random_number())
        landing_page.click_next_button()
        landing_page.enter_role_name_field(details.get('name'))
        landing_page.click_next_button()
        landing_page.enter_sec_pin_one(details.get('pin'))
        landing_page.enter_sec_pin_two(details.get('pin'))
        landing_page.click_allow_access_btn()

    def test_facility_name_list(self):
        landing_page = LandingPage(self.driver, self.wait)
        landing_page.click_allow_prompt()

    def test_search_facility_name(self):
        landing_page = LandingPage(self.driver, self.wait)
        landing_page.click_search_facility(details.get('fac_name'))
        landing_page.click_yes_button()

    def test_landing_to_home(self):
        landing_page = LandingPage(self.driver, self.wait)
        landing_page.click_skip_button()




















    '''
        def test_country_list(self):
        # Landing Page
        landing_page = LandingPage(self.driver, self.wait)
        landing_page.click_next_button()
        landing_page.click_get_started_button()
        landing_page.click_rad_btn_demo_country()
        landing_page.click_rad_btn_tripura()
        landing_page.enter_phone_number_field(generator.generate_random_number())
        landing_page.click_next_button()
        landing_page.enter_role_name_field(details.get('name'))
        landing_page.click_next_button()
        landing_page.enter_sec_pin_one(details.get('pin'))
        landing_page.enter_sec_pin_two(details.get('pin'))
        landing_page.click_allow_access_btn()
        landing_page.click_allow_prompt()
        landing_page.click_search_facility(details.get('fac_name'))
        landing_page.click_yes_button()
        landing_page.click_skip_button()
    '''
