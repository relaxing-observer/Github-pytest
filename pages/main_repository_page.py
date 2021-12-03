import allure

from utils.browser_helper import BrowserHelper
from utils.locators import MainRepositoryPageLocators
from .base_page import BasePage
from .header_user_page import HeaderUserPage
from utils.generated_data import GeneratedData


class MainRepositoryPage(HeaderUserPage, BrowserHelper, BasePage):
    @allure.step("Go to repository settings page")
    def go_to_repository_settings(self):
        """
        Method goes to repository settings page.
        """
        self.browser.find_element(*MainRepositoryPageLocators.SETTINGS_REPOSITORY_BUTTON).click()

    @allure.step("Go to adding README")
    def go_to_adding_readme_page(self):
        """
        Method goes to adding README.
        """
        self.browser.find_element(*MainRepositoryPageLocators.ADDING_README_BUTTON).click()

    @allure.step("Verification of actual repo name by data comparison")
    def should_be_correct_repository_name(self):
        """
        Method verifies the actual name of repository with random name.
        """
        actual_repository_name = self.browser.find_element(*MainRepositoryPageLocators.ACTUAL_REPOSITORY_NAME).text
        assert str(actual_repository_name) in f"{GeneratedData.LAST_GENERATED_NAME}",\
            "Name of actual repo isn't correct"

    @allure.step("Verification of created README file")
    def should_be_created_readme_file(self):
        """
        Method verifies created README file.
        """
        assert self.is_element_present(*MainRepositoryPageLocators.LAST_COMMIT_TIMESTAMP), \
            "Probably commit with README hasn't created"