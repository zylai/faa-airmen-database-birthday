import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Firefox()
driver.get("https://amsrvs.registry.faa.gov/airmeninquiry/Main.aspx")

lastname_field = '//*[@id="ctl00_content_ctl01_txtbxLastName"]'
month_dropdown = '//*[@id="ctl00_content_ctl01_ddlSearchBirthMonth"]'
day_dropdown = '//*[@id="ctl00_content_ctl01_ddlSearchBirthDay"]'
year_field = '//*[@id="ctl00_content_ctl01_txtbxSearchBirthYear"]'
submit_buttom = '//*[@id="ctl00_content_ctl01_btnSearch"]'

for year in range(1900, 2020):
	search_year = year
	for month in range(1, 12):
		search_month = month
		if ((search_month == 4) or (search_month == 6) or (search_month == 9) or (search_month == 11)):
			day_limit = 30
		elif ((search_month == 1) or (search_month == 3) or (search_month == 5) or (search_month == 7) or (search_month == 8) or (search_month == 10) or (search_month == 12)):
			day_limit = 31
		else:
			if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
				day_limit = 29
			else:
				day_limit = 28
		for day in range(1, day_limit):
			driver.find_element_by_xpath(lastname_field).clear();
			driver.find_element_by_xpath(lastname_field).send_keys("lindbergh");

			Select(driver.find_element_by_xpath(month_dropdown)).select_by_value(str(month).zfill(2))
			Select(driver.find_element_by_xpath(day_dropdown)).select_by_value(str(day).zfill(2))

			driver.find_element_by_xpath(year_field).clear();
			driver.find_element_by_xpath(year_field).send_keys(year)

			driver.find_element_by_xpath(submit_buttom).click()

			time.sleep(60)
