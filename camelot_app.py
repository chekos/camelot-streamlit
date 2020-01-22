import streamlit as st
import camelot

def process_pdf(pdf_bytes):
  with open("tmp.pdf", "wb") as file:
    file.write(pdf_bytes.read())

def main():
    """Streamlit app testing camelot.py"""

    st.write("# Testing Camelot on Streamlit!")

    uploaded_file = st.file_uploader(label="Upload PDF with tables", type="pdf")
    if uploaded_file is not None:
      process_pdf(uploaded_file)
      tables = camelot.read_pdf("tmp.pdf", pages="all")
    
      for table in tables:
        st.write(table.df)
    else:
      st.write("waiting")

if __name__=="__main__":
    main()
