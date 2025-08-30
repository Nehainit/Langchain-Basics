from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

model = ChatOpenAI()

prompt1= PromptTemplate(
    template='Generate a detail report about {topic}',
    input_variables=['topic']
)

prompt2= PromptTemplate(
    template='Genertate 5 most important points from {report}',
    input_variables=['report']
)

parser = StrOutputParser()

chain1 = prompt1 | model | parser | prompt2 | model | parser
report = chain1.invoke({'topic': 'pehlgam terriost attack on india'})

# chain2 = r
# points = chain2.invoke({'report': report})

print(report)







