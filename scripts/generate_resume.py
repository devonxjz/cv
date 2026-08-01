from pathlib import Path

from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "output" / "pdf" / "tran-le-thai-cv.pdf"
PUBLIC = ROOT / "public" / "tran-le-thai-cv.pdf"

FONT_DIR = Path("/usr/share/fonts/truetype/lato")
pdfmetrics.registerFont(TTFont("Lato", FONT_DIR / "Lato-Regular.ttf"))
pdfmetrics.registerFont(TTFont("Lato-Medium", FONT_DIR / "Lato-Medium.ttf"))
pdfmetrics.registerFont(TTFont("Lato-Semibold", FONT_DIR / "Lato-Semibold.ttf"))
pdfmetrics.registerFont(TTFont("Lato-Black", FONT_DIR / "Lato-Black.ttf"))

INK = HexColor("#182019")
MUTED = HexColor("#5F685F")
LINE = HexColor("#C8CEC6")
ACCENT = HexColor("#F05A3C")
PAPER = HexColor("#F3F4EF")


def wrap(text: str, font: str, size: float, width: float) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = word if not current else f"{current} {word}"
        if pdfmetrics.stringWidth(candidate, font, size) <= width:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def paragraph(
    pdf: canvas.Canvas,
    text: str,
    x: float,
    y: float,
    width: float,
    font: str = "Lato",
    size: float = 8.5,
    leading: float = 11.2,
    color=MUTED,
) -> float:
    pdf.setFillColor(color)
    pdf.setFont(font, size)
    for line in wrap(text, font, size, width):
        pdf.drawString(x, y, line)
        y -= leading
    return y


def section_title(pdf: canvas.Canvas, text: str, x: float, y: float, width: float) -> float:
    pdf.setFillColor(INK)
    pdf.setFont("Lato-Black", 10.2)
    pdf.drawString(x, y, text)
    pdf.setStrokeColor(ACCENT)
    pdf.setLineWidth(2)
    pdf.line(x, y - 5, x + width, y - 5)
    return y - 18


def bullet(pdf: canvas.Canvas, text: str, x: float, y: float, width: float) -> float:
    pdf.setFillColor(ACCENT)
    pdf.circle(x + 2.2, y - 2.2, 1.5, stroke=0, fill=1)
    return paragraph(pdf, text, x + 10, y, width - 10, size=8.15, leading=10.5)


def label_value(pdf: canvas.Canvas, label: str, value: str, x: float, y: float, width: float) -> float:
    pdf.setFillColor(MUTED)
    pdf.setFont("Lato-Medium", 6.8)
    pdf.drawString(x, y, label.upper())
    y -= 10
    return paragraph(pdf, value, x, y, width, font="Lato-Semibold", size=8.4, leading=10.8, color=INK) - 5


def make_resume() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PUBLIC.parent.mkdir(parents=True, exist_ok=True)

    width, height = A4
    pdf = canvas.Canvas(str(OUTPUT), pagesize=A4)
    pdf.setTitle("Trần Lê Thái - Backend, AI and Security Engineer")
    pdf.setAuthor("Trần Lê Thái")
    pdf.setSubject("Curriculum Vitae")
    pdf.setFillColor(PAPER)
    pdf.rect(0, 0, width, height, stroke=0, fill=1)

    margin = 34
    header_y = height - 45
    pdf.setFillColor(INK)
    pdf.setFont("Lato-Black", 25)
    pdf.drawString(margin, header_y, "TRẦN LÊ THÁI")
    pdf.setFillColor(ACCENT)
    pdf.rect(width - 45, header_y - 2, 11, 25, stroke=0, fill=1)

    pdf.setFillColor(INK)
    pdf.setFont("Lato-Semibold", 9.6)
    pdf.drawString(margin, header_y - 20, "BACKEND ENGINEER / AI ENGINEER / SECURITY-MINDED DEVELOPER")
    pdf.setFillColor(MUTED)
    pdf.setFont("Lato", 7.4)
    pdf.drawString(margin, header_y - 36, "Ho Chi Minh City, Vietnam")
    pdf.drawString(margin + 108, header_y - 36, "tranlethai11102006@gmail.com")
    pdf.drawString(margin + 265, header_y - 36, "github.com/devonxjz")
    pdf.drawString(margin + 380, header_y - 36, "linkedin.com/in/devonxjz")

    top = header_y - 64
    left_x = margin
    left_w = 337
    right_x = 397
    right_w = width - right_x - margin

    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(0.7)
    pdf.line(right_x - 18, 40, right_x - 18, top + 14)

    left_y = section_title(pdf, "PROFILE", left_x, top, left_w)
    left_y = paragraph(
        pdf,
        "Information Technology student at HCMUTE building reliable backend services and practical AI systems. I focus on clear tool boundaries, controlled execution, useful memory, observable workflows and secure-by-design behavior.",
        left_x,
        left_y,
        left_w,
        size=8.8,
        leading=11.6,
    ) - 15

    left_y = section_title(pdf, "SELECTED PROJECTS", left_x, left_y, left_w)
    projects = [
        (
            "CV-Agent",
            "AI resume analysis and optimization platform using Google Gemini, Express, MongoDB and React.",
        ),
        (
            "MissLost",
            "UEH lost-and-found platform with real-time chat, verified returns, NestJS, Next.js and PostgreSQL.",
        ),
        (
            "VibeTDU",
            "Interactive virtual chemistry lab built with Spring Boot, Next.js, Gemini integration and Zustand.",
        ),
        (
            "WeatherForecast AI",
            "ML prediction, alerts, analytics, maps and chatbot support using Spring, TensorFlow, Redis and PostgreSQL.",
        ),
    ]
    for title, body in projects:
        pdf.setFillColor(INK)
        pdf.setFont("Lato-Semibold", 9.1)
        pdf.drawString(left_x, left_y, title)
        left_y -= 12
        left_y = paragraph(pdf, body, left_x, left_y, left_w, size=8.1, leading=10.4) - 7

    left_y = section_title(pdf, "ENGINEERING EXPERIENCE", left_x, left_y + 1, left_w) - 2
    experience = [
        "Designing REST APIs, service layers and persistence around maintainability and debugging.",
        "Building agentic workflows that select tools, call external services and return structured results.",
        "Exploring memory, state management, prompt design, guardrails, evaluation and observability.",
        "Practicing web security and vulnerability analysis through Burp Suite and hands-on labs.",
    ]
    for item in experience:
        left_y = bullet(pdf, item, left_x, left_y, left_w) - 3

    right_y = section_title(pdf, "EDUCATION", right_x, top, right_w)
    right_y = label_value(pdf, "2024-Present", "HCMUTE\nInformation Technology", right_x, right_y, right_w)
    right_y = paragraph(pdf, "Focus: Backend Engineering and Information Security", right_x, right_y, right_w, size=7.8, leading=10) - 8
    right_y = label_value(pdf, "2021-2024", "Hung Vuong High School for the Gifted\nSpecialized in Informatics", right_x, right_y, right_w)

    right_y = section_title(pdf, "HIGHLIGHTS", right_x, right_y - 3, right_w)
    right_y = label_value(pdf, "2023", "Third Prize in School Science and Engineering", right_x, right_y, right_w)
    right_y = label_value(pdf, "ASEAN", "AABW AI Agent Build Competition participant", right_x, right_y, right_w)

    right_y = section_title(pdf, "TECHNICAL SKILLS", right_x, right_y - 2, right_w)
    skills = [
        ("Languages", "Java, Python, JavaScript, TypeScript, C, C++"),
        ("Backend", "Spring, NestJS, Node.js, REST APIs"),
        ("Data", "PostgreSQL, MongoDB, MySQL, SQL/NoSQL modeling"),
        ("AI", "Agent workflows, tool calling, memory, guardrails, evaluation"),
        ("Security", "Burp Suite, TryHackMe, Hack The Box, Root-Me"),
        ("Tools", "Git, GitHub, Docker, Vercel"),
    ]
    for label, value in skills:
        right_y = label_value(pdf, label, value, right_x, right_y, right_w)

    pdf.setFillColor(MUTED)
    pdf.setFont("Lato", 6.8)
    pdf.drawString(margin, 22, "Contact: tranlethai11102006@gmail.com")
    pdf.drawRightString(width - margin, 22, "Updated August 2026")

    pdf.showPage()
    pdf.save()
    PUBLIC.write_bytes(OUTPUT.read_bytes())


if __name__ == "__main__":
    make_resume()
