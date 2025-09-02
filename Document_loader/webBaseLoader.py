from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader=WebBaseLoader('https://www.geeksforgeeks.org/python/python-map-function/')

docs=loader.load()

print(docs[0].page_content)

# model=ChatOpenAI()
# parser=StrOutputParser()


