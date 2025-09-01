from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableMap,RunnableParallel,RunnableBranch,RunnableLambda
from langchain.output_parsers import PydanticOutputParser
from typing import Literal
from pydantic import BaseModel,Field
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()
class feedback(BaseModel):
    feedback:Literal['positive','negative']=Field(description="The sentiment of the feedback")

parser = StrOutputParser()
parser2=PydanticOutputParser(pydantic_object=feedback)


prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback: {feedback}\n\n{format_instructions}',
    input_variables=['feedback'],
    partial_variables={'format_instructions':parser2.get_format_instructions()}
)

prompt2=PromptTemplate(
    template='Write an appropriate response to this postive feedback: {feedback}',
    input_variables=['feedback']
)

prompt3=PromptTemplate(
    template='Write an appropriate response to the following negative feedback: {feedback}',
    input_variables=['feedback']
)

classfier_chain=prompt1 | model | parser2

branch_chain=RunnableBranch(
(lambda x:x.feedback=='positive',prompt2 | model | parser),
(lambda x:x.feedback=='negative',prompt3 | model | parser),
RunnableLambda(lambda x:f"could not find sentiments in {x}")
)

chain=classfier_chain | branch_chain

result=chain.invoke({'feedback':'I hate this product'})
print(result)
# translator_chain=prompt2 | model | parser




