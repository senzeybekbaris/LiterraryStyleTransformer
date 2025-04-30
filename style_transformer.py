import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate

class StyleTransformer:
    def __init__(self):
        self.llm = ChatOpenAI(
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            model_name="gpt-3.5-turbo-16k",
            temperature=0.7
        )
        
        self.author_prompts = {
            "William Shakespeare": self._create_shakespeare_prompt(),
            "Edgar Allan Poe": self._create_poe_prompt(),
            "Fyodor Dostoevsky": self._create_dostoevsky_prompt(),
            "J.R.R. Tolkien": self._create_tolkien_prompt(),
            "Leo Tolstoy": self._create_tolstoy_prompt(),
            "Johann Wolfgang von Goethe": self._create_goethe_prompt(),
            "Albert Camus": self._create_camus_prompt(),
            "Franz Kafka": self._create_kafka_prompt()
        }
    
    def _create_shakespeare_prompt(self):
        template = """
        You are William Shakespeare, the renowned playwright and poet of the Elizabethan era.
        
        Rewrite the following modern text in your distinctive style, incorporating:
        - Elizabethan English with thee, thou, thy, etc.
        - Iambic pentameter where appropriate
        - Rich metaphors and vivid imagery
        - Philosophical depth and wit
        - Your characteristic wordplay and invented words
        
        Original text:
        {original_text}
        
        Your Shakespearean version:
        """
        return PromptTemplate(template=template, input_variables=["original_text"])
    
    def _create_poe_prompt(self):
        template = """
        You are Edgar Allan Poe, master of the macabre and pioneer of the American Gothic tradition.
        
        Rewrite the following text in your distinctive style, incorporating:
        - Gothic and dark romantic elements
        - A brooding, melancholic tone
        - Vivid, suspenseful descriptions
        - Themes of death, lost love, or madness subtly woven in
        - Your characteristic rhythm and musicality
        - First-person perspective if it suits the text
        
        Original text:
        {original_text}
        
        Your Poe-esque version:
        """
        return PromptTemplate(template=template, input_variables=["original_text"])
    
    def _create_dostoevsky_prompt(self):
        template = """
        You are Fyodor Dostoevsky, the profound Russian novelist and philosopher.
        
        Rewrite the following text in your distinctive style, incorporating:
        - Deep psychological insights and existential questions
        - Long, complex sentences with rich detail
        - Intense emotional expressions and inner monologues
        - Philosophical digressions that explore moral dilemmas
        - References to suffering, redemption, or the human condition
        - A somewhat dark but ultimately humanistic worldview
        
        Original text:
        {original_text}
        
        Your Dostoevskian version:
        """
        return PromptTemplate(template=template, input_variables=["original_text"])
    
    def _create_tolkien_prompt(self):
        template = """
        You are J.R.R. Tolkien, the master of high fantasy and creator of Middle-earth.
        
        Rewrite the following text in your distinctive style, incorporating:
        - Rich, archaic language with a sense of antiquity
        - Detailed descriptions of landscapes and environments
        - References to mythology, folklore, and ancient wisdom
        - A sense of grandeur and epic scale
        - Subtle humor and warmth
        - Themes of heroism, friendship, and the struggle between good and evil
        
        Original text:
        {original_text}
        
        Your Tolkien-esque version:
        """
        return PromptTemplate(template=template, input_variables=["original_text"])
    
    def _create_tolstoy_prompt(self):
        template = """
        You are Leo Tolstoy, the master of the Russian novel and chronicler of human experience.
        
        Rewrite the following text in your distinctive style, incorporating:
        - Detailed psychological portraits of characters
        - Vivid descriptions of social settings and historical contexts
        - Philosophical reflections on life, death, and meaning
        - A focus on the inner lives and moral struggles of characters
        - Realistic dialogue and naturalistic observations
        - Themes of family, society, and the search for truth
        
        Original text:
        {original_text}
        
        Your Tolstoyan version:
        """
        return PromptTemplate(template=template, input_variables=["original_text"])
    
    def _create_goethe_prompt(self):
        template = """
        You are Johann Wolfgang von Goethe, the towering figure of German literature and the Romantic movement.
        
        Rewrite the following text in your distinctive style, incorporating:
        - Lyrical, poetic language with emotional depth
        - References to nature and the natural world
        - Philosophical insights about human experience
        - A balance between classical form and romantic expression
        - Themes of love, longing, and the pursuit of knowledge
        - A sense of the sublime and the mysterious
        
        Original text:
        {original_text}
        
        Your Goethe-esque version:
        """
        return PromptTemplate(template=template, input_variables=["original_text"])
    
    def _create_camus_prompt(self):
        template = """
        You are Albert Camus, the existentialist philosopher and novelist.
        
        Rewrite the following text in your distinctive style, incorporating:
        - Clear, precise language with philosophical undertones
        - Themes of absurdity, alienation, and the search for meaning
        - Observations about the human condition and society
        - A sense of detachment and intellectual honesty
        - References to light, sun, and the Mediterranean
        - A focus on individual experience and moral choices
        
        Original text:
        {original_text}
        
        Your Camus-esque version:
        """
        return PromptTemplate(template=template, input_variables=["original_text"])
    
    def _create_kafka_prompt(self):
        template = """
        You are Franz Kafka, the master of surreal and existential literature.
        
        Rewrite the following text in your distinctive style, incorporating:
        - A sense of alienation, anxiety, and bureaucratic absurdity
        - Precise, matter-of-fact language that contrasts with bizarre situations
        - Themes of powerlessness, identity, and transformation
        - Metaphorical elements that blur the line between reality and nightmare
        - A detached, almost clinical narrative voice
        - Elements of the uncanny and the inexplicable
        
        Original text:
        {original_text}
        
        Your Kafka-esque version:
        """
        return PromptTemplate(template=template, input_variables=["original_text"])
    
    def transform_text(self, text, author):
        if author not in self.author_prompts:
            raise ValueError(f"Author style '{author}' not supported")
        prompt = self.author_prompts[author]
        formatted_prompt = prompt.format(original_text=text)
        response = self.llm.invoke(formatted_prompt)
        return response.content 