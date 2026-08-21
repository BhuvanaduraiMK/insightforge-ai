<div align="center">

# 🚀 InsightForge AI

### AI-Powered Business Intelligence Assistant

<p>
  <strong>Upload • Analyze • Visualize • Understand • Ask AI</strong>
</p>

<p>
  <img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=24&duration=3000&pause=800&color=0E75B6&center=true&vCenter=true&width=750&lines=AI+Business+Intelligence+Assistant;Automated+Data+Analysis;Dynamic+KPI+Generation;Business+Insights+%26+Visualization;Gemini-Powered+Dataset+Q%26A;Automated+PDF+Business+Reports" />
</p>

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB"/>
  <img src="https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white"/>
  <img src="https://img.shields.io/badge/Google%20Gemini-8E75B2?style=for-the-badge&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/ReportLab-FF6F00?style=for-the-badge"/>
</p>

<p>
  <a href="https://github.com/BhuvanaduraiMK">
    <img src="https://img.shields.io/badge/GitHub-BhuvanaduraiMK-181717?style=for-the-badge&logo=github"/>
  </a>
  <a href="https://www.linkedin.com/in/bhuvanadurai-m-1312a7248/">
    <img src="https://img.shields.io/badge/LinkedIn-Bhuvanadurai%20M-0077B5?style=for-the-badge&logo=linkedin"/>
  </a>
</p>

</div>

---

# 📌 About the Project

**InsightForge AI** is a full-stack **AI-powered Business Intelligence Assistant** that transforms raw CSV datasets into meaningful business insights.

Instead of manually performing repetitive data analysis, users can upload a dataset and automatically receive:

- 📊 Dataset profiling
- 🧹 Data cleaning
- 📈 KPI generation
- 💡 Business insights
- 📉 Correlation analysis
- 🔎 Outlier detection
- 📊 Data visualizations
- 📄 Automated PDF reports
- 🤖 AI-generated business questions
- 💬 Gemini-powered dataset Q&A

The goal of the project is to combine **Data Analytics + Backend Engineering + Generative AI** into one practical business intelligence platform.

---

# 🎯 Project Objective

Traditional data analysis often requires users to manually:

1. Inspect datasets
2. Clean missing values
3. Calculate statistics
4. Identify business KPIs
5. Analyze relationships
6. Detect outliers
7. Create visualizations
8. Prepare reports
9. Interpret the results

InsightForge AI automates these steps through a single web application.

### Simple workflow

```text
        CSV Dataset
             │
             ▼
      ┌──────────────┐
      │ Data Upload  │
      └──────┬───────┘
             │
             ▼
     ┌─────────────────┐
     │ Data Processing │
     └────────┬────────┘
              │
      ┌───────┼────────┐
      ▼       ▼        ▼
    KPIs   Insights  Quality
      │       │        │
      └───────┼────────┘
              ▼
      ┌─────────────────┐
      │ Statistical     │
      │ Analysis        │
      └────────┬────────┘
               │
        ┌──────┼───────┐
        ▼      ▼       ▼
     Charts  PDF     Context
                       │
                       ▼
                 ┌──────────┐
                 │ Gemini AI │
                 └────┬─────┘
                      │
                      ▼
                  AI Q&A

```
Dashboard includes
| Section               | Purpose                                  |
| --------------------- | ---------------------------------------- |
| 📤 Dataset Upload     | Upload CSV data                          |
| 📊 KPI Cards          | Display important dataset metrics        |
| 💡 Business Insights  | Automatically generated observations     |
| 📈 Visual Analysis    | Histograms, bar charts and box plots     |
| 📄 Business Report    | Generate downloadable PDF                |
| ❓ Suggested Questions | AI-generated business questions          |
| 🤖 AI Q&A             | Ask questions about the uploaded dataset |




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
