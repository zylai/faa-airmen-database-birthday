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

# Define search parameters here
# Parameters must be specific enough that the database only returns one result
# This script will automatically stop as soon as the search returns at least one match
# Using Charles Lindbergh to test since his DOB is publicly known
firstname = 'Charles'
lastname = 'Lindbergh'

# Initialize WebDriver and navigate to the webpage
driver = webdriver.Firefox()
driver.get("https://amsrvs.registry.faa.gov/airmeninquiry/Main.aspx")

# Define location of fields and buttons using XPath
firstname_field = '//*[@id="ctl00_content_ctl01_txtbxFirstName"]'
lastname_field = '//*[@id="ctl00_content_ctl01_txtbxLastName"]'
month_dropdown = '//*[@id="ctl00_content_ctl01_ddlSearchBirthMonth"]'
day_dropdown = '//*[@id="ctl00_content_ctl01_ddlSearchBirthDay"]'
year_field = '//*[@id="ctl00_content_ctl01_txtbxSearchBirthYear"]'
submit_buttom = '//*[@id="ctl00_content_ctl01_btnSearch"]'
airmen_exists = '//*[@id="ctl00_content_ctl01_drAirmenList_ctl01_lnkbtnAirmenName"]'

# Loop through all possible dates, starting at year 1901 as there is
# a glitch in the FAA's database where 01/01/1900 matches everyone
# A future update will allow you to define a narrower date range
for year in range(1901, 2020):
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
		for day in range(1, day_limit+1):
			driver.find_element_by_xpath(lastname_field).clear()
			driver.find_element_by_xpath(firstname_field).send_keys(firstname)
			driver.find_element_by_xpath(lastname_field).send_keys(lastname)

			# zfill adds leading zeroes to match the format of the day to the site's HTML values
			Select(driver.find_element_by_xpath(month_dropdown)).select_by_value(str(month).zfill(2))
			Select(driver.find_element_by_xpath(day_dropdown)).select_by_value(str(day).zfill(2))

			driver.find_element_by_xpath(year_field).clear()
			driver.find_element_by_xpath(year_field).send_keys(year)

			driver.find_element_by_xpath(submit_buttom).click()

			# Optional, but when the FAA site is slow, it's a good idea to add a time delay
			# to ensure that results have fully loaded before Selenium checks the page source
			# time.sleep(10)

			assert "search criteria provided above" in driver.page_source

			if (check()):
				print ("Birthday found: " + str(month) + "/" + str(day) + "/" + str(year))
				driver.close()
				exit()
