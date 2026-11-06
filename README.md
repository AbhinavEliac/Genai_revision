# GenAI Revision

Curious about generative AI? This repo is a hands-on playground of small,
runnable Python examples built around GenAI and the LangChain ecosystem. You’ll
find chat models, Hugging Face integrations, embeddings, structured extraction,
document loading, and a starter PDF summarization demo.

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
│   └── RAG_project/
│       ├── main.py                 # PDF loading and LLM summarization example
│       ├── covariance_vs_correlation.txt
│       ├── deep_learning_and_transformers.pdf
│       └── document_loaders/
│           ├── pdf.py              # PDF loading and text chunking
│           ├── text.py             # Text-file loading and chunking
│           └── web_page.py         # Web-page loading
├── .env.example                   # Placeholder environment variables
├── LICENSE
└── requirements.txt
```

## Before you start

- Python with `venv` and `pip`
- The packages listed in [`requirements.txt`](requirements.txt)
- API credentials for examples that call hosted models:
  - `OPENAI_API_KEY` for the OpenAI chat and embedding examples
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
| `OPENAI_API_KEY` | `chat.py`, `embeddings.py`, `movie_data_cleaner.py`, and `RAG_project/main.py` |
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

Loads a PDF and sends its first page to `gpt-4o-mini` for a summary. Check
[Notes and limitations](#notes-and-limitations) before running this one.

The document-loader examples can be run separately:

```bash
python Projects/RAG_project/document_loaders/pdf.py
python Projects/RAG_project/document_loaders/text.py
python Projects/RAG_project/document_loaders/web_page.py
```

The PDF and text demos load a document, split it into chunks, and print them.
The web demo fetches a page and prints its extracted text.

## Notes and limitations

- **This isn’t a full RAG pipeline yet.** The project demonstrates document
  loading and text splitting, but it does not create embeddings, store vectors,
  retrieve relevant chunks, or ground an answer in retrieved context.
- **Check the PDF path before running.** The RAG scripts use absolute Windows
  paths in their `filepath` variables. Update the path in the script to a PDF
  available on your machine. The repository includes
  `Projects/RAG_project/deep_learning_and_transformers.pdf`.
- **The summarization script only processes the first page.** Although the
  script creates chunks, it currently passes the first page's text to the model
  rather than summarizing all pages or using those chunks.
- **Hosted model IDs and availability can change.** A model or endpoint
  may require access approval or may no longer be served under the identifier in
  the example.
- **The demos print output directly.** They don’t include a web interface,
  persistent conversation store, or production error handling.
- `requirements.txt` lists dependencies without version pins. Installing it may
  resolve newer package versions than those used when the examples were written.

## License

This project is distributed under the [MIT License](LICENSE).
