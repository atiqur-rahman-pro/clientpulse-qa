# ClientPulse QA - Executive Testing & Assurance Hub ⚡

A client-focused **Automated Testing, Quality Assurance & Executive Reporting Platform** built with **Python, FastAPI, Pytest, Modern Glassmorphism Dashboard UI**, and **Jenkins CI/CD Pipeline**.

---

## 🌟 Key Features

1. **Client Executive Dashboard**: Real-time pass/fail rates, response latency metrics, and test execution details.
2. **Automated Pytest Engine**: Unit, API health check, and E2E regression test suites.
3. **Exportable Audit Reports**: One-click printable/downloadable Executive HTML Audit Report.
4. **Jenkins CI/CD Integration**: Fully compatible Jenkinsfile for automated regression testing on every commit.

---

## 🚀 Quick Start

### 1. Local Run
```bash
# Install dependencies
pip install -r requirements.txt

# Run FastAPI Server
python -m uvicorn main:app --reload --port 8000
```
Open **`http://localhost:8000`** in your browser!

### 2. Run Tests
```bash
python -m pytest
```

### 3. Run via Docker
```bash
docker build -t clientpulse-qa .
docker run -p 8000:8000 clientpulse-qa
```
