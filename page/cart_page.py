from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class CartPage:

    # Selectores
    _CART_ITEMS = (By.CLASS_NAME, "cart_item")
    _CART_ITEM_NAME = (By.CLASS_NAME, "inventory_item_name")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def obtener_productos_carrito(self):
        productos = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEMS))
        return productos
    
    # page/cart_page.py

# En page/cart_page.py
    def obtener_nombres_productos_carrito(self):
       elementos = self.wait.until(EC.visibility_of_all_elements_located(self._CART_ITEM_NAME))
       return [el.text for el in elementos]
 
    

      