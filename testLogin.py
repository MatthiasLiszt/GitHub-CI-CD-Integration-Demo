import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    # SETUP: Configure Chrome to run without a UI (Headless)
    chrome_options = Options()
    chrome_options.add_argument("--headless") 
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    # TEARDOWN: Close browser after each test
    driver.quit()

# We use @pytest.mark.parametrize to run the same logic with different data
@pytest.mark.parametrize("user, pwd, expected_status", [
    ("standard_user", "secret_sauce", "success"),
    ("locked_out_user", "secret_sauce", "blocked"),
    ("problem_user", "secret_sauce", "success"),
    ("performance_glitch_user", "secret_sauce", "success"),
    ("wrong_user", "secret_sauce", "fail"),
    ("standard_user", "wrong_pass", "fail"),
])
def test_sauce_demo_login(driver, user, pwd, expected_status):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    
    # Locate and interact
    driver.find_element(By.ID, "user-name").send_keys(user)
    driver.find_element(By.ID, "password").send_keys(pwd)
    driver.find_element(By.ID, "login-button").click()

    if expected_status == "success":
        # Assert we reached the inventory page
        wait.until(EC.url_contains("inventory.html"))
        assert "inventory.html" in driver.current_url
        
    elif expected_status == "blocked":
        error_msg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
        assert "locked out" in error_msg.text.lower()
        
    elif expected_status == "fail":
        error_msg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
        assert "Username and password do not match" in error_msg.text
