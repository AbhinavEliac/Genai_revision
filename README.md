# GenAI Revision

Curious about generative AI? This repo is a hands-on playground of small,
runnable Python examples built around GenAI and the LangChain ecosystem. You’ll
find chat models, Hugging Face integrations, embeddings, structured extraction,
document loaders, text splitters, starter PDF summarization, and vector store
indexing with Chroma.

These are learning projects, not one big packaged app. Each script runs on its
own, and some need API keys, a model download, an internet connection, or a
quick local file-path update. Pick a demo and get experimenting.

## What’s inside

- [Repository layout](#repository-layout)
- [Before you start](#before-you-start)
- [Setup](#setup)
- [Try the demos](#try-the-demos)
- [Notes and limitations](#notes-and-limitations)

## Repository layout

```text
.
├── chatmodels/
│   ├── chat.py                     # Basic chat completion through LangChain
│   ├── chatbot.py                  # Interactive, multi-turn persona chatbot
│   ├── huggingface.py              # Hosted Hugging Face chat model
│   └── localmodel.py               # Local Hugging Face text-generation model
├── embeddingmodels/
│   ├── embeddings.py               # OpenAI embeddings
│   └── hf_embeddings.py            # Hugging Face embeddings
├── Projects/
│   ├── movie_data_cleaner.py       # Movie information extraction to a Pydantic schema
│   ├── RAG_project/
│   │   ├── main.py                 # PDF loading, recursive chunking, and LLM summarization
│   │   ├── covariance_vs_correlation.txt
│   │   ├── deep-learning-material-dept-ece-ase-blr-1.pdf
│   │   ├── deep_learning_and_transformers.pdf
│   │   └── document_loaders/
│   │       ├── pdf.py              # PDF loading and token chunking (TokenTextSplitter)
│   │       ├── text.py             # Text loading and character chunking (CharacterTextSplitter)
│   │       └── web_page.py         # Web-page loading (WebBaseLoader)
│   └── vectorstores/
│       └── vectorstore.py          # Vector store indexing, Chroma persistence, similarity search, and retrieval
├── .env.example                   # Placeholder environment variables
├── LICENSE
└── requirements.txt
```

## Before you start

- Python with `venv` and `pip`
- The packages listed in [`requirements.txt`](requirements.txt)
- API credentials for examples that call hosted models:
  - `OPENAI_API_KEY` for the OpenAI chat, embedding, and vector store examples
  - `HUGGINGFACEHUB_API_TOKEN` for the hosted Hugging Face example
- Internet access for hosted APIs, web-page loading, and initial model downloads

The local Hugging Face demo downloads
`TinyLlama/TinyLlama-1.1B-Chat-v1.0`, so make sure you’ve got enough disk space
and memory. The requirements also include PyTorch and related packages.

## Setup

First, clone the repo and hop into the project folder:

```bash
git clone https://github.com/AbhinavEliac/Genai_revision.git
cd Genai_revision
```

Next, create and activate a virtual environment:

**Windows PowerShell**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the dependencies and you’re nearly set:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create a local `.env` file from the template. On Windows PowerShell:

```powershell
Copy-Item .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

Swap the placeholders in `.env` for the credentials needed by the demos you
want to try. Keep your keys private: don’t commit a populated `.env` file or
paste API keys into source code.

| Variable | Used by |
| --- | --- |
| `OPENAI_API_KEY` | `chat.py`, `embeddings.py`, `movie_data_cleaner.py`, `RAG_project/main.py`, and `vectorstores/vectorstore.py` |
| `HUGGINGFACEHUB_API_TOKEN` | `chatmodels/huggingface.py` |
| `GROQ_API_KEY`, `GEMINI_API_KEY`, `MISTRAL_API_KEY` | Included in the template for provider experiments; not used by the current example scripts |

## Try the demos

Run these commands from the repo root with your virtual environment activated.
Every script is independent, so start wherever you like.

### Chat models

```bash
python chatmodels/chat.py
```

Sends a single prompt to `gpt-4o-mini` using LangChain's `init_chat_model`.

```bash
python chatmodels/chatbot.py
```

Starts a command-line conversation with one of three prompt personas: funny,
sad, or angry. Pick a mode when prompted, then enter `0` to wrap up and exit.

```bash
python chatmodels/huggingface.py
```

Calls a hosted Hugging Face model through LangChain's endpoint integration. You
need a Hugging Face token and access to a model endpoint.

```bash
python chatmodels/localmodel.py
```

Loads TinyLlama for local text generation. The first run may download the model
files, so it can take a little while.

### Embeddings

```bash
python embeddingmodels/embeddings.py
python embeddingmodels/hf_embeddings.py
```

Both demos embed a short list of sample questions and print the resulting
vectors. One uses OpenAI's `text-embedding-3-small`; the other loads
`BAAI/bge-small-en-v1.5` through Hugging Face.

### Projects

```bash
python Projects/movie_data_cleaner.py
```

Enter a movie description and `gpt-4o-mini` extracts details like the title,
rating, director, release year, genres, and a short summary. A Pydantic schema
and LangChain output-parser instructions keep the result structured.

```bash
python Projects/RAG_project/main.py
```

Loads a PDF, chunks it using `RecursiveCharacterTextSplitter`, and sends the prompt
to `gpt-4o-mini` for a bullet-point summary. Check
[Notes and limitations](#notes-and-limitations) before running this one.

The document-loader and text-splitter examples can be run separately:

```bash
python Projects/RAG_project/document_loaders/pdf.py
python Projects/RAG_project/document_loaders/text.py
python Projects/RAG_project/document_loaders/web_page.py
```

- `pdf.py`: Loads a PDF using `PyPDFLoader` and splits it into chunks with `TokenTextSplitter` (`chunk_size=100`, `chunk_overlap=10`).
- `text.py`: Loads a UTF-8 text file using `TextLoader` and splits it into chunks with `CharacterTextSplitter` (`chunk_size=100`, `chunk_overlap=10`).
- `web_page.py`: Fetches a web page using `WebBaseLoader` and prints its extracted text.

### Vector stores & retrieval

```bash
python Projects/vectorstores/vectorstore.py
```

Demonstrates persistent vector indexing and similarity retrieval using Chroma:
1. **Document Loading**: Loads a PDF via `PyPDFLoader`.
2. **Text Chunking**: Splits content into manageable chunks using `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=100`).
3. **Embeddings & Persistence**: Embeds chunks using OpenAI's `OpenAIEmbeddings` and persists the vector index to a local directory (`chroma-db/`).
4. **Similarity Search**: Performs nearest-neighbor similarity search (`vectorstore.similarity_search`).
5. **Retriever Interface**: Converts the store into a LangChain retriever (`vectorstore.as_retriever()`) and fetches relevant chunks via `retriever.invoke()`.

## Notes and limitations

- **Building towards a complete RAG pipeline.** Document loading, text
  chunking, embedding generation, Chroma vector storage, and similarity retrieval
  are now set up. The remaining step for an end-to-end question-answering RAG system
  is passing the retrieved chunks dynamically into a generation prompt chain.
- **Check file paths before running.** The scripts in `RAG_project` and
  `vectorstores` use absolute Windows paths in their `filepath` variables. Update
  the paths in the scripts to match your local repository clone if running from a
  different directory or machine.
- **Vector store persistence.** `vectorstore.py` writes to a local `chroma-db/`
  directory (ignored by Git). Delete or re-initialize this directory if you switch
  embedding models or change input documents.
- **The summarization script passes the first page.** Although `main.py`
  generates recursive character chunks, it currently passes the first page's text
  to the model for summarization.
- **Hosted model IDs and availability can change.** A model or endpoint
  may require access approval or may no longer be served under the identifier in
  the example.
- **The demos print output directly.** They don’t include a web interface,
  persistent conversation store, or production error handling.
- `requirements.txt` lists dependencies without version pins. Installing it may
  resolve newer package versions than those used when the examples were written.

## License

This project is distributed under the [MIT License](LICENSE).
