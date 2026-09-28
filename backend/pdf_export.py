from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

BASE_DIR = Path(__file__).resolve().parent.parent
OUTPUT_DIR = BASE_DIR / "generated"

OUTPUT_DIR.mkdir(exist_ok=True)

def create_pdf(comic):

    output = OUTPUT_DIR / "comiccraft_comic.pdf"

    styles = getSampleStyleSheet()

    doc = SimpleDocTemplate(
        str(output),
        pagesize=A4
    )

    content = []

    content.append(
        Paragraph(comic["title"], styles["Title"])
    )

    content.append(Spacer(1, 20))

    for panel in comic["panels"]:

        content.append(
            Paragraph(
                f"Panel {panel['panel']}",
                styles["Heading2"]
            )
        )

        content.append(
            Paragraph(
                panel["scene"],
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 10))

        content.append(
            Paragraph(
                panel["dialogue"],
                styles["BodyText"]
            )
        )

        content.append(Spacer(1, 25))

    doc.build(content)

    return output
