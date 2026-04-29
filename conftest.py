import pytest
from selenium import webdriver
import allure
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from data.config import Config


@pytest.fixture(scope="function")
def init_driver():
    with allure.step("Initialize WebDriver"):
        options = webdriver.ChromeOptions()
        if Config.HEADLESS_MODE:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        driver.implicitly_wait(Config.IMPLICIT_WAIT_TIMEOUT)
        driver.maximize_window()

    with allure.step(f"Navigate to {Config.BASE_UI_URL}"):
        driver.get(Config.BASE_UI_URL)
    yield driver
    with allure.step("Quit WebDriver"):
        driver.quit()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("init_driver")
        if driver is not None:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="failure_screenshot",
                attachment_type=allure.attachment_type.PNG
            )
