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
    size: float = 13,
    leading: float = 16,
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
    pdf.setFont("Lato-Black", 14)
    pdf.drawString(x, y, text)
    pdf.setStrokeColor(ACCENT)
    pdf.setLineWidth(2)
    pdf.line(x, y - 5, x + width, y - 5)
    return y - 22


def bullet(pdf: canvas.Canvas, text: str, x: float, y: float, width: float) -> float:
    pdf.setFillColor(ACCENT)
    pdf.circle(x + 3, y - 3, 2, stroke=0, fill=1)
    return paragraph(pdf, text, x + 12, y, width - 12, size=13, leading=16)


def label_value(pdf: canvas.Canvas, label: str, value: str, x: float, y: float, width: float) -> float:
    pdf.setFillColor(MUTED)
    pdf.setFont("Lato-Medium", 13)
    pdf.drawString(x, y, label.upper())
    y -= 15
    return paragraph(pdf, value, x, y, width, font="Lato-Semibold", size=13, leading=16, color=INK) - 6


def draw_github_icon(pdf: canvas.Canvas, x: float, y: float, size: float = 18) -> None:
    pdf.saveState()
    pdf.setFillColor(INK)
    pdf.roundRect(x, y, size, size, 4, stroke=0, fill=1)

    cx = x + size / 2
    face_y = y + size * 0.5
    pdf.setFillColor(HexColor("#FFFFFF"))
    pdf.circle(cx, face_y, size * 0.31, stroke=0, fill=1)

    left_ear = pdf.beginPath()
    left_ear.moveTo(x + size * 0.28, y + size * 0.66)
    left_ear.lineTo(x + size * 0.33, y + size * 0.86)
    left_ear.lineTo(x + size * 0.47, y + size * 0.7)
    left_ear.close()
    pdf.drawPath(left_ear, stroke=0, fill=1)

    right_ear = pdf.beginPath()
    right_ear.moveTo(x + size * 0.72, y + size * 0.66)
    right_ear.lineTo(x + size * 0.67, y + size * 0.86)
    right_ear.lineTo(x + size * 0.53, y + size * 0.7)
    right_ear.close()
    pdf.drawPath(right_ear, stroke=0, fill=1)

    pdf.setFillColor(INK)
    pdf.circle(x + size * 0.4, y + size * 0.5, size * 0.035, stroke=0, fill=1)
    pdf.circle(x + size * 0.6, y + size * 0.5, size * 0.035, stroke=0, fill=1)

    pdf.setFillColor(HexColor("#FFFFFF"))
    pdf.roundRect(x + size * 0.38, y + size * 0.14, size * 0.1, size * 0.21, 1.5, stroke=0, fill=1)
    pdf.roundRect(x + size * 0.52, y + size * 0.14, size * 0.1, size * 0.21, 1.5, stroke=0, fill=1)
    pdf.restoreState()


def draw_linkedin_icon(pdf: canvas.Canvas, x: float, y: float, size: float = 18) -> None:
    pdf.saveState()
    pdf.setFillColor(HexColor("#0A66C2"))
    pdf.roundRect(x, y, size, size, 4, stroke=0, fill=1)

    pdf.setFillColor(HexColor("#FFFFFF"))
    pdf.circle(x + size * 0.3, y + size * 0.73, size * 0.075, stroke=0, fill=1)
    pdf.roundRect(x + size * 0.22, y + size * 0.24, size * 0.16, size * 0.36, 1.2, stroke=0, fill=1)
    pdf.roundRect(x + size * 0.46, y + size * 0.24, size * 0.16, size * 0.38, 1.2, stroke=0, fill=1)
    pdf.roundRect(x + size * 0.59, y + size * 0.39, size * 0.17, size * 0.24, 1.5, stroke=0, fill=1)
    pdf.roundRect(x + size * 0.68, y + size * 0.24, size * 0.08, size * 0.28, 1.1, stroke=0, fill=1)
    pdf.restoreState()


def make_resume() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    PUBLIC.parent.mkdir(parents=True, exist_ok=True)

    width, height = A4
    pdf = canvas.Canvas(str(OUTPUT), pagesize=A4)
    pdf.setTitle("Trần Lê Thái - AI Engineering Intern and Backend Developer")
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
    pdf.setFont("Lato-Semibold", 14)
    pdf.drawString(margin, header_y - 22, "AI ENGINEERING INTERN / BACKEND DEVELOPER")

    y_links = header_y - 48

    gh_x = margin
    icon_y = y_links - 3
    icon_size = 18
    draw_github_icon(pdf, gh_x, icon_y, icon_size)

    gh_text_x = gh_x + 25
    pdf.setFillColor(INK)
    pdf.setFont("Lato-Semibold", 13)
    gh_url_text = "devonxjz"
    pdf.drawString(gh_text_x, y_links, gh_url_text)
    gh_w = pdfmetrics.stringWidth(gh_url_text, "Lato-Semibold", 13)
    pdf.linkURL("https://github.com/devonxjz", (gh_x, icon_y, gh_text_x + gh_w, icon_y + icon_size), relative=0)

    li_x = gh_text_x + gh_w + 24
    draw_linkedin_icon(pdf, li_x, icon_y, icon_size)

    li_text_x = li_x + 25
    pdf.setFillColor(INK)
    pdf.setFont("Lato-Semibold", 13)
    li_url_text = "devonxjz"
    pdf.drawString(li_text_x, y_links, li_url_text)
    li_w = pdfmetrics.stringWidth(li_url_text, "Lato-Semibold", 13)
    pdf.linkURL("https://www.linkedin.com/in/devonxjz", (li_x, icon_y, li_text_x + li_w, icon_y + icon_size), relative=0)

    top = header_y - 70
    left_x = margin
    left_w = 164
    right_x = 224
    right_w = width - right_x - margin

    pdf.setStrokeColor(LINE)
    pdf.setLineWidth(0.7)
    pdf.line(right_x - 18, 40, right_x - 18, top + 14)

    right_y = section_title(pdf, "PROFILE", right_x, top, right_w)
    right_y = paragraph(
        pdf,
        "Information Technology student at HCMUTE pursuing an AI Engineering Internship. I design and ship LLM-powered agents — spanning prompt/context engineering, tool-use orchestration, structured outputs, and workflow evaluation — backed by reliable, secure-by-design APIs.",
        right_x,
        right_y,
        right_w,
        size=13,
        leading=16,
    ) - 15

    right_y = section_title(pdf, "SELECTED PROJECTS", right_x, right_y, right_w)
    projects = [
        (
            "PhongVu AI Sales Agent",
            "07/2026 - 08/2026",
            "Role: AI Agent Developer. Built a sales assistant flow for product discovery, requirement collection and structured purchase guidance using LLM orchestration with commerce data. Designed the conversation flow to clarify customer needs, use product information and return consistent recommendations.",
        ),
        (
            "CV-Agent",
            "03/2025 - 05/2025",
            "Role: Full-stack AI Developer. Built a resume analysis and optimization platform with Google Gemini, Express, MongoDB and React, returning scored feedback and actionable rewrite suggestions. Connected resume processing, AI evaluation and a responsive interface into one practical workflow for improving applications.",
        ),
        (
            "VibeTDU",
            "9/2025 - 10/2026",
            "Role: Backend and AI Integration Developer. Built an interactive virtual chemistry lab with Spring Boot, Next.js and Gemini support for guided experiments and learning feedback. Integrated experiment flows, backend APIs and AI-assisted explanations to make lab activities more interactive and easier to follow.",
        ),
    ]
    for title, period, body in projects:
        pdf.setFillColor(INK)
        pdf.setFont("Lato-Semibold", 14)
        pdf.drawString(right_x, right_y, title)
        pdf.setFillColor(MUTED)
        pdf.setFont("Lato", 13)
        pdf.drawRightString(right_x + right_w, right_y, period)
        right_y -= 18
        right_y = paragraph(pdf, body, right_x, right_y, right_w, size=13, leading=16) - 10

    right_y = section_title(pdf, "ENGINEERING EXPERIENCE", right_x, right_y, right_w)
    experience = [
        "Designing backend APIs, service layers and data models that support real AI product workflows.",
        "Building LLM workflows that call tools, use external services and return structured results.",
        "Exploring prompt design, memory, guardrails, evaluation and observability for practical AI systems.",
        "Practicing web security and vulnerability analysis through Burp Suite and hands-on labs.",
    ]
    for item in experience:
        right_y = bullet(pdf, item, right_x, right_y, right_w) - 4

    left_y = section_title(pdf, "EDUCATION", left_x, top, left_w)
    left_y = label_value(pdf, "09/2024 - Present", "HCMUTE\nInformation Technology", left_x, left_y, left_w)
    left_y = paragraph(pdf, "Focus: Backend Engineering & Security", left_x, left_y, left_w, size=13, leading=16) - 10
    left_y = label_value(pdf, "09/2021 - 06/2024", "Hung Vuong High School\nSpecialized in Informatics", left_x, left_y, left_w)

    left_y = section_title(pdf, "HIGHLIGHTS", left_x, left_y - 5, left_w)
    left_y = label_value(pdf, "2023", "Third Prize Science & Engineering", left_x, left_y, left_w)
    left_y = label_value(pdf, "07/2026", "AABW AI Agent Build Competition", left_x, left_y, left_w)

    left_y = section_title(pdf, "TECHNICAL SKILLS", left_x, left_y - 5, left_w)
    skills = [
        ("Languages", "Java, Python, JS, TS, C, C++"),
        ("Backend", "Spring Boot, NestJS, Node.js"),
        ("Database", "PostgreSQL, MongoDB, MySQL"),
        ("AI", "LLMs, Agents, Tools, Guardrails"),
        ("Security", "Burp Suite, TryHackMe"),
        ("Tools", "Git, Docker, Vercel"),
    ]
    for label, value in skills:
        left_y = label_value(pdf, label, value, left_x, left_y, left_w)

    pdf.setFillColor(MUTED)
    pdf.setFont("Lato", 11)
    pdf.drawString(margin, 20, "Contact: tranlethai11102006@gmail.com")
    pdf.drawRightString(width - margin, 20, "Ho Chi Minh City")

    pdf.showPage()
    pdf.save()
    PUBLIC.write_bytes(OUTPUT.read_bytes())


if __name__ == "__main__":
    make_resume()
