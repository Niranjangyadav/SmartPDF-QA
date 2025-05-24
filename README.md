## SmartPDF Q&A
This is a Flask based python application that extracts questions from an uploaded PDF and uses Google Gemini model to automatically generate answers. This tool streamlines the process of responding to bulk question documents, saving time and improving response consistency using state-of-the-art AI.

## Purpose
I made this project to automate the process of answering multiple questions embedded in PDF documents by leveraging OpenAI's language model. It is designed to:
* Save time and effort in manually answering bulk questions from PDFs 
* Improve consistency and quality of responses by using AI-generated answers
* Make document processing smarter by combining text extraction and natural language generation

## Installation
Install the required Python packages by running:
```bash
pip install flask PyPDF2 google-generativeai markdown werkzeug
```

## Running the Application
1. **Set your Google Gemini API key** in your environment:
- On macOS/Linux:
  ```bash
  export GEMINI_API_KEY="your_api_key_here"
  ```
- On Windows (Command Prompt):
  ```bash
  set GEMINI_API_KEY="your_api_key_here"
  ```
- On Windows (PowerShell):
  ```bash
  setx GEMINI_API_KEY "your_api_key_here"
  ```
2. Run the Flask app:
  ```bash
  python app.py
  ```
3. Open your browser and go to:
http://127.0.0.1:5000/
4. To stop the server, press Ctrl + C in the terminal.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




