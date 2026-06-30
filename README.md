# Attendance & Leave Management System - Selenium Automation

## Project Overview

This project automates the testing of a web-based Attendance & Leave Management System using Selenium WebDriver with Python.

The automation framework follows the Page Object Model (POM) design pattern and uses PyTest for test execution and pytest-html for report generation.

---

## Technologies Used

- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- HTML
- CSS
- JavaScript
- VS Code

---

## Features Tested

- ✅ Valid Login
- ✅ Invalid Login
- ✅ Empty Login Validation
- ✅ Mark Attendance
- ✅ Duplicate Attendance Prevention
- ✅ Apply Leave
- ✅ Leave Form Validation
- ✅ View Leave Status
- ✅ Admin Approval
- ✅ Logout Session Check

---

## Project Structure

```
AttendanceAutomation/
│
├── pages/
├── reports/
├── tests/
├── website/
├── conftest.py
└── README.md
```

---

## Test Cases

| Test Case | Status |
|-----------|--------|
| TC01 - Valid Login | ✅ Pass |
| TC02 - Invalid Login | ✅ Pass |
| TC03 - Empty Login | ✅ Pass |
| TC04 - Mark Attendance | ✅ Pass |
| TC05 - Duplicate Attendance | ✅ Pass |
| TC06 - Apply Leave | ✅ Pass |
| TC07 - Leave Validation | ✅ Pass |
| TC08 - View Leave Status | ✅ Pass |
| TC09 - Admin Approval | ✅ Pass |
| TC10 - Logout Session Check | ✅ Pass |

---

## Running the Project

Start the website using Live Server.

Run all automated tests:

```bash
pytest -v
```

Generate HTML Report:

```bash
pytest -v --html=reports/report.html --self-contained-html
```

---

## HTML Report

The project generates an HTML execution report showing the status of all automated test cases.

Result:

- Total Tests: 10
- Passed: 10
- Failed: 0

---

## Author

**Ananya**

B.Tech CSE  
KIIT University