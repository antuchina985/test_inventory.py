import pytest
from page.login_page import LoginPage # Asegúrate de tener esta si la usas como fixture
from page.inventory_page import InventoryPage
from page.cart_page import CartPage
from utils.lectos_json import leer_json


RUTA_JSON = "datos/productos.json"

@pytest.mark.parametrize("usuario, password", [("standard_user", "secret_sauce")])    
@pytest.mark.parametrize("nombre_producto", leer_json(RUTA_JSON))  
def test_inventory(login_page, usuario, password, nombre_producto):
    #solicion parcial ingresa a la pagina dos veces

    login_page.driver.get("https://www.saucedemo.com")
    # 1. Realizar el login primero
    login_page.login_completo(usuario, password)
    
    # 2. Inicializar la página de inventario usando el driver de login_page
    inventory_page = InventoryPage(login_page.driver)
   # 3. Acciones en el inventario
# Aquí solo ejecutas la acción. No guardes el resultado en una variable.
    inventory_page.agregar_producto_por_nombre(nombre_producto["nombre"])

# 4. Ir al carrito para verificar
    inventory_page.abrir_carrito() 

# 5. Inicializar CartPage y obtener los nombres reales del carrito
    cart_page = CartPage(login_page.driver)
    nombres_reales = cart_page.obtener_nombres_productos_carrito()

# 6. Verificación final (Assert)
# Comprobamos si el nombre que queríamos agregar está en la lista del carrito
    assert nombre_producto["nombre"] in nombres_reales, \
    f"Error: {nombre_producto['nombre']} no encontrado en el carrito. Encontrados: {nombres_reales}"
    

    


