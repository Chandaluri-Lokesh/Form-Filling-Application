# Form Filling Application

This application allows users to fill out forms using either speech or text input. It processes the input, extracts relevant information, and generates a completed application form.

## Features
- Accepts user input via speech recognition or text
- Automatically extracts and maps input data to the appropriate form fields
- Generates a fully completed application form in a structured format (e.g., PDF, DOCX)
- Supports multiple form templates

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd form-filling-app
   ```

2. Create a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Run the application:
   ```sh
   streamlit run app.py
   ```

## Usage
1. Select the type of form you want to fill.
2. Choose your input method: speech or text.
3. Provide the required details.
4. Review the generated form and download the completed version.

## Dependencies
- Python 3.x
- Streamlit
- SpeechRecognition
- PyPDF2 / python-docx (for form generation)
- OpenAI Whisper (optional for advanced speech recognition)

## License
This project is licensed under the MIT License.
