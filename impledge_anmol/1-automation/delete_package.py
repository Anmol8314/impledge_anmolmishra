from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# ✅ Correct Edge WebDriver path (Change if needed)
edge_driver_path = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedgedriver.exe"

# ✅ Setup Edge WebDriver
service = Service(edge_driver_path)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

try:
    print("🚀 Starting package deletion automation...")

    # Step 1: Open KloudShip login page
    driver.get("https://ecspro-qa.kloudship.com")
    driver.maximize_window()

    # ✅ Wait for login elements
    wait = WebDriverWait(driver, 10)
    email_field = wait.until(EC.presence_of_element_located((By.ID, "email")))

    print("✅ Login page loaded successfully.")

    # Step 2: Perform Login
    email_field.send_keys("kloudship.qa.automation@mailinator.com")
    driver.find_element(By.ID, "password").send_keys("Password1")
    driver.find_element(By.ID, "login-button").click()

    # ✅ Wait until login completes
    wait.until(EC.presence_of_element_located((By.LINK_TEXT, "Package Types")))
    print("✅ Logged in successfully.")

    # Step 3: Navigate to "Package Types"
    driver.find_element(By.LINK_TEXT, "Package Types").click()
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "package-list")))
    print("✅ Navigated to Package Types page.")

    # Step 4: Find and Delete the Latest Package
    try:
        # Find the first (latest) package in the list
        package_row = wait.until(EC.presence_of_element_located((By.XPATH, "//table//tr[1]")))
        delete_button = package_row.find_element(By.CLASS_NAME, "delete-package-button")

        package_name = package_row.find_element(By.CLASS_NAME, "package-name").text
        print(f"🗑️ Deleting package: {package_name}")

        # Click Delete button
        delete_button.click()

        # Confirm deletion
        confirm_button = wait.until(EC.element_to_be_clickable((By.ID, "confirm-delete")))
        confirm_button.click()

        # ✅ Wait for deletion confirmation
        wait.until(EC.text_to_be_present_in_element((By.XPATH, "//div[@class='success-message']"), "Package deleted successfully"))
        print(f"✅ Package '{package_name}' successfully deleted!")

    except Exception as e:
        print("❌ No package found or deletion failed.")

    # Step 5: Logout
    wait.until(EC.element_to_be_clickable((By.ID, "logout"))).click()
    print("✅ Logged out successfully.")

except Exception as e:
    print(f"❌ Test Failed: {e}")

finally:
    input("Press Enter to close Edge...")  # Keeps browser open for verification
    driver.quit()
