
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class ClickAndSendKeys():

    def test(self):
        baseUrl = "https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(baseUrl)
        driver.implicitly_wait(5)


        #time.sleep(4)

        email = driver.find_element(By.ID, "identifierId")
        email.click()
        email.send_keys("enter your email")

        #time.sleep(5)

        proceed = driver.find_element(By.XPATH, ".//*[@id='identifierNext']/content/span")

        proceed.click()

        time.sleep(2)

        password = driver.find_element(By.XPATH, ".//*[@id='password']/div[1]/div/div[1]/input")
        password.click()
        time.sleep(2)
        password.send_keys(" enter password")

        proceed_2 = driver.find_element(By.XPATH, ".//*[@id='passwordNext']/content/span")
        proceed_2.click()





ff = ClickAndSendKeys()
ff.test()
