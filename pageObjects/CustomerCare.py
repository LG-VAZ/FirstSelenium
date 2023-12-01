from selenium.webdriver.common.by import By

class CustomerCare:
    def __init__(self, driver):
        self.driver = driver

    name = (By.ID, "name")
    email = (By.ID, "email")
    phone = (By.ID, "phone")
    message = (By.ID, "message")
    buttonCC = (By.CSS_SELECTOR, 'input[value="Send to Customer Care"]')

    def getCCName(self):
        return self.driver.find_element(*CustomerCare.name)

    def getCCEmail(self):
        return self.driver.find_element(*CustomerCare.email)

    def getCCPhone(self):
        return self.driver.find_element(*CustomerCare.phone)

    def getCCMessage(self):
        return self.driver.find_element(*CustomerCare.message)

    def getCCButton(self):
        return self.driver.find_element(*CustomerCare.buttonCC)
