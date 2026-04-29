import allure


class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_list(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step("Click element")
    def click(self, locator):
        self.find(locator).click()