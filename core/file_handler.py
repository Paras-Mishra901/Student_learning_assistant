import PyPDF2
def extract_text_from_file(uploaded_file):
    try:
        if uploaded_file is None:
            return ""

        file_name = uploaded_file.name.lower()

        if file_name.endswith(".txt"):
            return uploaded_file.read().decode("utf-8", errors="ignore")

        elif file_name.endswith(".pdf"):
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            extracted_text = ""

            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    extracted_text += page_text + "\n"

            return extracted_text.strip()

        else:
            return "Unsupported file format. Please upload TXT or PDF."

    except Exception as e:
        return f"File Extraction Error: {str(e)}"