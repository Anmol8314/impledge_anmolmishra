from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time

# ✅ Correct Edge WebDriver path (Update if needed)
edge_driver_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"

# ✅ Setup Edge WebDriver
service = Service(edge_driver_path)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

# ✅ Configuration
BASE_URL = "https://ecspro-qa.kloudship.com"
USER_EMAIL = "kloudship.qa.automation@mailinator.com"
USER_PASSWORD = "Password1"

try:
    print("🚀 Starting automation...")

    # ✅ Step 1: Open KloudShip Login Page
    driver.get(BASE_URL)
    driver.maximize_window()

    # ✅ Step 2: Perform Login with Explicit Wait
    wait = WebDriverWait(driver, 15)

    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))
    password_field = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    email_field.clear()
    email_field.send_keys(USER_EMAIL)
    password_field.clear()
    password_field.send_keys(USER_PASSWORD)

    # ✅ Use JavaScript click if normal click doesn't work
    driver.execute_script("arguments[0].click();", login_button)
    
    print("✅ Login button clicked. Waiting for login confirmation...")

    # ✅ Wait for login success by checking redirection or a dashboard element
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Package Types")))
    print("✅ Logged in successfully.")

    # ✅ Step 3: Navigate to "Package Types"
    driver.find_element(By.LINK_TEXT, "Package Types").click()
    wait.until(EC.element_to_be_clickable((By.ID, "add-manually")))
    print("✅ Navigated to Package Types page.")

    # ✅ Step 4: Click on "Add Manually"
    driver.find_element(By.ID, "add-manually").click()
    wait.until(EC.presence_of_element_located((By.ID, "package-name")))
    print("✅ Opened Add Package Form.")

    # ✅ Step 5: Enter package details
    package_name = f"Package_{random.randint(1000, 9999)}"
    length = str(random.randint(5, 50))
    width = str(random.randint(5, 50))
    height = str(random.randint(5, 50))
    weight = str(random.randint(1, 20))

    driver.find_element(By.ID, "package-name").send_keys(package_name)
    driver.find_element(By.ID, "length").send_keys(length)
    driver.find_element(By.ID, "width").send_keys(width)
    driver.find_element(By.ID, "height").send_keys(height)
    driver.find_element(By.ID, "weight").send_keys(weight)

    print(f"✅ Entered package details: {package_name}, {length}x{width}x{height}, {weight}kg")

    # ✅ Step 6: Click Save and Verify
    driver.find_element(By.ID, "save-button").click()
    print("✅ Clicked Save button. Waiting for confirmation...")

    # ✅ Wait for confirmation message or package appearing in the list
    success_message = wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='success-message']"), "Package added successfully"))

    if success_message:
        print(f"🎉 Package '{package_name}' successfully added and verified!")

    # ✅ Step 7: Logout
    wait.until(EC.element_to_be_clickable((By.ID, "logout"))).click()
    print("✅ Logged out successfully.")

except Exception as e:
    print(f"❌ Test Failed: {e}")

finally:
    input("Press Enter to close Edge...")  # Keeps browser open for verification
    driver.quit()
