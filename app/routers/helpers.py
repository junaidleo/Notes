from langchain.document_loaders import WebBaseLoader
from langchain.chains.combine_documents.stuff import StuffDocumentsChain
from langchain.chains import LLMChain
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
from langchain.prompts import PromptTemplate
from langchain.docstore.document import Document
from app.core.config import settings



# Summarize note content
def summarize_content(content: str):
    prompt_template = """Write a concise summary of the following:

    "{content}"

    CONCISE SUMMARY:
    """

    prompt = PromptTemplate.from_template(prompt_template)

    load_dotenv()
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-1106", api_key=settings.OPENAI_API_KEY)
    llm_chain = LLMChain(prompt=prompt, llm=llm)

    stuff_chain = StuffDocumentsChain(
        llm_chain=llm_chain, document_variable_name="content")

    docs = [Document(page_content=content)]

    return stuff_chain.run(docs)

