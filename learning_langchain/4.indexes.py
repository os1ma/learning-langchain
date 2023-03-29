from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.document_loaders.sitemap import SitemapLoader


loader = SitemapLoader(web_path="https://www.studyco.io/sitemap.xml")
documents = loader.load()
print("=== documents[0] ===")
print(documents[0])

# ここからのコードは以下の 2 行と同じ内容です
#
# index = VectorstoreIndexCreator().from_loaders([loader])
# result = index.query("StudyCoのメンバーを1人選んで紹介してください。")

text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)
embeddings = OpenAIEmbeddings()
db = Chroma.from_documents(texts, embeddings)
retriever = db.as_retriever()
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(), chain_type="stuff", retriever=retriever)
result = qa.run("StudyCoのメンバーを1人選んで紹介してください。")

print("=== result ===")
print(result)
