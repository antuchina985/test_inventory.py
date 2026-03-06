from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest

from utils.datos import leer_csv_login
from page.login_page import LoginPage
from utils.logger import logger

@pytest.mark.parametrize("usuario, password, debe_funcionar", leer_csv_login("datos/data_login.csv"))
def test_login_validation(login_page, usuario, password, debe_funcionar):
    # 'login_page' ya es el objeto de la clase LoginPage (viene del fixture)
    
    logger.info(f"--- Iniciando Test: Usuario {usuario} ---")
    
    logger.info("Navegando a la página de login...")
    login_page.abrir_pagina()
    # 1. USAR EL NOMBRE CORRECTO: login_completo
    logger.info(f"Ejecutando login_completo para {usuario}...")
    login_page.login_completo(usuario, password) 
    
    # 2. VALIDACIÓN
    driver = login_page.driver # Accedemos al driver guardado en el objeto
    
    if str(debe_funcionar).lower() == 'true':
        logger.info("Verificando que la URL sea /inventory.html")
        assert "/inventory.html" in driver.current_url, "Error: Login fallido para usuario válido"
        logger.info("Login exitoso.")
    else:
        logger.warning("Verificando mensaje de error esperado...")
        mensaje = login_page.obtener_error()
        assert "Epic sadface" in mensaje, f"Error inesperado: {mensaje}"
        logger.info(f"Mensaje de error validado: {mensaje}")