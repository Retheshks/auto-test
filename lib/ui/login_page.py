from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def get_username_textbox(self):
        try:
            un = self.driver.find_element_by_name('username')
            return un
        except:
            return None

    def get_password_textbox(self):
        try:
            return self.driver.find_element_by_name('pwd')
        except:
            return None

    def get_login_button(self):
        try:
            return self.driver.find_element_by_xpath("//input[@type='submit']")
        except:
            return None

    def wait_for_login_page_to_load(self):
        wait = WebDriverWait(driver=self.driver, timeout=30)
        wait.until(expected_conditions.visibility_of(self.get_username_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_password_textbox()))
        wait.until(expected_conditions.visibility_of(self.get_login_button()))


