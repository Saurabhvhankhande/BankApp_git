import time

from selenium.webdriver.common.by import By


class Login_page:
    click_Login_link_xpath="//a[normalize-space()='Login']"
    text_username_xpath="//input[@id='username']"
    text_password_xpath="//input[@id='password']"
    click_login_button_xpath="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def login_link(self):
        self.driver.find_element(By.XPATH,self.click_Login_link_xpath).click()

    def username_text(self,username):
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(username)

    def password_text(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH,self.click_login_button_xpath).click()
        time.sleep(5)

