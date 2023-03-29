from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders.sitemap import SitemapLoader


loader = SitemapLoader(web_path="https://www.studyco.io/sitemap.xml")
documents = loader.load()


template = """
以下のcontextをもとに質問に回答してください。
ただし、少しだけ明らかに嘘と分かる情報をまぜてください。

ここからcontextです。

{context}

contextは以上です。

質問: {question}
回答:
"""
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

print("=== result ===")
result = qa.run("StudyCoのメンバーを1人選んで紹介してください。")
print(result)
