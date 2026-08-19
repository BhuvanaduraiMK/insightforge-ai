import os

from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
    Image,
    PageBreak,
)
from reportlab.lib.styles import (
    getSampleStyleSheet,
    ParagraphStyle,
)
from reportlab.lib.enums import TA_CENTER
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4


def generate_pdf(
    report: str,
    kpis: list,
    filename: str,
    histogram=None,
    bar_charts=None,
    boxplots=None,
):
    """
    Generate Business Analysis PDF report.

    Includes:
    - Business report
    - KPI table
    - Selected visualizations
    """

    document = SimpleDocTemplate(
        filename,
        pagesize=A4,
        rightMargin=40,
        leftMargin=40,
        topMargin=40,
        bottomMargin=40,
    )

    styles = getSampleStyleSheet()

    title_style = ParagraphStyle(
        "CustomTitle",
        parent=styles["Heading1"],
        alignment=TA_CENTER,
        fontSize=22,
        textColor=colors.black,
        spaceAfter=20,
    )

    heading_style = ParagraphStyle(
        "CustomHeading",
        parent=styles["Heading2"],
        fontSize=14,
        textColor=colors.black,
        spaceBefore=10,
        spaceAfter=10,
    )

    normal_style = styles["BodyText"]

    story = []

   
    lines = report.split("\n")

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if set(line) == {"="}:
            continue

        if set(line) == {"-"}:
            continue

       
        if line == "End of Report":

            story.append(
                Spacer(1, 20)
            )

            story.append(
                Paragraph(
                    "KEY PERFORMANCE INDICATORS (KPIs)",
                    heading_style
                )
            )

            table_data = [
                ["KPI", "Value"]
            ]

            for kpi in kpis:

                table_data.append([
                    kpi.get("title", "N/A"),
                    str(kpi.get("value", "N/A"))
                ])

            table = Table(
                table_data,
                colWidths=[260, 120]
            )

            table.setStyle(
                TableStyle([
                    (
                        "BACKGROUND",
                        (0, 0),
                        (-1, 0),
                        colors.lightgrey
                    ),
                    (
                        "TEXTCOLOR",
                        (0, 0),
                        (-1, 0),
                        colors.black
                    ),
                    (
                        "FONTNAME",
                        (0, 0),
                        (-1, 0),
                        "Helvetica-Bold"
                    ),
                    (
                        "GRID",
                        (0, 0),
                        (-1, -1),
                        0.5,
                        colors.grey
                    ),
                    (
                        "BACKGROUND",
                        (0, 1),
                        (-1, -1),
                        colors.whitesmoke
                    ),
                    (
                        "BOTTOMPADDING",
                        (0, 0),
                        (-1, -1),
                        6
                    ),
                ])
            )

            story.append(table)

            story.append(
                Spacer(1, 20)
            )

            continue

       
        if "Business Analysis Report" in line:

            story.append(
                Paragraph(
                    line,
                    title_style
                )
            )

        elif line.isupper() and len(line) > 3:

            story.append(
                Paragraph(
                    line,
                    heading_style
                )
            )

        else:

            story.append(
                Paragraph(
                    line,
                    normal_style
                )
            )

        story.append(
            Spacer(1, 6)
        )

   
    story.append(
        PageBreak()
    )

    story.append(
        Paragraph(
            "VISUAL ANALYSIS",
            heading_style
        )
    )

    story.append(
        Paragraph(
            "The following charts provide visual summaries "
            "of important patterns in the uploaded dataset.",
            normal_style
        )
    )

    story.append(
        Spacer(1, 15)
    )

    if bar_charts:

        story.append(
            Paragraph(
                "Categorical Analysis",
                heading_style
            )
        )

        # Limit PDF size
        selected_bars = bar_charts[:4]

        for chart_path in selected_bars:

            if not os.path.exists(chart_path):
                continue

            story.append(
                Image(
                    chart_path,
                    width=450,
                    height=280
                )
            )

            story.append(
                Spacer(1, 15)
            )

    
    if histogram:

        story.append(
            PageBreak()
        )

        story.append(
            Paragraph(
                "Distribution Analysis",
                heading_style
            )
        )

        selected_histograms = histogram[:3]

        for chart_path in selected_histograms:

            if not os.path.exists(chart_path):
                continue

            story.append(
                Image(
                    chart_path,
                    width=450,
                    height=270
                )
            )

            story.append(
                Spacer(1, 15)
            )

    
    if boxplots:

        story.append(
            PageBreak()
        )

        story.append(
            Paragraph(
                "Outlier Analysis",
                heading_style
            )
        )

        selected_boxplots = boxplots[:3]

        for chart_path in selected_boxplots:

            if not os.path.exists(chart_path):
                continue

            story.append(
                Image(
                    chart_path,
                    width=450,
                    height=270
                )
            )

            story.append(
                Spacer(1, 15)
            )

    
    document.build(story)