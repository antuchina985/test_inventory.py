import pytest
from selenium import webdriver
from page.login_page import LoginPage
from selenium.webdriver.chrome.options import Options 
import pathlib 
from datetime import datetime
import time

target = pathlib.Path("reports/screens") #  Carpeta para guardar las capturas de pantalla
target.mkdir(parents=True, exist_ok=True) # Asegura que la carpeta exista antes de guardar las capturas

@pytest.fixture
def driver():
    
    options=Options()
    options.add_argument("--incognito")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("window-size=1920,1080")
    options.add_argument("--headless=new")  # Descomenta esta línea para ejecutar en modo headless

@pytest.fixture
def login_page(driver):
    """
    Realiza el login y devuelve la instancia de la página 
    ya autenticada para interactuar con ella.
    """
    page = LoginPage(driver) # 1. Creamos la instancia
    page.abrir_pagina()      # 2. Usamos la instancia
    
    
    return page # 3. ¡DEVOLVEMOS LA PÁGINA, NO EL DRIVER!
@pytest.fixture

def url_base():
    return "https://jsonplaceholder.typicode.com/users"

@pytest.fixture
def api_key():
    return {
        "x-api-key": "reqres_9f2eb1c315cf4703a5a01e91fb3ad6b3",
        "Content-Type": "application/json"
    }

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield

    report = outcome.get_result()
    if report.when in ("setup", "call") and report.failed:
        driver = item.funcargs.get("driver", None)

        if driver: 
            #timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            timestamp_unix = int (time.time())
            file_name = target / f"{report.when}_{item.name}_{timestamp_unix}.png"
            driver.save_screenshot(str(file_name))
