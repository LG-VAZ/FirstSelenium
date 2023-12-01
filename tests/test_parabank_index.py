from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from pageObjects.HomePageData import HomePageData
from pageObjects.HomeParabank import HomeParabank
from tests.conftest import take_screenshot
from utilities.BaseClass import BaseClass


class TestParabankIndex(BaseClass):

    def test_Parabank(self,getData):
        home = HomeParabank(self.driver)
        home.getNameLogin().send_keys(getData["user"])#get data de la case Data
        home.getPassLogin().send_keys(getData["pass"])
        home.getButtonLogin().click()

        #take_screenshot ( self.driver , "test2.png" )

    @pytest.fixture(params = HomePageData.test_Home_Page_Data)
    def getData(self, request):
        return request.param
