import streamlit as st
import camelot
import base64

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
        df = table.df
        csv = df.to_csv(index=False)
        b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
        href = f'<a href="data:file/csv;base64,{b64}">Download CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
        st.markdown(href, unsafe_allow_html=True)
        if st.button("wanna just copy + paste?"):
          st.text_area(csv)

    else:
      st.write("waiting")

if __name__=="__main__":
    main()
