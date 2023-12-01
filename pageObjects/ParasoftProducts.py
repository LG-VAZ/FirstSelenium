from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ParasoftProducts:
    def __init__(self,driver):
        self.driver=driver

    products=(By.LINK_TEXT,'Products')
    listaProducts=(By.ID,'menu-products-sub-menu')

    def getLocateButton(self):
        # Encontrar el elemento del botón "Products"
        button_to_hover_over=self.driver.find_element(*ParasoftProducts.products)
        # Crear una instancia de ActionChains
        actions=ActionChains(self.driver)
        # Mover el puntero encima del botón "Products"
        actions.move_to_element(button_to_hover_over).perform()
        return actions

    def getListaProducts(self):
        WebDriverWait(self.driver,10).until(EC.presence_of_element_located(self.products))
        product_elements=self.driver.find_elements(By.XPATH,'//ul[@id="menu-products-sub-menu"]/li/a')
        titles_and_elements=[(element.get_attribute('title'),element) for element in product_elements]
        print(titles_and_elements)
        return titles_and_elements

    def clickElementByIndex(self,index):
        elements=self.getListaProducts()
        if 0 <= index < len(elements):
            element_to_click=elements[index][1]
            element_to_click.click()
        else:
            print(f"Index {index} is out of range.")
