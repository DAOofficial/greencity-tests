import allure
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent


class SkipContainer(BaseComponent):

    CREATE_EVENT_BTN = (By.XPATH, "//button[contains(text(), 'Create event')]")

    def __init__(self, driver, root):
        super().__init__(driver, root)
        self.driver = driver

    @allure.step("Click create event")
    def click_create_event(self):
        self.driver.find_element(*self.CREATE_EVENT_BTN).click()