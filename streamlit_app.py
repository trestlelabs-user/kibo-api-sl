import streamlit as st
import constants

# st.title('Kibo API demo')

home_page = st.Page("home.py", title='Home')
table_to_excel_page = st.Page("table_to_excel_api.py", title="Table to Excel")
ocr_page = st.Page("ocr_api.py", title="OCR - Text extraction")
translation_page = st.Page("translation_api.py", title="Translation")
identity_page = st.Page("identity_docs_api.py", title="Identify Documents")
identity_page_1 = st.Page("identity_docs_api.py", title="Identify Documents - 1")
custom_data_extraction_page = st.Page("custom_data_extraction_api.py", title="Custom data extraction")
medical_reports_page = st.Page("medical_reports_api.py", title="Meidcal reports")
handwritten_prescriptions_page = st.Page("handwritten_prescriptions_api.py", title="Handwritten prescriptions")
# documentation = st.Page(f"{constants.BASE_URL}/docs", title='Documentation')
with st.sidebar:
    st.page_link(
        page=f"{constants.BASE_URL}/docs",
        label="**Documentation**",
        icon="🏠",
    )
pg = st.navigation(
    {
        "Home": [home_page],
        "New": [identity_page],
        "General": [ocr_page, translation_page, custom_data_extraction_page],
        "Utility": [table_to_excel_page],
        "Medical": [medical_reports_page, handwritten_prescriptions_page],
        # "Documentation": [documentation]
    }
)
pg.run()
