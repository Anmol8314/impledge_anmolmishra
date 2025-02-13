KloudShip Automation Test Suite
Overview
This project automates test cases for KloudShip using Selenium (Python) for web automation, Postman for API testing, and SQL for database validation.

Technologies Used
Selenium WebDriver (Python)
Edge WebDriver
Postman for API testing
SQL for database queries
Exercise 1: Selenium Automation
Test Case 01: Add Package
Login with provided credentials.
Navigate to Package Types.
Click Add Manually and enter:
Name: FirstName_LastName
Dimensions: Random integer (< 20)
Logout and verify package is visible after re-login.
Test Case 02: Delete Package
Login and go to Package Types.
Delete the newly added package.
Logout and verify package is removed after re-login.
Exercise 2: Postman API Tests
Fix Failing Test Cases
Import Impledge_QA_Exercise.postman_collection.json into Postman.
Fix failing test cases.
New Request – Get Shipment Details
Fetch shipment details for shp_e0b570fd1d7d4b62bd206917eae5881a.
Add Test Cases
Verify selected_rate.retail_rate = 12.
Check retail_rate > list_rate.
Exercise 3: SQL Queries
Open SQL Practice and view schema.
Run these updates:
sql
Copy
Edit
UPDATE Admissions SET attending_doctor_id = 29 WHERE attending_doctor_id = 3;
UPDATE Admissions SET patient_id = 4 WHERE patient_id = 35;
Write queries to:
Get doctors with admissions.
Get doctors without admissions.
Get patients with missing doctor details.
How to Run
Selenium Tests
bash
Copy
Edit
pip install selenium  
python automation_test.py
Ensure Edge WebDriver is installed.

Postman & SQL
Import collection, fix tests, and add requests.
Execute SQL queries after updates.
Expected Outcomes
Selenium logs in, adds, and deletes packages successfully.
Postman returns correct shipment details and passes tests.
SQL queries fetch correct doctor & patient data.
Author
Anmol Mishra

