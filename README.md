# Python Essentials for MLOps  
## Module 3: Testing with Pytest

> 🧪 **This repository is my personal workspace for experimenting with the code and concepts taught in the course **Python Essentials for MLOps - Module 3: Testing with Pytest** available on Coursera:  
[https://www.coursera.org/learn/python-mlops-duke](https://www.coursera.org/learn/python-mlops-duke) It is not an official or production-ready project.**

---

## 📚 What I'm Exploring

This module focuses on using `pytest` to write clean, maintainable, and robust tests in Python—an essential skill for MLOps pipelines and production-ready machine learning systems.

Topics covered:

- ✅ Writing simple and expressive unit tests with `pytest`
- 🧱 Using test functions and test classes
- 🔁 Setup and teardown methods for test environments
- 🧩 Pytest fixtures for reusable, isolated logic
- 🐞 Reading and interpreting test failure outputs
- ⚙️ Useful `pytest` CLI flags and tools
- ⚡ Running tests in parallel with `pytest-xdist`

---

## 📁 Project Layout

```bash
.
├── utils.py                  # Utility functions (e.g., string_to_int)
├── test_failure_output.py   # Intentional test failures to analyze output
├── test_classes.py          # Using classes, setup/teardown
├── test_fixtures.py         # Using pytest fixtures
├── requirements.txt         # Dependencies
└── README.md                # This file
```

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
