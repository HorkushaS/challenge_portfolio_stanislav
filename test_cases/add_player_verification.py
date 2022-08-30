import os
import time
import unittest

from selenium import webdriver

from pages.login_page import LoginPage
from pages.Dashboard import Dashboard
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT

class TestLoginPage(unittest.TestCase):

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_add_player_verification(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.assert_element_text(self.driver, LoginPage.title_of_box_xpath, LoginPage.header_of_box)
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.wait_for_element_to_be_clickable(user_login.sign_in_button_xpath)
        user_login.click_on_the_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.title_of_page()
        dashboard_page.click_on_the_players_button()
        dashboard_page.wait_for_element_to_be_clickable(dashboard_page.filter_table_button_xpath)
        dashboard_page.click_on_the_filter_table_button()
        dashboard_page.type_in_filter_name(dashboard_page.name)
        dashboard_page.type_in_filter_surname(dashboard_page.surname)
        dashboard_page.assert_main_position()
        time.sleep(3)


    @classmethod
    def tearDown(self):
        self.driver.quit()