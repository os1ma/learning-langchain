from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import UnstructuredURLLoader
from langchain.document_loaders.sitemap import SitemapLoader


loader = SitemapLoader(web_path="https://www.studyco.io/sitemap.xml")
documents = loader.load()
print("=== documents[0] ===")
print(documents[0])

index = VectorstoreIndexCreator().from_loaders([loader])
result = index.query("早野さんのことを紹介してください。")
print("=== result ===")
print(result)
