import markdown
from flask import Flask, render_template, request, jsonify
import os
import google.generativeai as genai
from werkzeug.utils import secure_filename
import PyPDF2
import time

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Make sure your GEMINI_API_KEY is properly set in environment
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

def extract_questions_from_pdf(pdf_path):
    questions = []
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and line.endswith('?'):
                    questions.append(line)
    return questions

def get_answer_from_gemini(questions):
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")
        response = model.generate_content(questions)
        return response.text
    except Exception as e:
        error_msg = str(e)
        if "429" in error_msg:
            return "⚠️ Rate limit hit. Please wait a minute and try again."
        return f"❌ Error getting answer: {error_msg}"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    if file and file.filename.endswith('.pdf'):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        try:
            questions = extract_questions_from_pdf(filepath)
            qa_pairs = []
            for question in questions:
                answer = get_answer_from_gemini(question)
                
                # Convert Markdown response to HTML
                answer_html = markdown.markdown(answer)
                
                qa_pairs.append({
                    'question': question,
                    'answer': answer_html  # Store HTML content here
                })
                time.sleep(1.5)
            
            # Clean up the file
            os.remove(filepath)
            
            return render_template('index.html', qa_pairs=qa_pairs)
        except Exception as e:
            if os.path.exists(filepath):
                os.remove(filepath)
            return render_template('index.html', qa_pairs=[], error=str(e))

    return render_template('index.html', qa_pairs=[], error='Invalid file type')

if __name__ == '__main__':
    app.run(debug=True)