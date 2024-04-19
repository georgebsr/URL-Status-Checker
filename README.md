# URL Status Checker

## Introduction

URL Status Checker is a Python script designed to automate the task of checking the status codes of URLs listed in an Excel file. I wrote this script to help me automate some tasks in my job. It can be useful for tasks such as data analysis, quality assurance, or any scenario where validating URLs is necessary.

## Features

- **Reads URLs from Excel**: Utilizes the Pandas library to read URLs from an Excel file.
- **Checks URL Status Codes**: Makes HTTP HEAD requests to each URL to determine its status code.
- **Error Handling**: Handles exceptions gracefully and provides informative error messages.
- **Exports Results**: Generates a new Excel file containing the URLs and their corresponding status codes.

## Requirements

- Python 3.x
- Pandas library
- Requests library

## Usage

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/georgebsr/URL-Status-Checker


2. **Navigate to the Project Directory:**
    ```bash
    cd url-status-checker

3. **Install Dependencies:**
    ```bash
    pip install pandas requests

4. **Run the Script:**
    ```bash
    python url_status_checker.py

# Example

Suppose you have an Excel file named `url_list.xlsx` with a column named `URLs` containing the URLs to be checked. You can use URL Status Checker to verify the status codes as follows:

    ```bash
    python url_status_checker.py
 After execution, the script will create a new Excel file named url_status_results.xlsx containing the URLs along with their corresponding status codes.

