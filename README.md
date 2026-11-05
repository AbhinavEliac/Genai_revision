# GenAI Revision

A collection of small, runnable Python examples for exploring generative AI and
the LangChain ecosystem. The repository covers chat models, Hugging Face model
integrations, embeddings, structured extraction, document loading, and a basic
PDF summarization example.

These are learning examples rather than a single packaged application. Each
script is run independently, and some require API credentials, model downloads,
internet access, or a local file path adjustment.

## Contents

- [Repository layout](#repository-layout)
- [Requirements](#requirements)
- [Setup](#setup)
- [Examples](#examples)
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

## Requirements

- Python with `venv` and `pip`
- The packages listed in [`requirements.txt`](requirements.txt)
- API credentials for examples that call hosted models:
  - `OPENAI_API_KEY` for the OpenAI chat and embedding examples
  - `HUGGINGFACEHUB_API_TOKEN` for the hosted Hugging Face example
- Internet access for hosted APIs, web-page loading, and initial model downloads

The local Hugging Face model example downloads `TinyLlama/TinyLlama-1.1B-Chat-v1.0`
and may require substantial disk space and memory. The requirements also include
PyTorch and related packages.

## Setup

Clone the repository and enter its directory:

```bash
git clone https://github.com/AbhinavEliac/Genai_revision.git
cd Genai_revision
```

Create and activate a virtual environment.

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

Install the dependencies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Create a local `.env` file from the template. In PowerShell:

```powershell
Copy-Item .env.example .env
```

On macOS or Linux:

```bash
cp .env.example .env
```

Replace the placeholder values in `.env` with the credentials needed for the
examples you intend to run. Never commit a populated `.env` file or paste API
keys into source code.

| Variable | Used by |
| --- | --- |
| `OPENAI_API_KEY` | `chat.py`, `embeddings.py`, `movie_data_cleaner.py`, and `RAG_project/main.py` |
| `HUGGINGFACEHUB_API_TOKEN` | `chatmodels/huggingface.py` |
| `GROQ_API_KEY`, `GEMINI_API_KEY`, `MISTRAL_API_KEY` | Included in the template for provider experiments; not used by the current example scripts |

## Examples

Run commands from the repository root with the virtual environment activated.
Each script is independent.

### Chat models

```bash
python chatmodels/chat.py
```

Sends a single prompt to `gpt-4o-mini` using LangChain's `init_chat_model`.

```bash
python chatmodels/chatbot.py
```

Starts a command-line conversation with one of three prompt personas: funny,
sad, or angry. Select a mode when prompted; enter `0` in the conversation to
exit.

```bash
python chatmodels/huggingface.py
```

Calls a hosted Hugging Face model through LangChain's endpoint integration. It
requires a Hugging Face token and a model endpoint that is available to the
account.

```bash
python chatmodels/localmodel.py
```

Loads the TinyLlama model for local text generation. The first run may download
the model files.

### Embeddings

```bash
python embeddingmodels/embeddings.py
python embeddingmodels/hf_embeddings.py
```

Both examples embed a short list of sample questions and print the resulting
vectors. The first uses OpenAI's `text-embedding-3-small`; the second loads
`BAAI/bge-small-en-v1.5` through Hugging Face.

### Projects

```bash
python Projects/movie_data_cleaner.py
```

Prompts for a movie description and asks `gpt-4o-mini` to extract fields such as
title, rating, director, release year, genres, and a short summary. The output
format is guided by a Pydantic schema and LangChain's output-parser instructions.

```bash
python Projects/RAG_project/main.py
```

Loads a PDF and sends its first page's text to `gpt-4o-mini` for a summary. See
[Notes and limitations](#notes-and-limitations) before running this example.

The document-loader examples can be run separately:

```bash
python Projects/RAG_project/document_loaders/pdf.py
python Projects/RAG_project/document_loaders/text.py
python Projects/RAG_project/document_loaders/web_page.py
```

The PDF and text examples load a document, split it into chunks, and print the
chunks. The web example fetches a page and prints its extracted text.

## Notes and limitations

- **This is not yet a complete RAG pipeline.** The project demonstrates document
  loading and text splitting, but it does not create embeddings, store vectors,
  retrieve relevant chunks, or ground an answer in retrieved context.
- **Check the PDF path before running.** The RAG scripts use absolute Windows
  paths in their `filepath` variables. Update the path in the script to a PDF
  available on your machine. The repository includes
  `Projects/RAG_project/deep_learning_and_transformers.pdf`.
- **The summarization script processes only the first page.** Although the
  script creates chunks, it currently passes the first page's text to the model
  rather than summarizing all pages or using those chunks.
- **Hosted model identifiers and availability can change.** A model or endpoint
  may require access approval or may no longer be served under the identifier in
  the example.
- **The examples print output directly.** They do not include a web interface,
  persistent conversation store, or production error handling.
- `requirements.txt` lists dependencies without version pins. Installing it may
  resolve newer package versions than those used when the examples were written.

## License

This project is distributed under the [MIT License](LICENSE).
