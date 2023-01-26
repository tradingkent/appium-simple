import time

from Pages.landing_page import wait
from Pages.landing_page import driver
from Pages.landing_page import LandingPage
from Utilities.data import details


class LanPage():

    def landing_page(self):

        # Landing Page
        landing_page = LandingPage(driver, wait)
        landing_page.click_next_button()
        landing_page.click_get_started_button()
        landing_page.click_rad_btn_demo_country()
        landing_page.click_rad_btn_tripura()
        landing_page.enter_phone_number_field(details.get('number'))
        landing_page.click_next_button()
        landing_page.enter_role_name_field(details.get('name'))
        landing_page.click_next_button()

        time.sleep(5)


landing = LanPage()
landing.landing_page()


