# 🧠 Multi-Agent AI Code Review System

A **Multi-Agent AI Code Review System** developed as a final project for **SEN0414 – Advanced Programming**.  
The system automatically analyzes Python source code and generates structured, explainable review feedback using a collaborative multi-agent architecture.

---

## 📌 Project Overview

Code review is a fundamental activity in software engineering, yet manual reviews are often time-consuming and inconsistent.  
This project demonstrates how **AI for Software Engineering (AI4SE)** principles can be applied to automate and support the code review process in an **educational and explainable** manner.

The system analyzes Python code using **deterministic static analysis techniques** and produces feedback related to:

- Code quality
- Security risks
- Performance issues
- Refactoring suggestions

Each responsibility is handled by a **specialized analysis agent**, coordinated through a central orchestrator.

---

## 🏗️ System Architecture

The system follows a **collaborative multi-agent architecture** consisting of:

- **Coordinator Agent** – Orchestrates analysis and aggregates results
- **Quality Agent** – Detects style, formatting, and maintainability issues
- **Security Agent** – Identifies unsafe constructs (e.g., `eval`, `exec`)
- **Performance Agent** – Flags inefficient patterns such as nested loops
- **Refactoring Agent** – Provides improvement suggestions based on best practices

The backend is implemented using **FastAPI**, and results are presented through a **lightweight web interface**.

---

## 🛠️ Technology Stack

| Category             | Technology                  |
| -------------------- | --------------------------- |
| Programming Language | Python 3.11                 |
| Backend Framework    | FastAPI                     |
| Static Analysis      | Python AST, heuristic rules |
| Testing Framework    | pytest, pytest-cov          |
| Frontend             | HTML, CSS, JavaScript       |

> ⚠️ This prototype does **not** rely on external LLM APIs, databases, or repository integrations in order to ensure deterministic and explainable behavior.

---

## 📂 Project Structure

multi_agent_code_review1/
│
├── app/
│ ├── agents/
│ │ ├── base.py
│ │ ├── quality.py
│ │ ├── security.py
│ │ ├── performance.py
│ │ └── refactor.py
│ ├── coordinator.py
│ ├── main.py
│ └── schemas.py
│
├── tests/
│ ├── test_agents.py
│ ├── test_api.py
│ └── ...
│
├── web/
│ ├── index.html
│ ├── styles.css
│ └── app.js
│
├── requirements.txt
└── README.md

---

## 🚀 Installation & Usage

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/justsevval/multi_agent_code_review.git
cd multi_agent_code_review

2️⃣ Create & Activate Virtual Environment
python -m venv venv
venv\Scripts\activate      # Windows
# source venv/bin/activate # Linux / macOS

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Backend Server
uvicorn app.main:app --reload

5️⃣ Open Web Interface
cpp
http://127.0.0.1:8000
Paste Python code into the interface and click Analyze to view the review results.

🔌 API Usage
POST /review
Analyzes a Python code snippet and returns detected issues.

Request Example

json
{
  "code": "eval('2+2')"
}
Response Example

json
{
  "issues": [
    {
      "agent": "SecurityAgent",
      "message": "Use of eval detected",
      "severity": "high"
    }
  ]
}
🧪 Testing & Coverage
All system components are covered by automated tests.


Run tests with coverage:

python -m pytest --cov=app
📊 Test Coverage

Overall Coverage: 99%

All critical modules and agents are tested

📽 Demo Video
A demo video (5–8 minutes) demonstrating:

System architecture

Code analysis examples

Web interface usage

Test execution and coverage

🔗 Demo Video: https://youtu.be/oxDwFHncb_Y

🎓 Academic Context
Course: SEN0414 – Advanced Programming

Department: Computer Engineering

Institution: Istanbul Kültür University

Semester: Fall 2025

This project was developed as an educational prototype aligned with AI4SE principles.

📜 License
This project is intended for academic use only.

✨ Final Notes
This project demonstrates how multi-agent systems can be applied to software engineering tasks to improve consistency, reduce manual effort, and provide structured, explainable feedback for learning-oriented development.
```
