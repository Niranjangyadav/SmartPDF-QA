import PyPDF2
import openai

# Function to extract text from a PDF file
def extract_questions_from_pdf(pdf_path):
    questions = []
    with open(pdf_path, "rb") as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            # Split the text into lines and filter out empty lines
            lines = text.split('\n')
            for line in lines:
                line = line.strip()
                if line and line.endswith('?'):  # Assuming questions end with '?'
                    questions.append(line)
    return questions

# Function to ask OpenAI a question
def ask_openai(question, api_key):
    openai.api_key = api_key
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )
    return response['choices'][0]['message']['content']

# Main function
def main():
    pdf_path = "your-file.pdf"  # Path to your PDF file
    api_key = "your_openai_api_key"  # Your OpenAI API key

    # Extract questions from the PDF
    questions = extract_questions_from_pdf(pdf_path)

    # Get answers for each question
    for question in questions:
        answer = ask_openai(question, api_key)
        print(f"Q: {question}\n: {answer}\n")

if __name__ == "__main__":
    main()

