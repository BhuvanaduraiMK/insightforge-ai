from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def generate_pdf(report: str, filename: str):
    """
    Generate Business Report PDF
    """
    document = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()
    story = []
    story.append(Paragraph(report, styles["Normal"]))
    document.build(story)
    