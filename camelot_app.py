import streamlit as st
import camelot
import base64
import uuid


def process_pdf(pdf_bytes):
    with open("tmp.pdf", "wb") as file:
        file.write(pdf_bytes.read())


def display_download_options(df):
    """Receives a dataframe and displays 2 ways to download the data."""
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(csv.encode()).decode()

    # href (save file) way
    href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
    st.markdown(href, unsafe_allow_html=True)

    # Copy and paste way
    if st.checkbox("Copy + paste?", key=uuid.uuid1()):
        st.text_area(csv)
    
    return None


def main():
    """Streamlit app testing camelot.py"""

    st.write("# Testing Camelot on Streamlit!")

    uploaded_file = st.file_uploader(label="Upload PDF with tables", type="pdf")
    if uploaded_file is not None:
        process_pdf(uploaded_file)
        tables = camelot.read_pdf("tmp.pdf", pages="all")

        for table in tables:
            df = table.df
            st.write(df)
            display_download_options(df)

    else:
        st.write("Upload a PDF file with some tables in it.")


if __name__ == "__main__":
    main()
