"""
login into the work day
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from environment import *

import time

class Login_Workday(object):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password


    def do_login(self):
        driver = webdriver.Chrome()
        driver.get(self.url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.element_to_be_clickable((By.XPATH , "//div[@class='gwt-Label GDPVGE1BM1' and @data-automation-id='authSelectorOptionLabel' and text()='Native Login']")))
        driver.find_element(By.XPATH, "//div[@class='gwt-Label GDPVGE1BM1' and @data-automation-id='authSelectorOptionLabel' and text()='Native Login']").click()

        driver.find_element(By.XPATH, "//input[@class='gwt-TextBox GDPVGE1BC3B' and @aria-label='Username']").send_keys("n0s01nx")
        driver.find_element(By.XPATH, "//input[@class='gwt-PasswordTextBox GDPVGE1BC3B' and @aria-label='Password']").send_keys("Walmart@2023")
        driver.find_element(By.XPATH, "//button[@class='GDPVGE1BOSC' and text() = 'Sign In']").click()

        wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@aria-label='In what city does your nearest sibling live?']")))
        driver.find_element(By.XPATH, "//input[@aria-label='In what city does your nearest sibling live?']").send_keys("1")
        driver.find_element(By.XPATH, "//input[@aria-label='What were the last four digits of your childhood telephone number?']").send_keys("1")
        driver.find_element(By.XPATH, "//button[text() = 'Submit']").click()

        driver.maximize_window()
        return driver



d = Login_Workday(work_day_url, work_day_usname, work_day_password)
driver = d.do_login()

time.sleep(60)
