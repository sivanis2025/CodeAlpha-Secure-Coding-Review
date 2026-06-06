# Secure Coding Review Report

## CodeAlpha Internship - Task 3

### Project Information

**Project Title:** Secure Coding Review of a Python Login Application

**Programming Language:** Python

**Application Type:** Login System

**Review Method:** Manual Code Review and Bandit Static Analysis Tool

**Tool Used:** Bandit

**Reviewer:** Sivani Senthilkumar

---

# 1. Introduction

Secure coding is an essential practice in software development that helps protect applications from security vulnerabilities and cyberattacks. The purpose of this project is to review a Python-based login application, identify potential security weaknesses, and implement secure coding practices to mitigate those risks.

This review focuses on detecting common vulnerabilities such as SQL Injection and improving the overall security of the application through secure coding techniques.

---

# 2. Objective

The objectives of this secure coding review are:

* Identify security vulnerabilities in the application.
* Analyze the risks associated with the vulnerabilities.
* Recommend appropriate remediation measures.
* Implement secure coding practices.
* Verify improvements using a static analysis tool.

---

# 3. Application Overview

The application is a simple Python login system that accepts a username and password from the user and validates the credentials against a database.

Two versions of the application were reviewed:

1. Vulnerable Version (`vulnerable_app.py`)
2. Secure Version (`secure_app.py`)

---

# 4. Vulnerability Assessment

## Vulnerability Identified: SQL Injection

### Vulnerable Code

```python
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
```

### Description

The application directly concatenates user input into the SQL query. An attacker can manipulate the query by inserting malicious SQL statements through the input fields.

### Risk Level

Medium

### CWE Reference

CWE-89: SQL Injection

### Potential Impact

* Unauthorized database access
* Authentication bypass
* Data leakage
* Database manipulation
* Compromise of sensitive information

---

# 5. Static Analysis Results

## Vulnerable Application Analysis

### Tool Used

Bandit Static Analysis Tool

### Result

Bandit detected a possible SQL Injection vulnerability.

**Issue Identified:**

* B608: Hardcoded SQL Expressions
* Possible SQL Injection vector through string-based query construction.

### Severity

Medium

### Confidence

Low

---

## Secure Application Analysis

### Security Improvements Implemented

* Parameterized SQL Queries
* Password Hashing using SHA-256
* Input Validation

### Result

After implementing secure coding practices, the application was scanned again using Bandit.

**Bandit Output:**

```text
No issues identified.
```

### Severity

None

### Confidence

No vulnerabilities detected.

---

# 6. Remediation Measures

The following remediation measures were implemented to improve application security:

## 6.1 Parameterized Queries

### Before

```python
query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"
```

### After

```python
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, hashed_password))
```

### Benefit

Prevents SQL Injection attacks by separating user input from SQL commands.

---

## 6.2 Password Hashing

### Implementation

```python
hashed_password = hashlib.sha256(password.encode()).hexdigest()
```

### Benefit

Protects passwords from being exposed in plaintext if the database is compromised.

---

## 6.3 Input Validation

### Implementation

```python
if not username or not password:
    print("Username and password cannot be empty")
```

### Benefit

Prevents invalid or empty user input from being processed.

---

# 7. Best Practices Followed

The following secure coding best practices were applied:

* Avoid direct SQL query concatenation.
* Use parameterized queries.
* Hash sensitive information such as passwords.
* Validate all user input.
* Perform regular code reviews.
* Use automated security analysis tools.
* Follow OWASP Secure Coding Guidelines.

---

# 8. Comparison of Results

| Feature                  | Vulnerable Application | Secure Application |
| ------------------------ | ---------------------- | ------------------ |
| SQL Injection Protection | No                     | Yes                |
| Password Hashing         | No                     | Yes                |
| Input Validation         | No                     | Yes                |
| Bandit Security Issues   | 1 Detected             | 0 Detected         |
| Security Level           | Vulnerable             | Improved           |

---

# 9. Conclusion

The secure coding review successfully identified an SQL Injection vulnerability in the Python login application. Through the implementation of parameterized queries, password hashing, and input validation, the identified vulnerability was mitigated.

Static analysis using the Bandit tool confirmed that the secure version of the application contained no detectable security issues. This project demonstrates the importance of secure coding practices in developing secure and reliable software applications.

---

# 10. References

1. OWASP Secure Coding Practices
2. OWASP Top 10 Security Risks
3. CWE-89: SQL Injection
4. Python Documentation
5. Bandit Documentation

---

**End of Report**
