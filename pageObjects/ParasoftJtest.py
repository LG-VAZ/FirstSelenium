from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ParasoftJetst:
    def __init__(self, driver):
        self.driver = driver

    videoMedia = (By.CSS_SELECTOR, ".play-button.click-track")
    playButton = (By.XPATH, '//button[contains(text(), "Static Analysis & SAST")]')
    iframe = (By.CLASS_NAME,"mfp-iframe")
    buttonNext = (By.XPATH, '//button[contains(text(), "Next")]')
    buttonRestar = (By.ID, "_text_CTA-PRIMARY")
    buttonExit = (By.CLASS_NAME, 'mfp-close')


    def getExitButton(self):
        return self.driver.find_element(*ParasoftJetst.buttonExit)

    def getButtonRestart(self):
        return self.driver.find_element(*ParasoftJetst.buttonRestar)

    def getButtonNext(self):
        return self.driver.find_element(*ParasoftJetst.buttonNext)

    def getMediaVideo(self):
        return self.driver.find_element(*ParasoftJetst.videoMedia)

    def switch_to_next_iframe(self):
        # Esperar a que el iframe esté presente en el DOM
        wait=WebDriverWait(self.driver,10)
        iframe_element=wait.until(EC.presence_of_element_located(ParasoftJetst.iframe))

        # Cambiar al iframe por el elemento
        self.driver.switch_to.frame(iframe_element)

    def getButtonPlay(self):
        # Esperar hasta que el botón sea clickeable
        wait=WebDriverWait(self.driver,10)
        button=wait.until(EC.element_to_be_clickable(ParasoftJetst.playButton))
        return button
