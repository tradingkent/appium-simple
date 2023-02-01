import base64
import os
import time
import pytest

from Pages.landing_page import LandingPage
from Utilities.common import RandomNumberGenerator
from Utilities.common import NameGenerator
from Utilities.data import details

# Patient page
from Pages.patient_page import PatientPage

generator = RandomNumberGenerator()
name_generator = NameGenerator()


@pytest.mark.usefixtures('setup')
class TestLanPage():

    def test_startup(self):
        # Validation of Opening and Start-up Pages

        landing_page = LandingPage(self.driver, self.wait)
        landing_page.click_next_button()
        landing_page.click_get_started_button()

