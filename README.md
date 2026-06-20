# Agentic YouTube Analyzer

An Agentic AI-powered YouTube Video Analyzer built using Gemini, Agno, and Streamlit.

The application analyzes YouTube videos and generates structured summaries, timestamps, multilingual reports, and downloadable PDF reports.

## Features

* Analyze YouTube videos using a URL
* Generate detailed video summaries
* Timestamp-based content breakdown
* Support for English and Hinglish output
* Download analysis reports as PDF
* Simple Streamlit user interface

## Technologies Used

* Python
* Streamlit
* Gemini API
* Agno Agent Framework
* ReportLab
* Python Dotenv

## Project Screenshots

Screenshots can be found in the `assets` folder.

## Installation

Clone the repository:

```bash
git clone <your-repository-url>
cd agentic-youtube-analyzer
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a file named `.env` in the project root directory.

Add your Gemini API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

You can get a Gemini API key from Google AI Studio.

## Run the Application

```bash
streamlit run ui.py
```

## Future Improvements

* Better support for multilingual transcripts
* Enhanced PDF formatting
* Additional export options
* Improved transcript handling

