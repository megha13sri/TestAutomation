"""
login into the work day
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from super_base_class import *
import time
import os


class Login_Workday(object):
    def __init__(self, url, username, password):
        self.url = url
        self.username = username
        self.password = password

    @staticmethod
    def get_driver():
        """
        This Function will return the selenium Driver
        :arg: None
        :return:
        """
        download_path = os.getcwd()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("prefs", {
            "download.default_directory": download_path,
            "download.prompt_for_download": False,
            "download.directory_upgrade": True,
            "safebrowsing.enabled": True
        })

        driver = webdriver.Chrome(options=chrome_options)
        return driver

    def do_login(self, driver):
        """
        This function will login into the workday.
        :param driver:
        :return: Nothing
        """

        driver.get(self.url)
        wait = WebDriverWait(driver, 20)
        wait.until(EC.element_to_be_clickable((By.XPATH, Xpath_Native)))
        driver.find_element(By.XPATH, Xpath_Native).click()

        driver.find_element(By.XPATH, Xpath_UserName).send_keys(self.username)
        driver.find_element(By.XPATH, Xpath_Password).send_keys(self.password)
        driver.find_element(By.XPATH, Xpath_SignIn).click()

        #wait.until(EC.element_to_be_clickable((By.XPATH, Xpath_Sibling_Quest)))
        #driver.find_element(By.XPATH, Xpath_Sibling_Quest).send_keys("1")
        #driver.find_element(By.XPATH, Xpath_Telephone_Quest).send_keys("1")
        #driver.find_element(By.XPATH, Xpath_Submit).click()

        driver.maximize_window()
        time.sleep(20)

    def get_file_from_wid(self, driver, wid_number):
        """
        Arguments:
        driver(str): selenium obj
        wid_number(str): wid_number

        Return: None
        """
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, Xpath_Search_Box)))
        search_input = driver.find_element(By.XPATH, Xpath_Search_Input)
        search_input.click()
        search_input = driver.find_element(By.XPATH, Xpath_Search_Input)
        search_input.send_keys("wid:" + wid_number)
        driver.implicitly_wait(3)
        search_input.send_keys(Keys.ENTER)

        time.sleep(2)
        try:
            driver.find_element(By.XPATH, Xpath_Click_File).click()
            time.sleep(2)
            driver.find_element(By.XPATH, Xpath_File_Details).click()
            time.sleep(2)
            driver.save_screenshot(current_log_dir + "download_file.png")
            element = driver.find_elements(By.XPATH, Xpath_File_Image)
            if len(element) > 1:
                download_link = element[1]
                download_link.click()
            else:
                element.click()
        except Exception as e:
            logger.error("An Error came in execution \n" + str(e))



    def get_integration_screen_shot(self, driver, wid_number):
        self.do_login(driver)
        driver.implicitly_wait(5)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.element_to_be_clickable((By.XPATH, Xpath_Search_Box)))
        search_input = driver.find_element(By.XPATH, Xpath_Search_Input)
        search_input.click()
        search_input = driver.find_element(By.XPATH, Xpath_Search_Input)
        search_input.send_keys("wid:" + wid_number)
        driver.implicitly_wait(3)
        search_input.send_keys(Keys.ENTER)
        driver.find_element(By.XPATH, Xpath_Integration_link).click()
        driver.implicitly_wait(1)
        time.sleep(2)
        driver.save_screenshot(current_log_dir + "integration_image.png")



#driver = Login_Workday.get_driver()
