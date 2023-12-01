from pageObjects.AccountsOverview import AccountsOverview
from tests.conftest import take_screenshot
from tests.test_parabank_index import TestParabankIndex
from utilities.BaseClass import BaseClass


class TestAccount(BaseClass):
    def checkAccount(self,TestParabankIndex):
        login = TestParabankIndex.test_Parabank()
        balance_elements = AccountsOverview(self.driver)
        balance_elements.get_balance_elements()
        print(balance_elements)
        total_balance_from_elements = balance_elements.get_total_balance_from_elements()

        # Obtener el total de la página
        total_balance_from_page = balance_elements.get_total_balance_from_page()

        take_screenshot(self.driver, "AAA.png")

        # Imprimir el resultado en la consola
        print(f"Resultado de la comparación: total_balance_from_elements = {total_balance_from_elements}, total_balance_from_page = {total_balance_from_page}")

        # Verificar la igualdad usando un assert
        assert total_balance_from_elements == total_balance_from_page , "La suma de balances no coincide con el total."