from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=120, chunk_overlap=1)

# reading the transcript
with open("test_exports/transcript.txt", "r", encoding="utf-8") as f:
    text = f.read()

chunks = text_splitter.create_documents([text])

embeddings = OpenAIEmbeddings()

vector_store = FAISS.from_documents(chunks, embeddings)

# vector_store.save_local("test_exports/vector_store")

retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 1})


# Augmentation

from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_template(
    "You are a helpful assistant. You are given a transcript of a video. You need to answer the question based on the context of the transcript. context: {context} Question: {question}"
)

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

chain = prompt | llm

result=chain.invoke({"context": retriever.invoke("What is the topic of the video?"), "question": "What is prime minister of Nepal"})

print(result.content)
