import streamlit as st
import speech_recognition as sr
from lease_agreement import generate_pdf as generate_lease_pdf
from birth_certificate import generate_pdf as generate_birth_pdf
from datetime import date

def get_voice_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("🎙️ Listening...")
        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            st.warning("Could not understand the audio. Please try again.")
        except sr.RequestError:
            st.error("Speech recognition service is unavailable.")
    return ""

st.set_page_config(page_title="Document Generator", layout="wide")

# Initialize session state for voice inputs
if 'voice_inputs' not in st.session_state:
    st.session_state.voice_inputs = {}

tab1, tab2 = st.tabs(["🏠 Lease Agreement", "📜 Birth Certificate"])

with tab1:
    st.title("🏠 Residential Lease Agreement Generator")
    
    st.subheader("🎤 Click a field below and then press 'Start Voice Input'")
    selected_field = st.selectbox("Select a field for voice input", ["Landlord's Name","Landlord's Address", "Tenant's Name","Additional Occupants", "Property Address","Residence Type","Bedrooms","Bathrooms","Lease Type","Lease Start Date","Lease End Date","Monthly Rent","Rent Due Date","Security Deposit","Return Period", "Additional Terms & Conditions", "Rules & Regulations",])
    if st.button("Start Voice Input"):
        voice_text = get_voice_input()
        if voice_text:
            st.session_state.voice_inputs[selected_field] = voice_text

    with st.form("lease_form"):
        st.subheader("🔹 Landlord & Tenant Details")
        landlord_name = st.text_input("Landlord's Name", st.session_state.voice_inputs.get("Landlord's Name", ""))
        landlord_address = st.text_input("Landlord's Address",st.session_state.voice_inputs.get("Landlord's Address", "") )
        tenant_name = st.text_input("Tenant's Name", st.session_state.voice_inputs.get("Tenant's Name", ""))
        additional_occupants = st.text_input("Additional Occupants", st.session_state.voice_inputs.get("Additional Occupants", ""))
        property_address = st.text_area("Property Address", st.session_state.voice_inputs.get("Property Address", ""))
        residence_type = st.text_area("Residence Type", st.session_state.voice_inputs.get("Residence Type", ""))
        bedrooms = st.text_area("Bedrooms", st.session_state.voice_inputs.get("Bedrooms", ""))
        bathrooms = st.text_area("Bathrooms", st.session_state.voice_inputs.get("Bathrooms", ""))
        lease_type = st.text_area("Lease Type", st.session_state.voice_inputs.get("Lease Type", ""))
        lease_start = st.text_area("Lease Start Date", st.session_state.voice_inputs.get("Lease Start Date", ""))
        lease_end = st.text_area("Lease End Date", st.session_state.voice_inputs.get("Lease End Date", ""))
        monthly_rent = st.text_area("Monthly Rent", st.session_state.voice_inputs.get("Monthly Rent", ""))
        due_date = st.text_area("Rent Due Date", st.session_state.voice_inputs.get("Rent Due Date", ""))
        security_deposit = st.text_area("Security Deposit", st.session_state.voice_inputs.get("Security Deposit", ""))
        return_period = st.text_area("Return Period", st.session_state.voice_inputs.get("Return Period", ""))
        additional_terms = st.text_area("Additional Terms & Conditions", st.session_state.voice_inputs.get("Additional Terms & Conditions", ""))
        rules_regulations = st.text_area("Rules & Regulations", st.session_state.voice_inputs.get("Rules & Regulations", ""))

        submit_lease = st.form_submit_button("Generate Lease Agreement")
    
    if submit_lease:
        if not landlord_name or not tenant_name or not property_address:
            st.warning("⚠️ Please fill out all required fields.")
        else:
            lease_data = {
                "landlord_name": landlord_name,
                "landlord_address": landlord_address,
                "tenant_name": tenant_name,
                "additional_occupants": additional_occupants,
                "property_address": property_address,
                "residence_type":residence_type,
                "bedrooms":bedrooms,
                "bathrooms":bathrooms,
                "lease_type":lease_type,
                "lease_start":lease_start,
                "lease_end":lease_end,
                "monthly_rent":monthly_rent,
                "due_date":due_date,
                "security_deposit":security_deposit,
                "return_period":return_period,
                "additional_terms": additional_terms,
                "rules_regulations": rules_regulations,

            }
            pdf_path = generate_lease_pdf(lease_data)
            st.success("✅ Lease Agreement Generated Successfully!")
            with open(pdf_path, "rb") as pdf_file:
                st.download_button("📄 Download Lease Agreement", pdf_file, file_name="Lease_Agreement.pdf", mime="application/pdf")

with tab2:
    st.title("📜 Birth Certificate Generator")
    
    st.subheader("🎤 Click a field below and then press 'Start Voice Input'")
    selected_field_birth = st.selectbox("Select a field for voice input", ["Full Name", "Place of Birth", "Father's Name", "Mother's Name", "Hospital Name"])
    if st.button("Start Voice Input", key="birth_voice"):
        voice_text = get_voice_input()
        if voice_text:
            st.session_state.voice_inputs[selected_field_birth] = voice_text
    
    with st.form("birth_certificate_form"):
        full_name = st.text_input("Full Name", st.session_state.voice_inputs.get("Full Name", ""))
        birth_place = st.text_input("Place of Birth", st.session_state.voice_inputs.get("Place of Birth", ""))
        father_name = st.text_input("Father's Name", st.session_state.voice_inputs.get("Father's Name", ""))
        mother_name = st.text_input("Mother's Name", st.session_state.voice_inputs.get("Mother's Name", ""))
        hospital_name = st.text_input("Hospital Name (if applicable)", st.session_state.voice_inputs.get("Hospital Name", ""))
        
        submit_birth = st.form_submit_button("Generate Birth Certificate")
    
    if submit_birth:
        if not full_name or not birth_place or not father_name or not mother_name:
            st.warning("⚠️ Please fill out all required fields.")
        else:
            birth_data = {
                "full_name": full_name,
                "birth_place": birth_place,
                "father_name": father_name,
                "mother_name": mother_name,
                "hospital_name": hospital_name,
            }
            pdf_path = generate_birth_pdf(birth_data)
            st.success("✅ Birth Certificate Generated Successfully!")
            with open(pdf_path, "rb") as pdf_file:
                st.download_button("📜 Download Birth Certificate", pdf_file, file_name="Birth_Certificate.pdf", mime="application/pdf")
