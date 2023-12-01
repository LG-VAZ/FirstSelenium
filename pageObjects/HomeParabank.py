from selenium.webdriver.common.by import By


class HomeParabank:
    def __init__(self, driver):
        self.driver = driver

    loginName = (By.NAME, "username")
    loginPass = (By.NAME, "password")
    buttonLogin = (By.CSS_SELECTOR, 'input[type="submit"].button')
    buttonContact = (By.LINK_TEXT , 'contact')

    def getNameLogin(self):
        return self.driver.find_element(*HomeParabank.loginName)

    def getPassLogin(self):
        return self.driver.find_element(*HomeParabank.loginPass)

    def getButtonLogin(self):
        return self.driver.find_element(*HomeParabank.buttonLogin)

    def getbuttonContact(self):
        return self.driver.find_element(*HomeParabank.buttonContact)