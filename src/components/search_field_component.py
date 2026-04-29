import allure
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent

class SearchField(BaseComponent):

    SEARCH_ICON = (By.CSS_SELECTOR, ".search-img")
    INPUT = (By.XPATH, "//input[@placeholder='Search']")
    ERR_MSG = (By.XPATH, "//*[contains(text(), \"didn't find any results\")]")

    @allure.step("Open field")
    def open(self):
        self.driver.find_element(*self.SEARCH_ICON).click()

    @allure.step("Searching text: {text}")
    def type(self, text):
        field = self.driver.find_element(*self.INPUT)
        field.clear()
        field.send_keys(text)

    @allure.step("Get search error message")
    def get_error(self):
        return self.driver.find_element(*self.ERR_MSG).text.strip()