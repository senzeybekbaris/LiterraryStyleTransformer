import os
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

class RAGEngine:
    def __init__(self, documents):
        self.embeddings = OpenAIEmbeddings(
            openai_api_key=os.environ.get("OPENAI_API_KEY")
        )
        
        self.vector_store = Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings
        )
        
        self.retriever = self.vector_store.as_retriever(
            search_type="similarity",
            search_kwargs={"k": 5}
        )
        
        template = """
        You are a helpful assistant that answers questions based on the provided context.
        Answer the question based only on the context below. If the context doesn't contain
        the information to answer the question, say "I don't have enough information to answer this question."
        Do not make up or hallucinate any information that is not in the context.
        
        Context:
        {context}
        
        Question: {question}
        
        Answer:
        """
        
        self.prompt = PromptTemplate(
            template=template,
            input_variables=["context", "question"]
        )
        
        self.llm = ChatOpenAI(
            openai_api_key=os.environ.get("OPENAI_API_KEY"),
            model_name="gpt-3.5-turbo",
            temperature=0
        )
        
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.retriever,
            chain_type_kwargs={"prompt": self.prompt}
        )
        
    def generate_answer(self, query):
        result = self.qa_chain.invoke({"query": query})
        return result["result"] 