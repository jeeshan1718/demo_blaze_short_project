import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    options = Options()
    options.add_argument("--headless")          # 👈 main cheez
    options.add_argument("--disable-gpu")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    driver.get("https://www.demoblaze.com")
    yield driver
    driver.quit()
