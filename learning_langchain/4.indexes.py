from langchain.document_loaders.sitemap import SitemapLoader
from langchain.indexes import VectorstoreIndexCreator


loader = SitemapLoader(web_path="https://www.studyco.io/sitemap.xml")
documents = loader.load()
print("=== documents[0] ===")
print(documents[0])

index = VectorstoreIndexCreator().from_loaders([loader])
result = index.query("StudyCoのメンバーを1人選んで紹介してください。")

print("=== result ===")
print(result)
