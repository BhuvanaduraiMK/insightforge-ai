<h1 align="center">🚀 InsightsForge AI</h1>

<h3 align="center">
AI-Powered Business Intelligence & Data Analysis Platform
</h3>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=24&duration=3000&pause=1000&center=true&vCenter=true&width=800&lines=AI+Business+Analyst;Data+Analysis+Platform;Automated+Business+Insights;AI-Powered+CSV+Analysis;FastAPI+%7C+React+%7C+Gemini+AI" />
</p>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white"/>

<img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>

<img src="https://img.shields.io/badge/React-Frontend-61DAFB?style=for-the-badge&logo=react&logoColor=black"/>

<img src="https://img.shields.io/badge/PostgreSQL-Database-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>

<img src="https://img.shields.io/badge/Gemini-AI-8E75B2?style=for-the-badge&logo=google&logoColor=white"/>

<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white"/>

</p>

<p align="center">

<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge"/>

<img src="https://img.shields.io/badge/Project-AI%20%7C%20Data%20Analytics-blue?style=for-the-badge"/>

<img src="https://img.shields.io/github/license/BhuvanaduraiMK/AI-Business-Analysis?style=for-the-badge"/>

</p>

---

# 📌 Project Overview

**InsightsForge AI** is an AI-powered Business Intelligence and Data Analysis platform designed to transform raw CSV datasets into meaningful business insights.

The platform allows users to upload a dataset and automatically performs:

- 📊 Dataset profiling
- 🧹 Data quality analysis
- 📈 KPI generation
- 💡 Business insight generation
- 🔗 Correlation analysis
- 📦 Outlier detection
- 📊 Automatic chart generation
- 📋 Business dashboard generation
- 🤖 AI-powered business questions
- 💬 Natural-language dataset Q&A
- 📄 Business report generation
- 📑 PDF report export

Instead of manually performing the same exploratory analysis for every dataset, InsightsForge AI automates the initial business-analysis workflow.

---

# 🎯 Problem Statement

Business users often receive raw datasets without knowing:

- How clean the data is
- Which metrics are important
- Which categories perform better
- Whether unusual values exist
- Which variables are correlated
- What business questions should be asked
- How to convert analysis into a professional report

Traditional analysis requires manually performing these steps using tools such as Excel, SQL, Python, or Power BI.

**InsightsForge AI aims to automate this first-level analysis process.**

---

# 💡 Solution

InsightsForge AI provides a single workflow:

```text
CSV Dataset
     │
     ▼
Dataset Upload
     │
     ▼
Data Profiling
     │
     ├── Dataset Structure
     ├── Missing Values
     ├── Duplicate Rows
     ├── Data Types
     └── Statistical Summary
     │
     ▼
Data Quality Analysis
     │
     ▼
Automatic KPI Generation
     │
     ▼
Business Insights
     │
     ├── Numeric Analysis
     ├── Category Analysis
     ├── Correlation Analysis
     └── Outlier Detection
     │
     ▼
Dashboard & Visualizations
     │
     ├── Bar Charts
     ├── Histograms
     └── Box Plots
     │
     ▼
Gemini AI
     │
     ├── Suggested Questions
     └── Dataset Q&A
     │
     ▼
Business Report
     │
     ▼
PDF Export

```

---

## 📌 About The Project

**InsightForge AI** is an AI-driven data analytics platform built to turn raw, messy business data into clear, actionable insights — without requiring users to write a single line of code.

Upload a spreadsheet, and InsightForge AI automatically cleans the data, computes key business metrics, generates interactive dashboards, and lets you *ask questions in plain English* to get instant answers powered by AI.

> 💡 Built for analysts, founders, and teams who want fast, data-driven decisions without a dedicated BI engineer.

---

## ✨ Key Features

- 📁 **Upload CSV / Excel** — bring your own data, no setup required
- 🧹 **Automated Data Cleaning** — handles missing values, duplicates, and formatting issues
- 🗄️ **PostgreSQL Storage** — structured, queryable, and persistent
- 📊 **KPI Generation** — auto-computed business metrics from your dataset
- 📈 **Interactive Dashboards** — visualize trends at a glance
- 🤖 **AI Question Answering** — ask questions about your data in natural language
- 📝 **Business Report Generation** — auto-written summaries of your data
- 📄 **PDF Export** — share polished reports with stakeholders
- 🐳 **Dockerized** — consistent setup across environments

---

## 🛠️ Tech Stack

<p>
<img src="https://skillicons.dev/icons?i=python,fastapi,postgresql,docker,git,github"/>
</p>

| Layer | Technology |
|---|---|
| **Backend** | Python, FastAPI |
| **Database** | PostgreSQL |
| **Data Processing** | Pandas, NumPy |
| **AI / NLP** | LLM-based Q&A engine |
| **Reporting** | PDF generation |
| **Deployment** | Docker |
| **Version Control** | Git & GitHub |

---

## 🏗️ Project Architecture

```
User Upload (CSV/Excel)
        │
        ▼
  Data Cleaning Layer
        │
        ▼
  PostgreSQL Storage
        │
        ▼
  KPI & Insight Engine ──► AI Q&A Module
        │
        ▼
  Dashboard + PDF Report
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL
- Docker (optional, recommended)

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/your-username/insightforge-ai.git
cd insightforge-ai

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up environment variables
cp .env.example .env
# then fill in your DATABASE_URL and API keys

# 5. Run database migrations (if applicable)
alembic upgrade head

# 6. Start the FastAPI server
uvicorn app.main:app --reload
```

### Run with Docker

```bash
docker-compose up --build
```

The API will be available at `http://localhost:8000`, with interactive docs at `http://localhost:8000/docs`.

---

## 📂 Project Structure

```
insightforge-ai/
├── app/
│   ├── main.py              # FastAPI entry point
│   ├── routers/              # API endpoints
│   ├── services/              # Data cleaning, KPI, AI logic
│   ├── models/                 # Database models
│   └── schemas/                 # Pydantic schemas
├── data/                       # Sample datasets
├── reports/                     # Generated PDF reports
├── tests/                        # Unit tests
├── requirements.txt
├── docker-compose.yml
└── README.md
```

---

## 🗺️ Roadmap

- [x] CSV/Excel upload & cleaning pipeline
- [x] PostgreSQL integration
- [x] KPI generation engine
- [ ] Interactive dashboard UI
- [ ] AI-powered natural language Q&A
- [ ] Automated business report generation
- [ ] PDF export
- [ ] User authentication & multi-tenant support

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/your-feature`)
3. Commit your changes (`git commit -m 'Add your feature'`)
4. Push to the branch (`git push origin feature/your-feature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## 📬 Contact

**Bhuvanadurai M**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/bhuvanadurai-m-1312a7248/)

---

<p align="center">
⭐ If you find this project useful, consider giving it a star! ⭐
</p>
