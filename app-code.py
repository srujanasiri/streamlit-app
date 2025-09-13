import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import docx
import PyPDF2

def extract_text(file):
    text = ""
    if file.type == "application/pdf":
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text += page.extract_text() or ""
    elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

st.title("📄 Word Cloud Generator")

uploaded_file = st.file_uploader("Upload a PDF or Word file", type=["pdf", "docx"])

if uploaded_file is not None:   # ✅ No extra spaces here
    text = extract_text(uploaded_file)
    if text.strip():
        wc = WordCloud(width=800, height=400, background_color="white").generate(text)
        fig, ax = plt.subplots()
        ax.imshow(wc, interpolation="bilinear")
        ax.axis("off")
        st.pyplot(fig)
    else:
        st.warning("⚠ No text found in the file.")
