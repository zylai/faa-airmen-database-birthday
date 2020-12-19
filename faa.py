import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

def check():
	try:
		driver.find_element_by_xpath(airmen_exists)
		return True
	except:
		return False

driver = webdriver.Firefox()
driver.get("https://amsrvs.registry.faa.gov/airmeninquiry/Main.aspx")

lastname_field = '//*[@id="ctl00_content_ctl01_txtbxLastName"]'
month_dropdown = '//*[@id="ctl00_content_ctl01_ddlSearchBirthMonth"]'
day_dropdown = '//*[@id="ctl00_content_ctl01_ddlSearchBirthDay"]'
year_field = '//*[@id="ctl00_content_ctl01_txtbxSearchBirthYear"]'
submit_buttom = '//*[@id="ctl00_content_ctl01_btnSearch"]'
airmen_exists = '//*[@id="ctl00_content_ctl01_drAirmenList_ctl01_lnkbtnAirmenName"]'

for year in range(1900, 2020):
	for month in range(1, 13):
		if ((month == 4) or (month == 6) or (month == 9) or (month == 11)):
			day_limit = 30
		elif ((month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12)):
			day_limit = 31
		else:
			if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
				day_limit = 29
			else:
				day_limit = 28
		for day in range(27, day_limit+1):
			driver.find_element_by_xpath(lastname_field).clear();
			driver.find_element_by_xpath(lastname_field).send_keys("lindbergh"); #using charles lindbergh to test since his DOB is publicly known

			Select(driver.find_element_by_xpath(month_dropdown)).select_by_value(str(month).zfill(2))
			Select(driver.find_element_by_xpath(day_dropdown)).select_by_value(str(day).zfill(2))

			driver.find_element_by_xpath(year_field).clear();
			driver.find_element_by_xpath(year_field).send_keys(year)

			driver.find_element_by_xpath(submit_buttom).click()

			time.sleep(10)

			assert "search criteria provided above" in driver.page_source

			if (check()):
				print ("Birthday found: " + str(month) + "/" + str(day) + "/" + str(year))
				driver.close()
				exit()
