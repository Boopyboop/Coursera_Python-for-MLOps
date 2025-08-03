# Python Essentials for MLOps  
## Module 3: Testing with Pytest

> 🧪 **This repository is my personal workspace for experimenting with the code and concepts taught in the course **Python Essentials for MLOps  
[https://www.coursera.org/learn/python-mlops-duke](https://www.coursera.org/learn/python-mlops-duke) It is not an official or production-ready project.**

### Module 3: Testing with Pytest** available on Coursera:  

---

## 📚 What I'm Exploring

This module focuses on using `pytest` to write clean, maintainable, and robust tests in Python—an essential skill for MLOps pipelines and production-ready machine learning systems.

---

## 🚀 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/your-username/python-essentials-mlops-module3.git
cd python-essentials-mlops-module3
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
```

---

## 🧪 Running Tests

Run all tests:

```bash
pytest
```

Run a specific file:

```bash
pytest test_failure_output.py
```

Stop at the first failure:

```bash
pytest -x
```

Just show what would run (without executing):

```bash
pytest --collect-only
```

Run in parallel (requires `pytest-xdist`):

```bash
pytest -n 4
```

---

## 🔧 Tools and Plugins

- [`pytest`](https://docs.pytest.org/)
- [`pytest-xdist`](https://pypi.org/project/pytest-xdist/)

---

## 📌 Disclaimer

This repository is **not a complete or polished project**. It is a sandbox for learning, testing, and exploring concepts from the **Python Essentials for MLOps – Module 3** course.

---

## 🧭 Module 5: Applied Python for MLOps

This module explores how to integrate Python scripts with Azure Machine Learning resources using the SDK. It focuses on connecting securely to the Azure ML Workspace from Python using environment variables and service principal authentication.

### 🧪 What’s Implemented

- Script to authenticate and connect to Azure ML Workspace using:
  - `ServicePrincipalAuthentication` from `azureml-core`
  - Credentials securely loaded via `python-dotenv`
- `.env` file structure (not included in repo):
  ```ini
  AZURE_SUBSCRIPTION_ID=...
  AZURE_TENANT_ID=...
  AZURE_CLIENT_ID=...
  AZURE_CLIENT_SECRET=...
  ```
- Workspace details:
  - Resource Group: `rg-mlopsclass-we-dev`
  - Workspace Name: `ws-mlopsclass-we-dev`

### 📁 Directory

```
Module5_appliedPythonForMLOps/
├── connect_workspace.py
```


## 📌 Disclaimer

This repository is **not a complete or polished project**. It is a sandbox for learning, testing, and exploring concepts from the **Python Essentials for MLOps – Module 3** course.

---
