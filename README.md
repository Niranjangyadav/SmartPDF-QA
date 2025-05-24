# SmartPDF Q&A
This is a Flask based python application that extracts questions from an uploaded PDF and uses Google Gemini model to automatically generate answers. This tool streamlines the process of responding to bulk question documents, saving time and improving response consistency using state-of-the-art AI.
# Purpose
I made this project to automate the process of answering multiple questions embedded in PDF documents by leveraging OpenAI's language model. It is designed to:
* Save time and effort in manually answering bulk questions from PDFs 
* Improve consistency and quality of responses by using AI-generated answers
* Make document processing smarter by combining text extraction and natural language generation
## Installation

Install the required Python packages by running:

```bash
pip install flask PyPDF2 google-generativeai markdown werkzeug

