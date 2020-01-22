import streamlit as st
import camelot

def main():
    """Streamlit app testing camelot.py"""

    st.write("# Testing Camelot on Streamlit!")

    uploaded_file = st.file_uploader(label="Upload PDF with tables", type="pdf")
    if uploaded_file:
      tables = camelot.read_pdf(uploaded_file)
    
      for table in tables:
        st.write(table.df)
    else:
      st.write("waiting")

if __name__=="__main__":
    main()
