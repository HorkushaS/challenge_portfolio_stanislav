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

    def test_log_in_to_the_system_negative_password(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.assert_element_text(self.driver, LoginPage.title_of_box_xpath, LoginPage.header_of_box)
        user_login.type_in_email('user02@getnada.com')
        user_login.type_in_password('test-1234')
        user_login.wait_for_element_to_be_clickable(user_login.sign_in_button_xpath)
        user_login.click_on_the_sign_in_button()
        user_login.wait_for_element_to_be_visible(user_login.password_warning_xpath)
        user_login.assert_element_text(self.driver, LoginPage.password_warning_xpath, LoginPage.password_warning)


    @classmethod
    def tearDown(self):
        self.driver.quit()