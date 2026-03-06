from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class InventoryPage:
    #selectores
    __INVENTORY_ITEMS =(By.CLASS_NAME,"inventory_item")
    __ADD_TO_CART_BUTTON =(By.CLASS_NAME,"btn_inventory")
    __CART_BADGE =(By.CLASS_NAME,"shopping_cart_badge")
    __ITEM_NAME =(By.CLASS_NAME,"inventory_item_name")
    _CART_LINK =(By.CLASS_NAME,"shopping_cart_link")


    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)


    def obtener_todos_los_productos(self):
        self.wait.until(EC.visibility_of_all_elements_located(self.__INVENTORY_ITEMS))
        productos= self.driver.find_elements(*self.__INVENTORY_ITEMS)
        return productos
    
    def obtener_nombre_producto(self):
        productos= self.driver.find_elements(*self.__ITEM_NAME)
        
        return [producto_nombre.text for producto_nombre in productos]
    

    def agregar_al_carrito(self):
    # Usamos el método que ya corregimos antes
        productos = self.obtener_todos_los_productos()
        print(f"DEBUG: Se encontraron {len(productos)} productos")
    # Asegúrate de estar buscando el botón de compra, no solo el item
        boton_compra = self.driver.find_element(*self.__ADD_TO_CART_BUTTON)
        boton_compra.click()

    # En page/inventory_page.py
    def agregar_producto_por_nombre(self, nombre_producto):
    # Ahora nombre_producto es "Sauce Labs Backpack" (un string)
        productos = self.obtener_todos_los_productos()
        for p in productos:
            if p.find_element(*self.__ITEM_NAME).text.strip() == nombre_producto.strip():
                # Hacer clic en el botón de ese producto
                p.find_element(By.CSS_SELECTOR, ".btn_inventory").click()
                break

    def abrir_carrito(self):
        self.wait.until(EC.element_to_be_clickable(self._CART_LINK)).click()
        return self
    def obtener_cantidad_carrito(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.__CART_BADGE))
            contador_carrito = self.driver.find_element(*self.__CART_BADGE)
            return int(contador_carrito.text)
        except:
            return 0




    
        
