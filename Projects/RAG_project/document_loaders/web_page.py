from langchain_community.document_loaders import WebBaseLoader

url = r"https://www.apple.com/in/store?afid=p240%7Cgo~cmp-11116556120~adg-109516736379~ad-827438452233_kwd-10778630~dev-c~ext-~prd-~mca-~nt-search&cid=aos-in-kwgo-txt-brand-brand--"

loader = WebBaseLoader(url)

docs = loader.load()

print(docs[0].page_content)