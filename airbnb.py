from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

class airb():

	def test(self):
		
		driver = webdriver.Firefox()
		driver.get("https://www.airbnb.co.in/a/?af=43720035&c=.pi0.pk20073631801_195744006206_c_12026464216&gclid=Cj0KCQiAq6_UBRCEARIsAHyrgUwVad-VA77uaBe_rcwmK5pTq35S8dyz2tyEQGratNpOGcQkM59KkmsaAqiuEALw_wcB")
		#driver.implicitly_wait(5)
		
		checkIn = driver.find_element(By.XPATH,"//*[@id='checkin_input']")	
		checkIn.click()
		a = checkIn.is_displayed()

		print(str(a))				
		
		checkInDate = driver.find_element(By.XPATH,".//*[@id='MagicCarpetSearchBar']/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[6]")
		checkInDate.click()
		print("Hi")

		checkout = driver.find_element(By.XPATH,".//*[@id='MagicCarpetSearchBar']/div[2]/div/div/div[2]/div/div/div/div/div[2]/div[2]/div/div[2]/div/table/tbody/tr[4]/td[7]")
		checkout.click()

		adult = driver.find_element(By.XPATH,".//*[@id='adults']")
		sel = Select(adult)

		sel.select_by_value("5")
		time.sleep(2)		
		sel.select_by_index(3)
		sel.select_by_visible_text("8 adults")

		searchit = driver.find_element(By.XPATH,".//*[@id='lp-search-button']/button")
		searchit.click()

ff = airb()
ff.test()
