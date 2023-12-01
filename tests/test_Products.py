import time

import pytest

from pageObjects.ParabankIndex import ParabankIndex
from pageObjects.ParasoftJtest import ParasoftJetst
from pageObjects.ParasoftProducts import ParasoftProducts
from utilities.BaseClass import BaseClass


@pytest.mark.prueba1
class TestProdcut(BaseClass):

    def test_Product(self):
        home=ParabankIndex(self.driver)
        home.getProductsLink().click()
        productPage=ParasoftProducts(self.driver)
        productPage.getLocateButton()
        productPage.getListaProducts()
        productPage.clickElementByIndex(2)
        productJtest=ParasoftJetst(self.driver)
        productJtest.getMediaVideo().click()
        #realizamos el cambio al Iframe
        productJtest.switch_to_next_iframe()

        productJtest.getButtonPlay().click()

        number_of_clicks=5 #declaramos el numero de clicks

        for click_number in range(1,number_of_clicks + 1): #ciclo for para contar el numero de clicks en number of clicks
            productJtest.getButtonNext().click()           #Realizar click despues de cada iteracion

        productJtest.getButtonRestart().click()
        self.driver.switch_to.default_content()
        productJtest.getExitButton().click()

