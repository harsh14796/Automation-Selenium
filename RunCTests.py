from selenium import webdriver
import os


class RunChromeTestsWindows():
    # https://sites.google.com/a/chromium.org/chromedriver/downloads
    # http://chromedriver.storage.googleapis.com/index.html?path=2.21/
    def test(self):
        driver = webdriver.Chrome()
        driver.get("http://www.letskodeit.com")
        options.addArguments("disable-infobars")


chromeTest = RunChromeTestsWindows()
chromeTest.test()
