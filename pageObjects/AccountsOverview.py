from selenium.webdriver.common.by import By

class AccountsOverview:

    def __init__(self, driver):
        self.driver = driver

    # Elementos relacionados con la tabla de cuentas
    balance_elements_locator = (By.XPATH, "//table[@id='accountTable']/tbody/tr/td[2][not(ancestor::tr/td/b[text()='Total'])]")
    total_balance_locator = (By.XPATH, "//table[@id='accountTable']/tbody/tr[3]/td[2]")

    def get_balance_elements(self):#obtenemos el valor de las tablas excluyendo Total
        return self.driver.find_elements(*AccountsOverview.balance_elements_locator)

    def get_total_balance_from_page(self):##Obtenemos el valor de Total
        total_balance_text = self.driver.find_element(*AccountsOverview.total_balance_locator).text
        return float(total_balance_text.strip('$'))

    def get_total_balance_from_elements(self):#suma de la columna
        balance_elements = self.get_balance_elements()
        total_balance_from_elements = sum(float(element.text.strip('$')) for element in balance_elements)
        return total_balance_from_elements
