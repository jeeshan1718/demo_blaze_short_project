from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    # Locators
    login_link = (By.ID, "login2")
    username_field = (By.ID, "loginusername")
    password_field = (By.ID, "loginpassword")
    login_button = (By.XPATH, "//button[text()='Log in']")
    welcome_user = (By.ID, "nameofuser")

    def __init__(self, driver):
        self.driver = driver

    def click_login_link(self):
        self.driver.find_element(*self.login_link).click()

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.username_field)
        ).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()

    def get_welcome_text(self):
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.welcome_user)
        ).text
