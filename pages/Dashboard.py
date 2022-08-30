import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    expected_title = 'Scouts panel'
    dashboard_url = ('https://scouts-test.futbolkolektyw.pl/')

    main_page_button_xpath = "//*/ul[1]/div[1]/div[2]/span"
    players_button_xpath = "//*/ul[1]/div[2]/div[2]/span"
    polski_button_xpath = "//*/ul[2]/div[1]/div[2]/span"
    sign_out_button_xpath = "//*/ul[2]/div[2]/div[2]/span"
    sidebar_burger_menu_button_xpath = "//*[@aria-label='menu']"
    dev_team_contact_button_xpath = "//*/div/div[3]/a"
    add_player_button_xpath = "//*/div[2]/div/div/a/button/span[1]"
    last_created_player_button_xpath = "//*/div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_button_xpath = "//*/div[3]/div/div/a[2]/button/span[1]"
    last_updated_report_button_xpath = "//*/div[3]/div/div/a[3]/button/span[1]"
    logo_scouts_panel_xpath = "//*[contains(@class,'MuiCardMedia-root')]"
    add_player_span_xpath = "//*/form/div[1]/div/span"
    name = "Burning"
    player_name_input_xpath = "//*/div[2]/div/div/input"
    surname = "Flame"
    player_surname_input_xpath = "//*/div[3]/div/div/input"
    age = "10.10.1995"
    age_input_xpath = "//*/div[7]/div/div/input"
    main_position = "Goalkeeper"
    main_position_input_xpath = "//*/div[11]/div/div/input"
    submit_button_xpath = "//*/div[3]/button[1]/span[1]"
    filter_table_button_xpath = "//*/div[2]/span[3]/button"
    filter_name_input_xpath = "//*/div[2]/div[1]/div/div/div/input"
    filter_surname_input_xpath = "//*/div[2]/div[2]/div/div/div/input"
    filter_table_main_position_xpath = "//*[@id='MUIDataTableBodyRow-0']/td[4]/div[2]"
    log_out_button_xpath = "//*/div/ul[2]/div[2]"

    def title_of_page(self):
        self.wait_for_element_to_be_clickable(self.players_button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def click_on_the_add_player_button(self):
        self.click_on_the_element(self.add_player_button_xpath)

    def type_in_name(self, name):
        self.field_send_keys(self.player_name_input_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.player_surname_input_xpath, surname)

    def type_in_age(self, age):
        self.field_send_keys(self.age_input_xpath, age)

    def type_in_main_position(self, main_position):
        self.field_send_keys(self.main_position_input_xpath, main_position)

    def click_on_the_submit_button(self):
        self.click_on_the_element(self.submit_button_xpath)

    def click_on_the_players_button(self):
        self.click_on_the_element(self.players_button_xpath)

    def click_on_the_filter_table_button(self):
        self.click_on_the_element(self.filter_table_button_xpath)

    def type_in_filter_name(self, name):
        self.field_send_keys(self.filter_name_input_xpath, name)

    def type_in_filter_surname(self, surname):
        self.field_send_keys(self.filter_surname_input_xpath, surname)

    def assert_main_position(self):
        self.assert_element_text(self.driver, self.filter_table_main_position_xpath, self.main_position)

    def click_on_the_log_out_button(self):
        self.click_on_the_element(self.log_out_button_xpath)

    pass
    # Task 2
    # Since I'm not sure which version of the page we should test
    # I will be using both localization specific locators (EN page) and structure specific.
    # I guess if we're making tests for both PL and EN versions
    # we should only use structure specific locators like:
    # main_page_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]" OR
    # sidebar_burger_menu_button_xpath = "//*[@aria-label='menu']'
    # since it will allow us to access this button on both versions
    # but text locators is shorter and it's unclear after a lesson
    # which locator is optimal in this case, I would prefer aforementioned universal xpath
    #
    # UPD: changed and cropped xpaths after watching Office hours, thanks Pati <3


