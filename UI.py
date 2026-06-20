import streamlit as st
from main import youtube_agent
from main import create_pdf

st.set_page_config(
    page_title="Youtube Video Analyzer",
    layout="centered"
)
st.title("AI Youtube Video Analyzer")

@st.cache_resource
def get_agent():
    return youtube_agent()

agent=get_agent()

video_url=st.text_input("Enter Youtube Video Link")
language = st.selectbox(
    "Select Output Language",
    ["English", "Hinglish"]
)
button=st.button("Analyze")
if video_url and button:
    with st.spinner("Analyzing ..."):
        try:
            response = agent.run(
            f'''Analyze this video: {video_url}
            Output Language: {language}
             Instructions:
             - Analyze the video regardless of the transcript language.
             - If the transcript is in another language, translate and understand it before analysis.
             - Generate the final report entirely in {language}.
             - Preserve technical terms where appropriate.'''
            )
            st.markdown("Analysis Report of Video : ")
            st.markdown(response.content)
            pdf_file = create_pdf(response.content)
            st.download_button(
                label="Download Analysis as PDF",
                data=pdf_file,
                file_name="youtube_video_analysis.pdf",
                mime="application/pdf"
                )
        except Exception as e:
            st.error(f"Something went wrong while analyzing the video. Please try again later.")