from pages.base_page import BasePage


class Dashboard(BasePage):
    # Since I'm not sure which version of the page we should test
    # I will be using both localization specific locators (EN page) and structure specific.
    # I guess if we're making tests for both PL and EN versions
    # we should only use structure specific locators like:
    # main_page_button_xpath = "//*[@id="__next"]/div[1]/div/div/div/ul[1]/div[1]" OR
    # sidebar_burger_menu_button_xpath = "//*[@aria-label='menu']'
    # since it will allow us to access this button on both versions
    # but text locators is shorter and it's unclear after a lesson
    # which locator is optimal in this case, I would prefer aforementioned universal xpath

    main_page_button_xpath = "//*[text()='Main page']"
    players_button_xpath = "//*[text()='Players']"
    polski_button_xpath = "//*[text()='Polski']"
    sign_out_button_xpath = "//*[text()='Sign out']"
    sidebar_burger_menu_button_xpath = "//*[@aria-label='menu']"
    dev_team_contact_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[1]/div/div[3]/a"
    add_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[2]/div/div/a/button/span[1]"
    last_created_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[1]/button/span[1]"
    last_updated_player_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[2]/button/span[1]"
    last_updated_report_button_xpath = "//*[@id='__next']/div[1]/main/div[3]/div[3]/div/div/a[3]/button/span[1]"
    pass
