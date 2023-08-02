import time

import allure
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from Pages.LoginPage import LoginPage
from Pages.HomePage import HomePage
from Utils import Utils as Utils
import pytest
import moment
from conftest import test_setup


@pytest.mark.usefixtures("test_setup")
class TestLogin():

    def test_login(self):
        driver=self.driver

        url = Utils.URL
        driver.get(url)
        driver.implicitly_wait(5)

        login = LoginPage(driver)
        login.enter_username(Utils.USERNAME)
        login.enter_password(Utils.PASSWORD)
        login.click_login()

        # driver.find_element(By.NAME, "username").send_keys("Admin")
        # driver.find_element(By.NAME, "password").send_keys("admin123")
        # driver.find_element(By.XPATH, "//*[@id='app']//div/button").click()

    def test_logout(self):
        try:
            driver = self.driver

            home = HomePage(driver)
            home.click_usermenu()
            home.click_logout()
            # time.sleep(5)
            # driver.find_element(By.XPATH, "//*[@id='app']//div/ul/li/span[@class='oxd-userdropdown-tab']").click()
            # driver.find_element(By.PARTIAL_LINK_TEXT, "Logout").click()
            time.sleep(5)
            print(driver.title)
            x=driver.title
            assert x=="rangeHRM"
        except AssertionError as error:
            print("Assertion error occured")

            print(error)
            current_time=moment.now().strftime("%d-%m-%Y_%H-%M-%S")
            screenshot_name="screenshot_"+current_time
            allure.attach(self.driver.get_screenshot_as_png(),name=screenshot_name,attachment_type=allure.attachment_type.PNG)
            raise
        except:
            print("There was an exception")
        else:
            print("There is no exception")
        finally:
            print("all set")




