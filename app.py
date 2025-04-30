import os
import streamlit as st
from dotenv import load_dotenv
from pdf_processor import process_pdf
from style_transformer import StyleTransformer

load_dotenv()
if "processed" not in st.session_state:
    st.session_state.processed = False
if "transformer" not in st.session_state:
    st.session_state.transformer = None
if "document_text" not in st.session_state:
    st.session_state.document_text = ""

st.title("Literary Style Transformer")
st.write("Upload a document and see how famous authors would rewrite it")

st.sidebar.title("Author Styles")
selected_author = st.sidebar.radio(
    "Choose an author style:",
    [
        "William Shakespeare", 
        "Edgar Allan Poe", 
        "Fyodor Dostoevsky",
        "J.R.R. Tolkien",
        "Leo Tolstoy",
        "Johann Wolfgang von Goethe",
        "Albert Camus",
        "Franz Kafka"
    ]
)

# File uploader
uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

if uploaded_file is not None:
    # Process PDF button
    if not st.session_state.processed:
        if st.button("Process Document"):
            with st.spinner("Processing document..."):
                # Save uploaded file temporarily
                with open("temp.pdf", "wb") as f:
                    f.write(uploaded_file.getvalue())
                
                # Process the PDF
                documents = process_pdf("temp.pdf")
                # Combine all document chunks into a single text
                full_text = " ".join([doc.page_content for doc in documents])
                st.session_state.document_text = full_text
                
                # Initialize transformer
                st.session_state.transformer = StyleTransformer()
                st.session_state.processed = True
                
                # Clean up
                os.remove("temp.pdf")
            
            st.success("Document processed successfully!")
    else:
        st.subheader("Original Document")
        with st.expander("Show original text"):
            st.write(st.session_state.document_text)
        
        # Transform button
        if st.button(f"Transform to {selected_author}'s Style"):
            with st.spinner(f"Transforming into {selected_author}'s style..."):
                transformed_text = st.session_state.transformer.transform_text(
                    st.session_state.document_text, 
                    selected_author
                )
                
            st.subheader(f"In the style of {selected_author}")
            st.write(transformed_text)
            
        # Reset button
        if st.button("Process a new document"):
            st.session_state.processed = False
            st.session_state.transformer = None
            st.session_state.document_text = ""
            st.experimental_rerun()
else:
    st.info("Please upload a PDF file to get started.")