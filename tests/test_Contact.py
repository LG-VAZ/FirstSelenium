from pageObjects.CustomerCare import CustomerCare
from pageObjects.HomeParabank import HomeParabank
from utilities.BaseClass import BaseClass


class TestContact ( BaseClass ) :

    def test_customerCare ( self ) :
        home = HomeParabank ( self.driver )
        home.getbuttonContact ( ).click ( )
        contact = CustomerCare ( self.driver )

        # Corregir la línea siguiente
        contact.getCCName().send_keys("Anonimous")
        contact.getCCEmail().send_keys("example@abc.mzn")
        phone = contact.getCCPhone()
        phone.send_keys("123-456-789")
        contact.getCCMessage().send_keys("QWERTYUIO")

        assert len(phone) == 9, "La longitud del número de teléfono no es igual a 9"

        contact.getCCButton().click()
