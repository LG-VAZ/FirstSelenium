from pageObjects.ParabankIndex import ParabankIndex
from pageObjects.Register import Register
from tests.conftest import take_screenshot
from utilities.BaseClass import BaseClass


class TestRegister(BaseClass):

    def test_Register(self):
        home = self.registerLink()
        register = Register(self.driver)
        register.getName().send_keys("Ks")
        register.getLastName().send_keys(" NAME")
        register.getAddress().send_keys(" 123")
        register.getCity().send_keys(" z")
        register.getState().send_keys(" State")
        register.getZip().send_keys("23")
        register.getPhone().send_keys("12")
        register.getSsn().send_keys("44")
        register.getUser().send_keys("adr")
        register.getPass().send_keys("adr")
        register.getConfirmPass().send_keys("adr")
        register.getButtonRegist().click()

        take_screenshot(self.driver, "test_Register.png")




