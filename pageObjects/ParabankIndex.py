from selenium.webdriver.common.by import By


class ParabankIndex:

    def __init__(self, driver):
        self.driver = driver

    register = (By.LINK_TEXT, "Register")
    products = (By.LINK_TEXT, "Products")

    def registerLink(self):
        return self.driver.find_element(*ParabankIndex.register)

    def getProductsLink( self ):
        return self.driver.find_element(*ParabankIndex.products)
