from fpdf import FPDF

def generate_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Birth Certificate", ln=True, align='C')
    pdf.ln(10)

    # Certificate Number & Issuing Authority
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, f"Certificate Number: {data['certificate_number']}", ln=True)
    pdf.cell(0, 10, f"Issuing Authority: {data['issuing_authority']}", ln=True)
    
    pdf.ln(5)

    # Personal Details
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Personal Details", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Full Name: {data['full_name']}\n"
                           f"Date of Birth: {data['birth_date']}\n"
                           f"Place of Birth: {data['birth_place']}\n"
                           f"Gender: {data['gender']}\n")

    pdf.ln(5)

    # Parent Details
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Parent Details", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Father's Name: {data['father_name']}\n"
                           f"Mother's Name: {data['mother_name']}\n")

    pdf.ln(5)

    # Hospital Name (if applicable)
    if data['hospital_name']:
        pdf.set_font("Arial", style="B", size=12)
        pdf.cell(0, 10, "Hospital Information", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(0, 10, f"Hospital Name: {data['hospital_name']}", ln=True)

    pdf.ln(10)

    # Official Seal and Signature
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Authorized Signature:", ln=True)
    pdf.cell(0, 10, "_________________________", ln=True)
    pdf.cell(0, 10, "Date: ___________________", ln=True)

    # Save PDF
    file_path = "Birth_Certificate.pdf"
    pdf.output(file_path)

    return file_path
