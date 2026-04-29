import pytest
import allure

from src.pages.events_page import EventsPage

BASE_URL = "https://www.greencity.cx.ua/#/greenCity/events"

@allure.feature("Filter events by status checkbox")
@allure.story("Filter events by status")
@allure.severity(allure.severity_level.NORMAL)
def test_status_checkbox(init_driver):
        page = EventsPage(init_driver)
        with allure.step("Open page"):
            initial_count = page.get_cards_count()
            status = page.status_filter()
            status.toggle()
        with allure.step("Select checkbox and click open"):
            # Open testing
            status.select("Open")
            status.toggle()
            cards = page.get_cards()
            assert len(cards) > 0, "No cards found"
            for card in cards:
                assert card.get_status() == "OPEN", "Not all found events are open"
            status.toggle()
            status.select("Open")
            status.toggle()
            assert len(page.get_cards()) == initial_count, "All events not displayed again"
            status.toggle()

        with allure.step("Select checkbox and click closed"):
            # Closed testing
            status.select("Closed")
            status.toggle()
            cards = page.get_cards()
            for card in cards:
                assert card.get_status() == "CLOSED", "Not all found events are closed"
            status.toggle()
            status.select("Closed")
            status.toggle()
        with allure.step("Select checkbox and click any status"):
            # Any status testing
            status.toggle()
            status.select("Any status")
            assert status.get_state("Open"), "Open is not selected"
            assert status.get_state("Closed"), "Closed is not selected"
            status.toggle()
            assert len(page.get_cards()) == initial_count, "Not all events are displayed again"
            status.toggle()
            if status.get_state("Any status"):
                status.select("Any status")
        with allure.step("Select checkbox and click both open and closed"):
            status.select("Open")
            status.select("Closed")
            assert status.get_state("Any status"), "Any status not linked when all options selected"
            status.toggle()
            assert len(page.get_cards()) == initial_count, "Not all events are displayed again"

@allure.feature("Verify search events")
@allure.story("Verify search by 1 valid and 1 failing search")
@allure.severity(allure.severity_level.MINOR)
def test_search_validation(init_driver):
    page = EventsPage(init_driver)
    with allure.step("Select search and input valid phrase"):
        test_phrase_true = "Event"
        test_phrase_fail = "Event54321"
        search = page.search()
        search.open()
        search.type(test_phrase_true)
        cards = page.get_cards()
        assert len(cards) > 0, "Event list is empty"
        for card in cards:
            title = card.get_title().upper()
            expected = test_phrase_true.upper()
            assert expected in title, f"Event '{card.get_title()}' doesn't contain '{test_phrase_true}'"
    with allure.step("Select search and input fail phrase"):
        search.type(test_phrase_fail)
        expected_text = "We didn't find any results matching to this search"
        error = search.get_error()
        assert error == expected_text, "Empty search text is incorrect"

@allure.feature("Verify auth prompt")
@allure.story("Verify auth prompt to create event")
@allure.severity(allure.severity_level.CRITICAL)
def test_create_event_authorization(init_driver):
        page = EventsPage(init_driver)
        page.header().click_create_event()
        modal = page.auth_modal()
        modal.wait_visible()
        assert modal.is_visible(), "Sign in modal window is not displayed"
        modal.close()
        modal.wait_closed(10)
        assert modal.is_visible() == False, "Sign in modal window not disappear"
