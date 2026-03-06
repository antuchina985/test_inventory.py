from selenium.webdriver.common.by import By
from page.login_page import LoginPage
from selenium import webdriver
import pytest
from conftest import driver
from page.inventory_page import InventoryPage


@pytest.mark.parametrize("usuario,password", [("standard_user","secret_sauce")])      
def test_inventory(login_page, usuario, password):
    # Asumiendo que login_page ya tiene el navegador iniciado
    inventory_page = InventoryPage(login_page.driver)
    login_page.login_completo(usuario, password)

    # Verificar productos
    productos = inventory_page.obtener_todos_los_productos()
    assert len(productos) > 0, "La cantidad de productos no es correcta"

    # Verificar carrito vacío
    assert inventory_page.obtener_cantidad_carrito() == 0, "El carrito no está vacío"

    # Agregar al carrito
    inventory_page.agregar_al_carrito()
    assert inventory_page.obtener_cantidad_carrito() == 1, "Error al agregar producto"





