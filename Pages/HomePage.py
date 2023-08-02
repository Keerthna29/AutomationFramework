from selenium.webdriver.common.by import By
class HomePage():

    def __init__(self,driver):
        self.driver=driver

        self.user_menu_link_xpath="//*[@id='app']//div/ul/li/span[@class='oxd-userdropdown-tab']"
        self.logout_link_link_text="Logout"
    def click_usermenu(self):
        self.driver.find_element(By.XPATH,self.user_menu_link_xpath).click()
    def click_logout(self):
        self.driver.find_element(By.PARTIAL_LINK_TEXT,self.logout_link_link_text).click()
