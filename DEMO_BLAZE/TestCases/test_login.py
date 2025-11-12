import pytest
from Pages.Login_page import LoginPage
import time

@pytest.mark.parametrize("username,password", [("Jeeshan1718", "kohli@1718")])
def test_valid_login(setup, username, password):
    driver = setup
    lp = LoginPage(driver)

    lp.click_login_link()
    lp.enter_username(username)
    lp.enter_password(password)
    lp.click_login_button()

    time.sleep(2)  # small wait for login to complete
    welcome_text = lp.get_welcome_text()

    assert username in welcome_text, "Login failed — Welcome text not found"
