from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_login_page(driver):
    driver.get("https://softwaretestingv1.praesignis.com/softwaretestingv1/Login_Page.html")
    wait = WebDriverWait(driver, 20)

    # Wait for username field
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    # Use JavaScript to set username
    driver.execute_script("arguments[0].value='anginni81@gmail.com';", username_field)

    # Wait for password field
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    # Use JavaScript to set password
    driver.execute_script("arguments[0].value='Anginni@81@';", password_field)

    # Click login button
    login_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Login']")))
    login_button.click()

    # Wait for URL redirection
    wait.until(EC.url_contains("dashboard"))  # replace "dashboard" with actual URL fragment

    print("Login test passed! Redirected to:", driver.current_url)

# Run the test
driver = webdriver.Chrome()
test_login_page(driver)
driver.quit()
