from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from src.components.base_component import BaseComponent
import allure
from selenium.webdriver.support import expected_conditions as EC

class AuthModal(BaseComponent):

    MODAL = (By.XPATH, "//app-auth-modal")

    def __init__(self, driver, root):
        super().__init__(driver, root)
        self.driver = driver
        self.CLOSE_BUTTON = (By.CSS_SELECTOR, "img.cross-btn")

    @allure.step("Check if modal is visible")
    def is_visible(self):
        return len(self.driver.find_elements(*self.MODAL)) > 0

    @allure.step("Close modal window")
    def close(self):
        self.driver.find_element(*self.CLOSE_BUTTON).click()

    @allure.step("Waiting for closing modal...")
    def wait_closed(self, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            lambda d: len(d.find_elements(*self.MODAL)) == 0)

    @allure.step("Waiting to open modal...")
    def wait_visible(self, timeout=10):
        self._wait.until(EC.element_to_be_clickable(self.CLOSE_BUTTON))