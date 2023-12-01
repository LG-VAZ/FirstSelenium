import pytest

from pageObjects.ParabankIndex import ParabankIndex


@pytest.mark.usefixtures("setup")
class BaseClass:
    def registerLink(self):
        parabankIndex = ParabankIndex(self.driver)
        parabankIndex.registerLink().click()
        return parabankIndex