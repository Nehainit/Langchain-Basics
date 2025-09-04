from langchain_core.runnables import RunnableLambda,RunnableParallel,RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import dotenv

dotenv.load_dotenv()

def word_count(text):
    return len(text.split())

model=ChatOpenAI()
parser=StrOutputParser()    
runnable_word_count=RunnableLambda(word_count)

joke_propmt=PromptTemplate(template="tell me a joke about {subject}",input_variables=['subject'])
joke_chain=joke_propmt | model | parser

joke_parralel=RunnableParallel(
    {
        'joke':RunnablePassthrough(),
        'word_count':RunnableLambda(word_count)
    }
)

final_chain=joke_chain|joke_parralel

result=final_chain.invoke({'subject':'AI'})
print(result)


