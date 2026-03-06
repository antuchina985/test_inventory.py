from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from page.login_page import LoginPage



@pytest.mark.parametrize("usuario, password", [("standard_user", "secret_sauce")])      
def test_inventory(login_page, usuario, password):
    #solicion parcial ingresa a la pagina dos veces

    login_page.driver.get("https://www.saucedemo.com")
    # 1. Realizar el login primero
    login_page.login_completo(usuario, password)
    
    # 2. Inicializar la página de inventario usando el driver de login_page
    inventory_page = InventoryPage(login_page.driver)
    
    # 3. Acciones en el inventario
    inventory_page.agregar_al_carrito()
    inventory_page.abrir_carrito()

    # 4. Acciones en el carrito (Usamos login_page.driver en lugar de driver solo)
    cart_page = CartPage(login_page.driver)
    productos_en_carrito = cart_page.obtener_productos_carrito()
    
    #assert len(productos_en_carrito) > 0, "El carrito está vacío"

    assert False
    
 



