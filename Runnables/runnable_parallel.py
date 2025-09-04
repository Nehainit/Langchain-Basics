from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
import dotenv

dotenv.load_dotenv()

model=ChatOpenAI()
parser=StrOutputParser()
twitter_prompt=PromptTemplate(template="generate a twitter post on the following topic: {topic}",
                      input_variables=['topic'])
twitter_chain=twitter_prompt | model | parser

linkdin_prompt=PromptTemplate(template="generate a linkdin post on the following topic: {topic}",
                      input_variables=['topic'])
linkdin_chain=linkdin_prompt | model | parser

runnable_parallel=RunnableParallel({

    'tweet':RunnableSequence(twitter_prompt,model,parser),
    'linkdin':RunnableSequence(linkdin_prompt,model,parser)
}
)

result=runnable_parallel.invoke({'topic':'AI'})
print(result)














