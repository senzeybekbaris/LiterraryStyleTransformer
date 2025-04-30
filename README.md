# Literary Style Transformer

A system that transforms uploaded documents into the writing style of famous authors using AI.

## Features

- Upload PDF documents
- Automatically extract and process text content
- Transform the document into different author styles:
  - William Shakespeare
  - Edgar Allan Poe
  - Fyodor Dostoevsky
  - J.R.R. Tolkien
  - Leo Tolstoy
  - Johann Wolfgang von Goethe
  - Albert Camus
  - Franz Kafka
- Modern UI with original and transformed text display

## Setup

1. Clone this repository
   ```
   git clone https://github.com/yourusername/literary-style-transformer.git
   cd literary-style-transformer
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root with your OpenAI API key:
   ```
   cp .env.example .env
   # Then edit .env and add your OpenAI API key
   ```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```
2. Open your web browser and navigate to the local URL displayed in the terminal (typically http://localhost:8501)
3. Upload a PDF file and click "Process Document"
4. Select an author style from the sidebar
5. Click "Transform" to see your document rewritten in the selected author's style

## How it Works

1. **PDF Processing**: The system extracts text from the uploaded PDF.
2. **Text Transformation**: When a style is selected, the system:
   - Uses a specialized prompt for the selected author
   - Sends the document text and prompt to an LLM (GPT-3.5 Turbo)
   - Returns the transformed text in the author's unique style

## Technologies Used

- LangChain: Framework for working with LLMs
- OpenAI: For text generation and transformation
- Streamlit: Web interface for user interaction
- PyPDF: PDF text extraction

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details. 