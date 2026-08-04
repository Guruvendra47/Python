# Windows Python Installation Guide

## Project Overview

This repository provides a comprehensive guide for installing and configuring Python on Windows. It covers downloading the official Python distribution, configuring environment variables, verifying the installation, creating virtual environments, and integrating Python with Visual Studio Code.

The objective is to establish a standardized Python development environment for software development, data engineering, automation, and machine learning projects.

---

# Objectives

This guide enables users to:

- Install Python on Windows
- Configure Python and pip
- Set up environment variables
- Create isolated virtual environments
- Configure Visual Studio Code for Python development
- Troubleshoot common installation issues

---

# Prerequisites

- Windows 10 or Windows 11
- Administrator privileges (optional)
- Internet connection

---

# Installation Workflow

```

Download Python

↓

Run Installer

↓

Add Python to PATH

↓

Verify Installation

↓

Upgrade pip

↓

Create Virtual Environment

↓

Configure VS Code

````

---

# Installation Steps

## 1. Download Python

Download the latest stable release from the official Python website.

https://www.python.org/downloads/windows/

---

## 2. Install Python

- Run the installer
- Enable **Add Python to PATH**
- Install Python
- Verify successful installation

---

## 3. Verify Installation

```bash
python --version
pip --version
````

---

## 4. Create a Virtual Environment

```bash
python -m venv .venv
```

Activate the environment:

PowerShell

```powershell
.\.venv\Scripts\Activate.ps1
```

Command Prompt

```cmd
.\.venv\Scripts\activate.bat
```

---

## 5. Configure Visual Studio Code

* Install VS Code
* Install the Python extension
* Select the virtual environment interpreter
* Run Python applications

---

# Repository Structure

```
Python-Installation-Guide/
│
├── Installation Guide.md
├── Screenshots/
├── Commands/
└── README.md
```

---

# Technologies Used

| Category               | Technology         |
| ---------------------- | ------------------ |
| Programming Language   | Python             |
| IDE                    | Visual Studio Code |
| Operating System       | Windows 10/11      |
| Package Manager        | pip                |
| Environment Management | venv               |

---

# Skills Demonstrated

* Python Installation
* Environment Configuration
* Package Management
* Virtual Environment Setup
* Development Environment Configuration

---

# Learning Outcomes

After following this guide, users will be able to:

* Install Python correctly
* Configure system environment variables
* Manage Python packages using pip
* Create isolated virtual environments
* Configure Visual Studio Code for Python development

---

# Author

**Guruvendra Singh**

Data Engineering | Python | SQL | Snowflake | AWS | ETL | Automation


