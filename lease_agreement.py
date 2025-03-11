from fpdf import FPDF

def generate_pdf(data):
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    pdf.cell(200, 10, "Residential Lease Agreement", ln=True, align='C')
    pdf.ln(10)

    # Landlord & Tenant Details
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Landlord & Tenant Details", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Landlord: {data['landlord_name']}\n"
                           f"Landlord Address: {data['landlord_address']}\n"
                           f"Tenant: {data['tenant_name']}\n"
                           f"Additional Occupants: {data['additional_occupants']}\n")

    pdf.ln(5)

    # Property Details
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Property Details", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Property Address: {data['property_address']}\n"
                           f"Residence Type: {data['residence_type']}\n"
                           f"Bedrooms: {data['bedrooms']}\n"
                           f"Bathrooms: {data['bathrooms']}\n")

    pdf.ln(5)

    # Lease Terms
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Lease Terms", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Lease Type: {data['lease_type']}\n"
                           f"Lease Start Date: {data['lease_start']}\n"
                           f"Lease End Date: {data['lease_end']}\n")

    pdf.ln(5)

    # Rent Details
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Rent Details", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, f"Monthly Rent: ${data['monthly_rent']}\n"
                           f"Rent Due Date: {data['due_date']}\n"
                           f"Security Deposit: ${data['security_deposit']}\n"
                           f"Return Period: {data['return_period']} days after lease end\n")

    pdf.ln(5)

    # Additional Terms & Rules
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Additional Terms & Rules", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data['additional_terms'])

    pdf.ln(5)



    # Rules & Regulations
    pdf.set_font("Arial", style="B", size=12)
    pdf.cell(0, 10, "Rules & Regulations", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, data['rules_regulations'])

    pdf.ln(5)

    pdf.ln(10)

    # Signature Section
    pdf.cell(0, 10, "Signed:", ln=True)
    pdf.cell(0, 10, "Landlord: ______________________   Date: __________", ln=True)
    pdf.cell(0, 10, "Tenant:   ______________________   Date: __________", ln=True)

    # Save PDF
    file_path = "Lease_Agreement.pdf"
    pdf.output(file_path)

    return file_path
