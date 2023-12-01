from selenium.webdriver.common.by import By


class Register:
    def __init__(self,driver):
        self.driver = driver

    name =(By.ID, "customer.firstName")
    lastName = (By.ID, "customer.lastName")
    address = (By.ID, "customer.address.street")
    city = (By.ID, "customer.address.city")
    state = (By.ID, "customer.address.state")
    zipCode = (By.ID, "customer.address.zipCode")
    phone = (By.ID, "customer.phoneNumber")
    ssn = (By.ID, "customer.ssn")
    user = (By.ID, "customer.username")
    passW = (By.ID, "customer.password")
    confirmPass = (By.ID, "repeatedPassword")
    buttonRegister = (By.CSS_SELECTOR, 'input[value="Register"]')

    def getName(self):
        return self.driver.find_element(*Register.name)

    def getLastName(self):
        return self.driver.find_element(*Register.lastName)

    def getAddress(self):
        return self.driver.find_element(*Register.address)

    def getCity(self):
        return self.driver.find_element(*Register.city)

    def getState(self):
        return self.driver.find_element(*Register.state)

    def getZip(self):
        return self.driver.find_element(*Register.zipCode)

    def getPhone(self):
        return self.driver.find_element(*Register.phone)

    def getSsn(self):
        return self.driver.find_element(*Register.ssn)

    def getUser(self):
        return self.driver.find_element(*Register.user)

    def getPass(self):
        return self.driver.find_element(*Register.passW)

    def getConfirmPass(self):
        return self.driver.find_element(*Register.confirmPass)

    def getButtonRegist(self):
        return self.driver.find_element(*Register.buttonRegister)