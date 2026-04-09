from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Open browser
driver = webdriver.Chrome()
driver.maximize_window()

# Open website
driver.get("https://automationexercise.com/")

# Wait setup
wait = WebDriverWait(driver, 10)

# Click Signup/Login button
wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//a[contains(text(),'Signup / Login')]"))
).click()

# Enter Email (Login section - second email field)
wait.until(EC.visibility_of_all_elements_located(
    (By.NAME, "email"))
)[1].send_keys("your_email@example.com")

# Enter Password
driver.find_element(By.NAME, "password").send_keys("yourpassword")

# Click Login button
driver.find_element(By.XPATH, "//button[text()='Login']").click()

# Verify Login
try:
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//*[contains(text(),'Logged in as')]")
    ))
    print("Test Passed ✅ - Login Successful")
except:
    print("Test Failed ❌ - Login Unsuccessful")

# Close browser
driver.quit()
