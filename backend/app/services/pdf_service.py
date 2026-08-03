from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors


def generate_pdf(report: str, kpis: list, filename: str):
    """
    Generate Business Report PDF
    """

    document = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "Title",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=22,
        textColor=colors.black,
        spaceAfter=20,
    )

    heading_style = ParagraphStyle(
        "Heading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.black,
        spaceBefore=10,
        spaceAfter=10,
    )

    normal_style = styles["BodyText"]

    story = []

    lines = report.split("\n")

    #Report
    for line in lines:

        line = line.strip()

        if not line:
            continue

        if set(line) == {"="}:
            continue

        if set(line) == {"-"}:
            continue

        #insert KPI Table
        if line == "End of Report":
            story.append(Spacer(1,20))
            story.append(Paragraph('KEY PERFORMANCE INDICATORS (KPIS)', heading_style))

            table_data = [["KPI", "Value"]]

            for kpi in kpis:
                table_data.append([
                    kpi['title'],
                    str(kpi['value'])
                ])

            table = Table(table_data, colWidths = [260, 120])

            table.setStyle( 
                TableStyle([
                    ('BACKGROUND', (0,0),(-1,0), colors.lightgrey),
                    ('TEXTCOLOR',(0,0),(-1,0), colors.black),
                    ("FONTNAME",(0,0), (-1,0), "Helvetica-Bold"),
                    ("GRID", (0,0), (-1,-1), 0.5, colors.grey),
                    ('BACKGROUND',(0,1),(-1,-1),colors.whitesmoke),
                    ("BOTTOMPADDING",(0,0),(-1,-1), 6),
                ])
            )

            story.append(table)
            story.append(Spacer(1, 20))





        if "Business Analysis Report" in line:
            story.append(
                Paragraph(line, title_style)
            )

        elif line.isupper() and len(line) > 3:
            story.append(
                Paragraph(line, heading_style)
            )

        else:
            story.append(
                Paragraph(line, normal_style)
            )

        story.append(
            Spacer(1, 6)
        )

    document.build(story)