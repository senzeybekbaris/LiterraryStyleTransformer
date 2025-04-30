import os
import streamlit as st
from dotenv import load_dotenv
from pdf_processor import process_pdf
from style_transformer import StyleTransformer
from author_info import AUTHOR_INFO
import time

load_dotenv()
if "processed" not in st.session_state:
    st.session_state.processed = False
if "transformer" not in st.session_state:
    st.session_state.transformer = None
if "document_text" not in st.session_state:
    st.session_state.document_text = ""

# Set page configuration
st.set_page_config(
    page_title="Literary Style Transformer",
    page_icon="📚",
    layout="wide"
)

# Initialize the style transformer
@st.cache_resource
def get_style_transformer():
    return StyleTransformer()

style_transformer = get_style_transformer()

# App title and description
st.title("📚 Literary Style Transformer")
st.markdown("""
Transform your text into the style of famous authors. Choose an author, enter your text, 
and adjust the intensity to see how your writing would look in the style of literary giants.
""")

# Sidebar for author selection and intensity
with st.sidebar:
    st.header("Settings")
    
    # Author selection
    available_authors = style_transformer.get_available_authors()
    selected_author = st.selectbox(
        "Select an Author",
        available_authors,
        index=0
    )
    
    # Intensity slider
    intensity = st.slider(
        "Style Intensity",
        min_value=1,
        max_value=10,
        value=5,
        step=1,
        help="Adjust how strongly the author's style should be applied (1 = subtle, 10 = extreme)"
    )
    
    # Display author information
    if selected_author in AUTHOR_INFO:
        st.divider()
        st.header("Author Information")
        author = AUTHOR_INFO[selected_author]
        
        # Display author image if available
        if "image" in author:
            st.image(author["image"], caption=author["name"])
        elif "image_url" in author:
            st.image(author["image_url"], caption=author["name"])
            
        st.markdown(f"**Years:** {author['years']}")
        st.markdown(f"**Nationality:** {author['nationality']}")
        st.markdown(f"**Genre:** {author['genre']}")
        
        st.markdown("**Famous Works:**")
        if isinstance(author['famous_works'], list):
            for work in author['famous_works']:
                st.markdown(f"- {work}")
        else:
            st.markdown(author['famous_works'])
            
        st.markdown("**Writing Style:**")
        if "writing_style" in author:
            st.markdown(author["writing_style"])
        elif "style_description" in author:
            st.markdown(author["style_description"])

# Main content area
col1, col2 = st.columns(2)

with col1:
    st.subheader("Your Text")
    input_text = st.text_area(
        "Enter the text you want to transform",
        height=300,
        placeholder="Type or paste your text here..."
    )

with col2:
    st.subheader("Transformed Text")
    
    # Add a transform button
    if st.button("Transform Text", type="primary"):
        if input_text:
            with st.spinner("Transforming your text..."):
                # Add a small delay to show the spinner
                time.sleep(1)
                
                # Transform the text
                transformed_text = style_transformer.transform_text(
                    input_text, 
                    selected_author, 
                    intensity
                )
                
                # Display the transformed text
                st.text_area(
                    f"Text in the style of {selected_author}",
                    transformed_text,
                    height=300,
                    disabled=True
                )
                
                # Add a download button
                st.download_button(
                    label="Download Transformed Text",
                    data=transformed_text,
                    file_name=f"{selected_author.lower().replace(' ', '_')}_style.txt",
                    mime="text/plain"
                )
        else:
            st.warning("Please enter some text to transform.")

# File uploader
st.subheader("Process PDF Document")
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
        # Create two columns for side-by-side display
        doc_col1, doc_col2 = st.columns(2)
        
        with doc_col1:
            st.subheader("Original Document")
            st.text_area(
                "Original text",
                st.session_state.document_text,
                height=400,
                disabled=True
            )
        
        with doc_col2:
            st.subheader(f"Transformed Text")
            # Transform button
            if st.button(f"Transform to {selected_author}'s Style"):
                with st.spinner(f"Transforming into {selected_author}'s style..."):
                    transformed_text = st.session_state.transformer.transform_text(
                        st.session_state.document_text, 
                        selected_author,
                        intensity
                    )
                    
                st.text_area(
                    f"In the style of {selected_author}",
                    transformed_text,
                    height=400,
                    disabled=True
                )
                
                # Add download button for transformed text
                st.download_button(
                    label="Download Transformed Text",
                    data=transformed_text,
                    file_name=f"{selected_author.replace(' ', '_')}_transformed.txt",
                    mime="text/plain"
                )
        
        # Reset button - centered below both columns
        st.button("Process a new document", use_container_width=True, on_click=lambda: setattr(st.session_state, 'processed', False))
else:
    st.info("Please upload a PDF file to get started.")

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center'>
    <p>Created with ❤️ for literature enthusiasts</p>
    <p>Powered by OpenAI's GPT models</p>
</div>
""", unsafe_allow_html=True)