import allure
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


@allure.step("Get option: {option_name}")
def get_option(option_name):
    option_locator = (By.XPATH, f"//mat-option//span[contains(text(), '{option_name}')]")
    return option_locator


class StatusCheckbox(BaseComponent):

    label_locator = (By.XPATH, "//mat-label[contains(text(), 'Status')]")

    @allure.step("Toggle checkbox")
    def toggle(self):
        label = self.driver.find_element(*self.label_locator)
        self.js_click(label)

    @allure.step("Select option: {name}")
    def select(self, name):
        option = self.driver.find_element(*get_option(name))
        option.click()

    @allure.step("Finding option: {option_name}")
    def get_state(self, option_name):
        option = self.driver.find_element(
            By.XPATH,
            f"//mat-option[.//span[normalize-space()='{option_name}']]"
        )
        return "mdc-list-item--selected" in option.get_attribute("class")