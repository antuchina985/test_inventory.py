from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class LoginPage:
    # URL de la pagina de login
    URL = "https://www.saucedemo.com/"

    # Localizadores (Tuplas)
    _USER_INPUT = (By.ID, "user-name")
    _PASSWORD_INPUT = (By.ID, "password")
    _LOGIN_BUTTON = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def abrir_pagina(self):
        self.driver.get(self.URL)
        return self

    def ingresar_usuario(self, usuario):
        # Usamos *self._USER_INPUT para desempaquetar la tupla
        user_input = self.wait.until(EC.visibility_of_element_located(self._USER_INPUT))
        user_input.clear()
        user_input.send_keys(usuario)
        return self

    def ingresar_pass(self, password):
         # El '*' es vital aquí porque _PASSWORD_INPUT es una tupla (By.ID, "password")
        password_input = self.driver.find_element(*self._PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)
        return self

    def hacer_click_login(self):
     # Aquí también agregamos el '*'
        self.driver.find_element(*self._LOGIN_BUTTON).click()
        return self

    def login_completo(self, usuario, password):
        self.ingresar_usuario(usuario)
        self.ingresar_pass(password)
        time.sleep(3)
        self.hacer_click_login()
        return self
    

    def obtener_error(self):
        div_error = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".error-message-container.error h3")))
        return div_error.text