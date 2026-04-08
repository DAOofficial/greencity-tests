import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class EventsPage(unittest.TestCase):

    BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

    def setUp(self):
        opt = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(options=opt)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get(self.BASE_URL)

    def toggle_status_menu(self):
        """Opens or closes status menu"""
        status_label = self.driver.find_element(By.XPATH, "//mat-label[contains(text(), 'Status')]")
        self.driver.execute_script("arguments[0].click();", status_label)

    def get_event_cards(self):
        return self.driver.find_elements(By.CLASS_NAME, "card-wrapper")

    def select_option(self, option_name):
        xpath = f"//mat-option//span[contains(text(), '{option_name}')]"
        option = self.driver.find_element(By.XPATH, xpath)
        option.click()

    def get_option_state(self, option_name):
        xpath = f"//mat-option//span[contains(text(), '{option_name}')]/ancestor::mat-option"
        return self.driver.find_element(By.XPATH, xpath).get_attribute("aria-selected")

    def test_status_checkbox(self):
        initial_count = len(self.get_event_cards())
        self.toggle_status_menu()

        # Open testing
        self.select_option("Open")
        self.toggle_status_menu()
        cards = self.get_event_cards()
        self.assertGreater(len(cards), 0)
        for card in cards:
            status = card.find_element(By.CLASS_NAME, "event-status").text
            self.assertEqual(status.strip().upper(), "OPEN")
        self.toggle_status_menu()
        self.select_option("Open")
        self.toggle_status_menu()
        self.assertEqual(len(self.get_event_cards()), initial_count)
        self.toggle_status_menu()

        # Closed testing
        self.select_option("Closed")
        self.toggle_status_menu()
        cards = self.get_event_cards()
        for card in cards:
            status = card.find_element(By.CLASS_NAME, "event-status").text
            self.assertEqual(status.strip().upper(), "CLOSED")
        self.toggle_status_menu()
        self.select_option("Closed")
        self.toggle_status_menu()

        # Any status testing
        self.toggle_status_menu()
        self.select_option("Any status")
        self.assertEqual(self.get_option_state("Open"), "true")
        self.assertEqual(self.get_option_state("Closed"), "true")
        self.toggle_status_menu()
        self.assertEqual(len(self.get_event_cards()), initial_count)
        self.toggle_status_menu()
        if self.get_option_state("Any status") == "true":
            self.select_option("Any status")
        self.select_option("Open")
        self.select_option("Closed")
        self.assertEqual(self.get_option_state("Any status"), "true", "Any status not linked when all options selected")
        self.toggle_status_menu()
        self.assertEqual(len(self.get_event_cards()), initial_count)

    def test_search_validation(self):
        test_phrase_true = "Event"
        test_phrase_fail = "Event54321"
        search_icon = self.driver.find_element(By.CSS_SELECTOR, ".search-img")
        search_icon.click()
        text_field = self.driver.find_element(By.XPATH, "//input[@placeholder='Search']")
        text_field.clear()
        text_field.send_keys(test_phrase_true)
        event_names = self.driver.find_elements(By.CLASS_NAME, "event-name")
        self.assertGreater(len(event_names), 0, "Event list is empty")
        for event in event_names:
            actual_title = event.text
            self.assertIn(test_phrase_true.upper(), actual_title.upper(),
                          f"Event '{actual_title}' doesn`t contain searched '{test_phrase_true}'")
        text_field.clear()
        text_field.send_keys(test_phrase_fail)
        error_msg_element = self.driver.find_element(By.XPATH, "//*[contains(text(), \"didn't find any results\")]")
        expected_text = "We didn't find any results matching to this search"
        actual_text = error_msg_element.text.strip()
        self.assertEqual(actual_text, expected_text, "Empty search text is incorrect")


    def test_create_event_authorization(self):
        create_event_btn = self.driver.find_element(By.XPATH, "//button[contains(text(), 'Create event')]")
        create_event_btn.click()
        wait = WebDriverWait(self.driver, 10)
        modal_xpath = "//app-auth-modal"
        sign_in_modal = wait.until(
            lambda d: d.find_element(By.XPATH, modal_xpath).is_displayed() and d.find_element(By.XPATH, modal_xpath))
        self.assertTrue(sign_in_modal.is_displayed(), "Sign in modal window is not displayed")
        close_icon = self.driver.find_element(By.CSS_SELECTOR, "img.cross-btn")
        self.driver.execute_script("arguments[0].click();", close_icon)
        wait.until(lambda d: len(d.find_elements(By.XPATH, modal_xpath)) == 0)
        modals = self.driver.find_elements(By.XPATH, "//app-auth-modal")
        self.assertEqual(len(modals), 0, "Sign in modal window is not closed")


    def tearDown(self):
        if self.driver:
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
