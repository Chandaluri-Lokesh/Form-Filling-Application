import fitz  # PyMuPDF
import re
import pdfplumber
from PIL import Image
import pytesseract
import io

# Extract placeholders from the uploaded PDF template
def extract_placeholders(pdf_path):
    doc = fitz.open(pdf_path)  # Open the PDF
    placeholders = set()  # To store placeholders like {{tenant_name}}, {{address}}, etc.
    
    for page in doc:
        text = page.get_text()  # Extract text from the page
        matches = re.findall(r"\{\{(.*?)\}\}", text)  # Regex to match {{placeholder}}
        placeholders.update(matches)  # Add found placeholders to the set
    
    doc.close()
    return list(placeholders)

# Fill the PDF with the user data
def fill_pdf(template_pdf, output_pdf, placeholders, user_data):
    doc = fitz.open(template_pdf)
    
    for page in doc:
        for key, value in user_data.items():
            placeholder = f"{{{{{key}}}}}"  # Example: {{tenant_name}}
            text_instances = page.search_for(placeholder)
            
            for inst in text_instances:
                page.insert_text(inst[:2], str(value), fontsize=12)  # Replace placeholder with value

    doc.save(output_pdf)
    doc.close()

# Extract text using OCR for image-based PDFs
def extract_text_with_ocr(pdf_path):
    extracted_text = ""

    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            # Extract text normally
            extracted_text += page.extract_text() or ""

            # Extract images (if any)
            for img in page.images:
                try:
                    # Convert the image to a PIL Image
                    image_data = img["stream"].get_data()
                    image = Image.open(io.BytesIO(image_data))
                    
                    # Apply OCR on the image
                    text_from_image = pytesseract.image_to_string(image)
                    extracted_text += "\n" + text_from_image  # Append OCR result
                    
                except Exception as e:
                    print(f"Error processing image: {e}")

    return extracted_text
