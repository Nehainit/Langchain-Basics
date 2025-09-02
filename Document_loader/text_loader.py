from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

loader=TextLoader('Document_loader/test.txt')
docs=loader.load()
model=ChatOpenAI()
parser=StrOutputParser()

prompt=PromptTemplate(template="summarize the following text: {text}",input_variables=['text'])
chain=prompt | model | parser

result=chain.invoke(docs)
print(result)




