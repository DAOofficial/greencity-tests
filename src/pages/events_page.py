from selenium.webdriver.common.by import By
from src.components.auth_modal import AuthModal
from src.components.skip_container import SkipContainer
from src.pages.base_page import BasePageallure
from src.components.event_card_component import EventCard
from src.components.status_checkbox_component import StatusCheckbox
from src.components.search_field_component import SearchField
import allure

class EventsPage(BasePage):
    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"
    CARDS = (By.CLASS_NAME, "card-wrapper")

    @allure.step("Open Events page")
    def open(self):
        self.driver.get(self.BASE_URL)

    @allure.step("Get cards list")
    def get_cards(self):
        elements = self.find_list(self.CARDS)
        return [EventCard(self.driver, el) for el in elements]

    @allure.step("Get header")
    def header(self):
        return SkipContainer(self.driver, self.driver)

    @allure.step("Get auth modal")
    def auth_modal(self):
        return AuthModal(self.driver, self.driver)

    @allure.step("Get status checkbox")
    def status_filter(self):
        return StatusCheckbox(self.driver, self.driver)

    @allure.step("Get search field")
    def search(self):
        return SearchField(self.driver, self.driver)

    @allure.step("Get cards count")
    def get_cards_count(self):
        return len(self.get_cards())