import datetime
import time

import pytest
from selenium import webdriver
from selenium.common import WebDriverException

driver = None


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome")


@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    driver.implicitly_wait(10)
    driver.get("https://parabank.parasoft.com/parabank/index.htm")
    driver.maximize_window()

    request.cls.driver = driver #DECLARAMOS Driver como universal para diferentes pruebas
    yield  # Proporcionar el objeto driver a las pruebas
    driver.quit()
    # Cierre del navegador al finalizar la prueba, incluso si hay errores

def take_screenshot(driver, filename):
    try:
        driver.save_screenshot(filename)
        print(f"Captura de pantalla guardada: {filename}")
    except WebDriverException as e:
        print(f"No se pudo tomar la captura de pantalla: {e}")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    # Si la prueba falla, tomar una captura de pantalla
    if rep.when == "call" and rep.failed:
        try:
            driver = item.funcargs['driver']
            timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            screenshot_filename = f"error_screenshot_{timestamp}.png"
            take_screenshot(driver, screenshot_filename)
        except WebDriverException as e:
            print(f"No se pudo tomar la captura de pantalla: {e}")