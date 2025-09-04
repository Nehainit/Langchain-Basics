from langchain_core.runnables import RunnableSequence
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import dotenv

dotenv.load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()
prompt=ChatPromptTemplate.from_template("translate the following text to {language}: {text}")

chain=prompt | model | parser

result=chain.invoke({'language':'french','text':'I love this product'})
print(result)


