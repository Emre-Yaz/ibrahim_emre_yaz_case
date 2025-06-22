# QA Engineer – Selenium Task

This project automates a UI flow on https://useinsider.com/ using Python and Selenium, following the Page Object Model (POM). It includes reliable UI interaction, filtering validations, Lever redirection testing, and Sphinx-based documentation generation. The goal is to showcase not only functional correctness, but also engineering practices.

---

## 🚀 Features & Goals

✅ Page Object Model (POM) architecture  
✅ Robust CSS/XPath selectors  
✅ Clean assertions and error messages  
✅ Logging and screenshot capture on failure  
✅ Test report & Sphinx documentation

✅ Tab switching and redirect assertion

---

## 🛠️ Setup & Installation

### 1. Clone the repository

```bash
git clone https://github.com/Emre-Yaz/ibrahim_emre_yaz_case.git
cd ibrahim_emre_yaz_case
```

### 2. Create and activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## ▶️ Running the Tests

### Basic execution

```bash
pytest
```

### With HTML report (requires pytest-html)

```bash
pytest --html=report.html --self-contained-html
```

### Running with different browsers and modes

You can configure the browser and headless mode via command-line options:

| Option              | Description                        |
| ------------------- | ---------------------------------- |
| `--browser=chrome`  | (default) Run in Chrome            |
| `--browser=firefox` | Run in Firefox                     |
| `--headless`        | Run without opening browser window |

```bash
# Run in headless Chrome
pytest --headless

# Run in Firefox (headed)
pytest --browser=firefox

# Run in headless Firefox with HTML report
pytest --browser=firefox --headless --html=report.html --self-contained-html
```

## 📸 Extras

- Screenshots: On any test failure, a screenshot is saved in /screenshots with a timestamp.
- Logging: Actions and errors are logged for traceability.
- Clean selectors: Carefully chosen XPaths and CSS for robustness against layout change

## 🙋 About Me

- QA Engineer with a passion for automation, product quality, and engineering best practices

## 📫 Contact

Feel free to reach me at: ibrahimemreyaz@gmail.com
