import os
import shutil
from datetime import datetime
from fastapi import Form

import pandas as pd
from fastapi import APIRouter, File, HTTPException, UploadFile
from app.services.profiling_service import profile_dataset
from app.services.cleaning_service import clean_dataset
from app.services.insights_service import generate_insights
from app.services.health_service import calculate_health_score
from app.services.correlation_service import correlation_analysis
from app.services.outlier_service import detect_outliers
from app.services.visualization_service import (
    generate_histogram,
    generate_bar_charts,
    generate_boxplot
)
from app.services.dashboard_service import generate_dashboard
from app.services.kpi_service import generate_kpis
#from app.services.qa_service import answer_question
from app.services.report_service import generate_report
from app.services.pdf_service import generate_pdf
from app.services.gemini_service import ask_gemini
from app.services.context_service import build_business_context
from app.storage import session_store
from app.services.ai_suggestion_service import generate_ai_suggestions





router = APIRouter(
    prefix="/upload",
    tags=["File Upload"]
)

UPLOAD_FOLDER = "uploads"


@router.post("/")
async def upload_file(
    file: UploadFile = File(...),
    question: str = Form("Summarize this dataset.")
):
    file_path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    try:
    # Read CSV
        df = pd.read_csv(file_path)

        # Clean dataset
        df = clean_dataset(df)

        #Kpis
        kpis = generate_kpis(df)

        #histogram
        histogram = generate_histogram(df)

        bar_chart = generate_bar_charts(df)

        boxplot = generate_boxplot(df)

        # Calculate health score
        health = calculate_health_score(df)

        correlations = correlation_analysis(df)

        outliers = detect_outliers(df) 
        
        # Generate business insights
        insights = generate_insights(df)

        # Profile dataset
        profile = profile_dataset(df)

        business_context = build_business_context(
            profile=profile,
            health=health,
            insights = insights,
            kpis=kpis

        )

        session_store.business_context = business_context

        suggestions = generate_ai_suggestions(
                    profile, kpis, insights
                )

        answer = ask_gemini(business_context, question)

        
        dashboard = generate_dashboard(
            insights = insights,
            health = health,
            correlations = correlations,
            outliers = outliers,
            histogram = histogram,
            bar_charts = bar_chart,
            boxplots = boxplot,
            profile = profile,
            kpis = kpis
        )

        report = generate_report(
            profile = profile,
            health = health,
            insights = insights,
            kpis = kpis
        )

        os.makedirs("reports", exist_ok = True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        pdf_path = f'reports/Business_Report_{timestamp}.pdf'
        generate_pdf(report = report, kpis = kpis, filename = pdf_path)


        return {
            "message": "File uploaded successfully",
            "filename": file.filename,
            "dashboard":dashboard,
            "answer": answer,
            "report": report,
            "pdf_report": pdf_path,
            "suggested_questions": suggestions
        }

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=f"Error reading CSV: {str(e)}"
        )