from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders import DirectoryLoader
import langchain


langchain.verbose = True

loader = DirectoryLoader("./langchain/docs/_build/html/", glob="**/*.html")
documents = loader.load()

template = """Use the following pieces of context to answer the question at the end. If you don't know the answer, just say that you don't know, don't try to make up an answer.

{context}

Question: {question}
条件: 少しだけ明らかに嘘と分かる情報をまぜてください。
Helpful Answer:"""
prompt = PromptTemplate(
    input_variables=["context", "question"], template=template)

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(texts, embeddings)
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(), chain_type="stuff", retriever=retriever,
    chain_type_kwargs={"prompt": prompt})

result = qa.run("LangChainの概要を1文で説明してください。")
print(f"result: {result}")
