from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

class OpenAI_llm:
    def __init__(self):
        load_dotenv()

    
    def get_llm(self):
        try:
            os.environ['OPENAI_API_KEY']=self.openai_api_key=os.getenv('OPENAI_API_KEY')
            # os.environ['GROQ_API_KEY']=self.openai_api_key=os.getenv('GROQ_API_KEY')
            llm=ChatOpenAI(api_key=self.openai_api_key,model="gpt-4o")
            # llm=ChatGroq(api_key=self.openai_api_key,model="openai/gpt-oss-120b")
            return llm
        except Exception as e:
            raise ValueError("Error occurred with exception : {e}")