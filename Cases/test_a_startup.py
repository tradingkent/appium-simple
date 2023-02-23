import base64
import os
import time
import pytest
#import softest

from Pages.landing_page import LandingPage
from Utilities.common import RandomNumberGenerator, DocumentCreator, FolderCreator
from Utilities.common import NameGenerator
from Utilities.data import details

# Patient page
from Pages.patient_page import PatientPage

generator = RandomNumberGenerator()
name_generator = NameGenerator()
doc_creator = DocumentCreator()
fol_creator = FolderCreator()

@pytest.mark.usefixtures('setup')
class TestLanPage():

    @pytest.mark.tags('All', 'TC1')
    def test_startup(self):
        # Validation of Opening and Start-up Pages

        landing_page = LandingPage(self.driver, self.wait)
        fol_creator.create_folder()
        landing_page.click_next_button()
        landing_page.click_get_started_button()
        doc_creator.gen_documentation(2, 4, 1)

