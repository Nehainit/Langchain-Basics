
from abc import ABC, abstractmethod
import random


class Runnable(ABC):
  @abstractmethod
  def invoke(input_data):
    pass

class NakliLLM(Runnable):

  def __init__(self):
    print("llm created")

  def invoke(self,prompt):
    response_list=['Delhi is the capital of india',
                   'IPL IS INDIAN PREMIMUM LEAGUE',
                   'AI stands for Artificial intelligence']
    return {'response': random.choice(response_list)}

  def predict(self,propmt):
    response_list=['Delhi is the capital of india',
                   'IPL IS INDIAN PREMIMUM LEAGUE',
                   'AI stands for Artificial intelligence']

    return {'response': random.choice(response_list)}

class NakliPropmptTemplate(Runnable):

  def __init__(self,template,input_variables):
    self.template=template
    self.input_variables=input_variables

  def invoke(self,input_dict):
    return self.template.format(**input_dict)

class Runnableconnector(Runnable):
  def __init__(self,runable_list):
    self.runable_list=runable_list
  def invoke(self,input_data):
    for runnable in self.runable_list:
      print(runnable)
      input_data=runnable.invoke(input_data)
      print(input_data)
    return input_data

class NaklistrOutputparser(Runnable):
  def __init__(self):
    pass
  def invoke(self, input_data):
    return input_data

template=NakliPropmptTemplate( template="write a {length} poem on {topic}",
                              input_variables={'length','topic'})

llm=NakliLLM()
# chain=Runnableconnector([template,llm])
# chain.invoke({'length':'short','topic':'india'})

template1=NakliPropmptTemplate( template="write a joke about {topic}",
                              input_variables={'topic'})

template2=NakliPropmptTemplate( template="Explain the joke {response}",
                              input_variables={'response'})

parser=NaklistrOutputparser()

chain1=Runnableconnector([template1,llm,parser])

chain2=Runnableconnector([template2,llm,parser])

final_chain=Runnableconnector([chain1,chain2])

final_chain.invoke({'topic':'donkey'})
