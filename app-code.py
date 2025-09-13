import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
from PyPDF2 import PdfReader
import docx
# ----------- Function to extract text from PDF -----------
def extract_text_from_pdf(file):
    text = ""
    pdf_reader = PdfReader(file)
    for page in pdf_reader.pages:
        text += page.extract_text() or ""
    return text
# ----------- Function to extract text from DOCX -----------
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = " ".join([para.text for para in doc.paragraphs])
    return text
# ----------- Preprocessing function -----------
def preprocess_text(text):
    # Lowercase
    text = text.lower()
    # Remove stopwords and generate word cloud directly (WordCloud handles stopwords)
    return text
    # ----------- Streamlit App -----------
def main():
    st.title("📄 Text Visualization - Word Cloud")
    st.write("Upload a *PDF* or *Word document* to generate a Word Cloud.")
uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx"])
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".pdf"):
            text = extract_text_from_pdf(uploaded_file)
        elif uploaded_file.name.endswith(".docx"):
            text = extract_text_from_docx(uploaded_file)
        else:
            st.error("Unsupported file type")
            return
        if text.strip() == "":
            st.warning("No extractable text found in the document.")
        else:
            processed_text = preprocess_text(text)
            # Generate word cloud
            wordcloud = WordCloud(
                width=800, 
                height=400,
                background_color="white",
                stopwords=STOPWORDS,
                collocations=True
            ).generate(processed_text)
            # Display word cloud
            st.subheader("Generated Word Cloud")
            fig, ax = plt.subplots(figsize=(10, 5))
            ax.imshow(wordcloud, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
if __name__="__main__":
    main()
