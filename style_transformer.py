import os
from openai import OpenAI
from dotenv import load_dotenv
from author_info import AUTHOR_INFO
import time

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

class StyleTransformer:
    def __init__(self):
        if not os.getenv("OPENAI_API_KEY"):
            raise ValueError("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
    
    def transform_text(self, text, author, intensity=5):
        intensity_factor = intensity / 10.0
        prompt = f"""
        Transform the following text to match the writing style of {author}. 
        The transformation intensity should be {intensity_factor} (where 0.1 is subtle and 1.0 is extreme).
        
        Original text:
        {text}
        
        Transformed text in the style of {author}:
        """
        
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": f"You are a literary style transformer that mimics the writing style of {author}."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=1000
            )
            
            transformed_text = response.choices[0].message.content.strip()
            return transformed_text
        
        except Exception as e:
            print(f"Error transforming text: {e}")
            return f"Error: {str(e)}"
    
    def get_available_authors(self):
        return list(AUTHOR_INFO.keys()) 