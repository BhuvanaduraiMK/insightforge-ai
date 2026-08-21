<h1 align="center">📊 InsightForge AI</h1>

<h3 align="center">
An AI-Powered Data Analytics Platform for Automated Insights & Business Reporting
</h3>

<p align="center">
<img src="https://readme-typing-svg.herokuapp.com?font=Poppins&size=22&duration=3500&pause=1000&center=true&vCenter=true&width=700&lines=AI-Powered+Data+Analytics;Automated+Insights+%26+Reporting;Built+with+FastAPI+%2B+Python;Turning+Raw+Data+into+Decisions" alt="Typing SVG" />
</p>

<p align="center">
<img src="https://img.shields.io/badge/Python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white"/>
<img src="https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white"/>
<img src="https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white"/>
<img src="https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge"/>
</p>

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
