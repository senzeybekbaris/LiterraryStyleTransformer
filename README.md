# Literary Style Transformer

A Streamlit application that transforms your text into the style of famous authors using OpenAI's GPT models.

## Features

- Transform any text into the style of famous authors like Ernest Hemingway, Jane Austen, Charles Dickens, and more
- Adjust the intensity of the style transformation
- Simple and intuitive user interface
- Download transformed text

## Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/literary-style-transformer.git
cd literary-style-transformer
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the Streamlit app:
```bash
streamlit run app.py
```

2. Open your web browser and navigate to the URL shown in the terminal (usually http://localhost:8501)

3. Select an author from the dropdown menu in the sidebar

4. Adjust the style intensity using the slider (1 = subtle, 10 = extreme)

5. Enter your text in the text area on the left

6. Click the "Transform Text" button to see your text transformed into the selected author's style

7. Download the transformed text using the download button

## Available Authors

- Ernest Hemingway
- Jane Austen
- Charles Dickens
- Virginia Woolf
- Mark Twain
- William Shakespeare

## Technologies Used

- [Streamlit](https://streamlit.io/) - Web application framework
- [OpenAI API](https://openai.com/api/) - For text transformation
- [Python-dotenv](https://github.com/theskumar/python-dotenv) - For environment variable management

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- OpenAI for providing the GPT models
- The authors whose styles are emulated in this application 