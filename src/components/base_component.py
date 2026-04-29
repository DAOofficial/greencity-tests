import allure
from selenium.webdriver.support.ui import WebDriverWait

class BaseComponent:

    def __init__(self, driver, root):
        self.driver = driver
        self.root = root
        self.driver = driver
        self._wait = WebDriverWait(driver, 10)

    @allure.step("Finding element: {locator}")
    def find(self, locator):
        return self.root.find_element(*locator)

    @allure.step("Enter email: {element}")
    def js_click(self, element):
        self.driver.execute_script("arguments[0].click();", element)