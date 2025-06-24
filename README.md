# Selenium Automation Framework – Page Object Model

This project automates the order placement flow on [automationexercise.com](https://automationexercise.com) using:

- Selenium with Python
- Pytest for testing
- Page Object Model (POM) for maintainability
- HTML reporting with `pytest-html`

## Project Structure
AutomationProj/
├── pages/ # Page Object classes
├── tests/ # Pytest-based test cases
├── .gitignore
├── README.md
└── report.html # Generated HTML report (optional)

## How to Run

1. Create virtual environment and install dependencies:
   ```bash
   pip install selenium pytest pytest-html
   
## Run the test with report:
pytest tests/test_place_order.py --html=report.html

