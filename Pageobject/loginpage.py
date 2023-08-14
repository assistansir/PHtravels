from selenium.webdriver.common.by import By


class travels:

    Text_Email_XPATH = (By.XPATH,"//input[@id='email']")
    Text_Password_XPATH = (By.XPATH,"//input[@id='password']")
    CLICK_CITY_XPATH =(By.XPATH,"//div[@class='filter-option']")
    CLICK_English_City_XPATH =(By.XPATH,"//a[@id='bs-select-1-0']")
    CLICK_Login_Button_XPATH =(By.XPATH,"//button[@id='submit']")
    Sucess_Massage_XPATH =(By.XPATH,"//a[@class='loadeffect d-flex align-items-center link-light text-decoration-none gap-2']//img")
    CLICK_Admin_button_XPATH = (By.XPATH, "//a[@id='dropdownUser1']")
    Click_Logout_XPATH = (By.XPATH, "//a[normalize-space()='Logout']")
    Logout_sussecful_massage_XPATH = (By.XPATH, "//img[@alt='favicon']")



    def __init__(self,driver):
        self.driver = driver

    def LOGIN(self):
        self.driver.get("https://phptravels.net/admin/login.php")


    def Enter_Email(self,email):
        self.driver.find_element(*travels.Text_Email_XPATH).send_keys(email)


    def Enter_Password(self,password):
        self.driver.find_element(*travels.Text_Password_XPATH).send_keys(password)


    def click_city(self):
        self.driver.find_element(*travels.CLICK_CITY_XPATH).click()

    def click_english(self):
        self.driver.find_element(*travels.CLICK_English_City_XPATH).click()


    def click_login_button(self):
        self.driver.find_element(*travels.CLICK_Login_Button_XPATH).click()

    def click_admin(self):
        self.driver.find_element(*travels.CLICK_Admin_button_XPATH).click()


    def click_logout(self):
        self.driver.find_element(*travels.Click_Logout_XPATH).click()



    def Logout_Status(self):
        try:
            self.driver.find_element(*travels.Logout_sussecful_massage_XPATH)
            return True
        except:
            return False






