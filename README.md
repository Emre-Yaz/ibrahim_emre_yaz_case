# QA Engineer – Selenium Task

This project automates a UI flow on https://useinsider.com/ using Python and Selenium. The goal is to showcase not only functional correctness, but also engineering practices.

---

## 🚀 Features & Goals

✅ Page Object Model (POM) architecture  
✅ Robust CSS/XPath selectors  
✅ Clean assertions and error messages  
✅ Logging and screenshot capture on failure  
✅ HTML test report

---

## 🧪 Test Coverage

### ✅ Steps Implemented

1. Visit `https://useinsider.com/` and check homepage is loaded
2. Navigate to Company → Careers and verify:
   - Career page URL
   - Presence of Locations, Teams, and Life at Insider sections
3. Visit QA-specific job page and filter jobs by:
   - Location: `Istanbul, Turkiye`
   - Department: `Quality Assurance`
4. Validate all job cards have correct:
   - Position → includes `Quality Assurance`
   - Department → `Quality Assurance`
   - Location → `Istanbul, Turkiye`
5. Click `View Role` and confirm redirect to Lever application page

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

## 📸 Extras

- Screenshots: On any test failure, a screenshot is saved in /screenshots with a timestamp.
- Logging: Actions and errors are logged for traceability.
- Clean selectors: Carefully chosen XPaths and CSS for robustness against layout change

## 🙋 About Me

- QA Engineer with a passion for automation, product quality, and engineering best practices

## 📫 Contact

Feel free to reach me at: ibrahimemreyaz@gmail.com
