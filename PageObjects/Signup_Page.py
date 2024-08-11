import time

from selenium.webdriver.common.by import By


class SignUp_Class:
    click_Signup_button_xpath = "//a[normalize-space()='Sign Up']"
    text_username_xpath = "//input[@id='username']"
    text_password_xpath = "//input[@id='password']"
    text_email_xpath = "//input[@id='email']"
    text_phone_xpath = "//input[@id='phone']"
    click_CreateUser_button_xpath = "//button[@type='submit']"
    success_msg_xpath = "//div[@class='success-message']"


    def __init__(self,driver):
        self.driver=driver


    def SignUp_button(self):
        self.driver.find_element(By.XPATH,self.click_Signup_button_xpath).click()

    def Enter_username(self,username):
        self.driver.find_element(By.XPATH,self.text_username_xpath).send_keys(username)

    def Enter_password(self,password):
        self.driver.find_element(By.XPATH,self.text_password_xpath).send_keys(password)

    def Enter_email(self,email):
        self.driver.find_element(By.XPATH,self.text_email_xpath).send_keys(email)

    def Enter_phone(self,phone):
        self.driver.find_element(By.XPATH,self.text_phone_xpath).send_keys(phone)
    def Create_User_button(self):
        self.driver.find_element(By.XPATH,self.click_CreateUser_button_xpath).click()
        time.sleep(10)

    def success_msg_validation(self):
        try:
            success_massage=self.driver.find_element(By.XPATH,self.success_msg_xpath).text
            return success_massage
        except:
            pass


