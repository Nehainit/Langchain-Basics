from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()


llm=OpenAI(model="gpt-3.5-turbo-instruct")
result=llm.invoke("What is the capital of France?") #invoke method is very impotant in llms,string as an input and string as output
print(result)

