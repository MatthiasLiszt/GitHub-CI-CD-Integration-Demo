from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_sauce_demo_login(user, pwd):
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    
    try:
        driver.get("https://www.saucedemo.com/")
        
        # Locate elements
        user_input = wait.until(EC.presence_of_element_located((By.ID, "user-name")))
        pass_input = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.ID, "login-button")

        # Input credentials
        user_input.send_keys(user)
        pass_input.send_keys(pwd)
        login_btn.click()

        # Logic to check outcome
        if user == "locked_out_user":
            error_msg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
            print(f"[-] {user}: Blocked as expected. (Error: {error_msg.text})")
        
        elif "invalid" in user or pwd != "secret_sauce":
            error_msg = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3[data-test='error']")))
            print(f"[-] {user}: Failed login as expected. (Error: {error_msg.text})")
        
        else:
            wait.until(EC.url_contains("inventory.html"))
            print(f"[+] {user}: Login successful!")

    except Exception as e:
        print(f"[!] Error testing {user}: {str(e)[:50]}...")
    
    finally:
        driver.quit()

# --- Execution ---
valid_users = [
    "standard_user", 
    "locked_out_user", 
    "problem_user", 
    "performance_glitch_user"
]

test_cases = [
    ("wrong_user", "secret_sauce"),  # Unknown username
    ("standard_user", "wrong_pass"), # Wrong password
]

# Run through all scenarios
print("Starting Swag Labs Test Suite...\n" + "-"*30)

# Test Valid List
for username in valid_users:
    test_sauce_demo_login(username, "secret_sauce")

# Test Failure Scenarios
for username, password in test_cases:
    test_sauce_demo_login(username, password)