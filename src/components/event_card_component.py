import allure
from selenium.webdriver.common.by import By
from src.components.base_component import BaseComponent

class EventCard(BaseComponent):
    def __init__(self, driver, root):
        super().__init__(driver, root)

    STATUS = (By.CLASS_NAME, "event-status")
    TITLE = (By.CLASS_NAME, "event-name")

    @allure.step("Get card status")
    def get_status(self):
        return self.find(self.STATUS).text.strip().upper()

    @allure.step("Get card title")
    def get_title(self):
        return self.find(self.TITLE).text