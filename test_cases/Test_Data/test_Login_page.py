import time

from PageObjects.Login_Page import Login_page
from PageObjects.Signup_Page import SignUp_Class


class Test_SignUp:

    def test_BankApp_url_001(self,setup):
        self.driver = setup
        if self.driver.title == "Bank Application":
            self.driver.save_screenshot(".\\ScreenShots\\main_page.jpg")
            time.sleep(2)
            assert True
        else:
            assert False

    def test_SignUp_002(self, setup):
        self.driver=setup
        self.su=SignUp_Class(self.driver)
        self.driver.save_screenshot(".\\ScreenShots\\signup_interface.jpg")
        self.su.SignUp_button()
        self.su.Enter_username("seusadcsar5bh")
        time.sleep(2)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        self.su.Enter_password("Sraafs4sfbh@1123")
        time.sleep(2)
        self.su.Enter_email("srasdeefbah1@gamail.com")
        time.sleep(2)
        self.su.Enter_phone("98465578811")
        self.su.Create_User_button()
        time.sleep(2)
        if self.su.success_msg_validation()=="User created successfully":
            self.driver.save_screenshot(".\\ScreenShots\\User creation.jpg")
            time.sleep(2)
            assert True
        else:
            assert False



    def test_Login_003(self, setup):
        self.driver=setup
        self.lp=Login_page(self.driver)
        self.lp.login_link()
        self.lp.username_text("Admin")
        self.lp.password_text("Admin@123")
        time.sleep(2)
        self.lp.click_login_button()
        time.sleep(2)
        if self.driver.title == "Dashboard":
            self.driver.save_screenshot(".\\ScreenShots\\login successfull.jpg")
            assert True
        else:
            assert False
            self.driver.save_screenshot(".\\ScreenShots\\login fail.jpg")