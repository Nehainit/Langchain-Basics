from langchain_community.document_loaders import PyPDFLoader
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()


pdf_loader=PyPDFLoader('Document_loader/L-G-0003984878-0008706570.pdf')
docs=pdf_loader.load()
print(docs[0].metadata)

model=ChatOpenAI()
parser=StrOutputParser()

prompt=PromptTemplate(template="summarize the following text: {text}",input_variables=['text'])
chain=prompt | model | parser

result=chain.invoke(docs)
print(result)


