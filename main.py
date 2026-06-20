from textwrap import dedent
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.google import Gemini
from agno.tools.youtube import YouTubeTools
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from io import BytesIO

load_dotenv()
def youtube_agent():
    return Agent(
    name="YouTube Agent",
    model=Gemini(id="gemini-2.5-flash"),
    tools=[YouTubeTools(
       languages=["hi", "en", "en-US"]
       )],
    instructions=dedent("""\
        You are an expert YouTube content analyst with a keen eye for detail! 🎓
        Follow these steps for comprehensive video analysis:
        1. Video Overview
           - Check video length and basic metadata
           - Identify video type (tutorial, review, lecture, etc.)
           - Note the content structure
        2. Timestamp Creation
           - Create precise, meaningful timestamps
           - Focus on major topic transitions
           - Highlight key moments and demonstrations
           - Format: [start_time, end_time, detailed_summary]
        3. Content Organization
           - Group related segments
           - Identify main themes
           - Track topic progression

        Your analysis style:
        - Begin with a video overview
        - Use clear, descriptive segment titles
        - Include relevant emojis for content types:
          📚 Educational
          💻 Technical
          🎮 Gaming
          📱 Tech Review
          🎨 Creative
        - Highlight key learning points
        - Note practical demonstrations
        - Mark important references

        Quality Guidelines:
        - Verify timestamp accuracy
        - Avoid timestamp hallucination
        - Ensure comprehensive coverage
        - Maintain consistent detail level
        - Focus on valuable content markers
    """),
    add_datetime_to_context=True,
    markdown=True,
)

def create_pdf(content):
    buffer = BytesIO()

    doc = SimpleDocTemplate(buffer)
    styles = getSampleStyleSheet()

    story = []

    for line in content.split("\n"):

        line = line.strip()

        if not line:
            story.append(Spacer(1, 10))
            continue

        if line.startswith("## "):
            story.append(
                Paragraph(
                    line.replace("## ", ""),
                    styles["Heading1"]
                )
            )

        elif line.startswith("### "):
            story.append(
                Paragraph(
                    line.replace("### ", ""),
                    styles["Heading2"]
                )
            )

        elif line.startswith("#### "):
            story.append(
                Paragraph(
                    line.replace("#### ", ""),
                    styles["Heading3"]
                )
            )

        else:
            line = line.replace("**", "")
            story.append(
                Paragraph(
                    line,
                    styles["BodyText"]
                )
            )

    doc.build(story)

    buffer.seek(0)
    return buffer