import time

import allure
from allure_commons.types import AttachmentType

from Pageobject.loginpage import travels


class Test_login:
    def test_login_001(self,setup):
        self.driver = setup
        self.tr = travels(self.driver)
        self.tr.LOGIN()
        self.tr.Enter_Email("admin@phptravels.com")
        self.tr.Enter_Password("demoadmin")
        self.tr.click_city()
        self.tr.click_english()
        self.tr.click_login_button()
        self.tr.click_admin()
        self.tr.click_logout()
        if self.tr.Logout_Status()== True:
            assert True
            allure.attach(self.driver.get_screenshot_as_png(),name="test_login_001",attachment_type=AttachmentType.PNG)
            self.driver.save_screenshot("D:\\PHtravels\\screenshoot\\test_login_001_Pass.PNG")
        else:
            self.driver.save_screenshot("D:\\PHtravels\\screenshoot\\test_login_001_Fail.PNG")
            assert False
