# CodeAlpha Task 3 - Secure Coding Review

## Objective
Perform a security review of a Python login application and identify vulnerabilities.

## Tools Used
- Python
- SQLite3
- Bandit

## Vulnerabilities Found
- SQL Injection (CWE-89)

## Security Improvements
- Parameterized Queries
- Password Hashing (SHA-256)
- Input Validation

## Project Files
- vulnerable_app.py
- secure_app.py
- secure_coding_review_report.md

## Results

### Vulnerable Application
Bandit detected SQL Injection vulnerability.

### Secure Application
Bandit reported:
"No issues identified."

## Author
Sivani Senthilkumar