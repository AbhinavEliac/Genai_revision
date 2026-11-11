# 🚀 GenAI Revision // The Hands-On Playground

> *Hey folks! Welcome to the repo. Cut through the AI hype and dive straight into clean, bite-sized, runnable Python scripts built around LangChain, OpenAI, Hugging Face, and Chroma. Let’s get our hands dirty.*

---

Welcome to **GenAI Revision**! We put this repo together as a straightforward, no-nonsense sandbox to brush up on everything Generative AI—from zero-shot LLM prompts to high-dimensional embeddings, structured data extraction, and on-disk vector stores.

Instead of dumping a bloated, monolithic app on your lap, every single script in here is designed to run independently right out of the box. Pick a demo, punch in your API keys, and start hacking.

Let's dive right in!

## What's on the Menu

- [Repo Layout & File Tree](#repo-layout--file-tree)
- [Before You Jump In (Prerequisites)](#before-you-jump-in-prerequisites)
- [Quickstart Setup Guide](#quickstart-setup-guide)
- [Test-Driving the Demos](#test-driving-the-demos)
  - [1. Chat Models & Conversational Bots](#1-chat-models--conversational-bots)
  - [2. Embedding Models & Semantic Search](#2-embedding-models--semantic-search)
  - [3. End-to-End Projects](#3-end-to-end-projects)
  - [4. Vector Stores & Similarity Retrieval (Chroma DB)](#4-vector-stores--similarity-retrieval-chroma-db)
- [Heads Up & Known Gotchas](#heads-up--known-gotchas)
- [License](#license)

## Repo Layout & File Tree

Here's a bird's-eye view of how the project is laid out:

```text
.
├── chatmodels/
│   ├── chat.py                     # Quick zero-shot chat completion via LangChain's init_chat_model
│   ├── chatbot.py                  # CLI multi-turn chatbot packing 3 wild personalities (funny, sad, angry)
│   ├── huggingface.py              # Hosted cloud inference hitting the Hugging Face Hub
│   └── localmodel.py               # Running TinyLlama bare-metal right on your local hardware
├── embeddingmodels/
│   ├── embeddings.py               # Grabbing high-dimensional vectors with OpenAI text-embedding-3-small
│   └── hf_embeddings.py            # Local embeddings on the fly using BAAI/bge-small-en-v1.5
├── Projects/
│   ├── movie_data_cleaner.py       # Wrangling messy movie reviews into rock-solid Pydantic schemas
│   ├── RAG_project/
│   │   ├── main.py                 # PDF ingestion, smart recursive chunking, and AI summarization
│   │   ├── create_db.py            # Ingestion script chunking documents into persistent Chroma vector DB
│   │   ├── covariance_vs_correlation.txt # Comprehensive stats cheat sheet for quick reference
│   │   ├── deep-learning-material-dept-ece-ase-blr-1.pdf # Full-blown deep learning coursebook (21 MB)
│   │   ├── deep_learning_and_transformers.pdf           # Handy architectural primer on transformers
│   │   └── document_loaders/
│   │       ├── pdf.py              # PDF parsing and token-based chunking with TokenTextSplitter
│   │       ├── text.py             # Slicing plain text files with CharacterTextSplitter
│   │       └── web_page.py         # Scraping web pages and stripping HTML via WebBaseLoader
│   └── vectorstores/
│       └── vectorstore.py          # End-to-end vector indexing, Chroma persistence, and k-NN retrieval
├── .env.example                   # Boilerplate template for your secret API keys
├── LICENSE                         # Permissive MIT license
└── requirements.txt                # All the Python goodies needed to get rolling
```

## Before You Jump In (Prerequisites)

Before you hit the ground running, make sure your machine has the right gear:

- **Python Setup**: Python 3.10+ installed and ready, along with standard `pip` and `venv`.
- **The Dependencies**: All the required packages listed in [`requirements.txt`](requirements.txt).
- **Hardware & Memory (Don't melt your laptop!)**:
  - Running [`chatmodels/localmodel.py`](chatmodels/localmodel.py) downloads `TinyLlama/TinyLlama-1.1B-Chat-v1.0` directly to your local drive.
  - Make sure you've got at least 8 GB of free RAM, some spare disk space, and working PyTorch support so you don't run into nasty Out-Of-Memory crashes.
- **API Keys & Credentials**:
  - `OPENAI_API_KEY`: A must-have for OpenAI chat, embeddings, and the Chroma retrieval demos.
  - `HUGGINGFACEHUB_API_TOKEN`: Needed if you're hitting hosted Hugging Face endpoints.
- **A Solid Internet Connection**: For pulling down model weights, hitting cloud APIs, and scraping web pages.

## Quickstart Setup Guide

Let’s get your environment spun up and ready to rock in four quick steps.

### Step 1: Grab the Repo

Pop open your terminal, clone the repo, and jump right in:

```bash
git clone https://github.com/AbhinavEliac/Genai_revision.git
cd Genai_revision
```

### Step 2: Fire Up a Virtual Environment

Always sandbox your dependencies so you don't trash your system Python:

**On Windows (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**On macOS / Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install the Goodies

Upgrade `pip` and pull down all the required packages:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4: Stash Your Secret Keys in `.env`

Copy over the sample environment template:

**On Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**On macOS / Linux:**

```bash
cp .env.example .env
```

Now crack open `.env` in your favorite editor (VS Code, Notepad, whatever floats your boat) and paste in your real API keys.

> 🔒 **Pro Tip / Security Check:** Never, ever commit your real `.env` file to Git or drop it into a public Discord or Slack channel. Treat your API keys like your house keys.

| Secret Key | What It Powers |
| :--- | :--- |
| `OPENAI_API_KEY` | Fuels `chat.py`, `embeddings.py`, `movie_data_cleaner.py`, `RAG_project`, and `vectorstores/vectorstore.py` |
| `HUGGINGFACEHUB_API_TOKEN` | Required strictly for `chatmodels/huggingface.py` |
| `GROQ_API_KEY`, `GEMINI_API_KEY`, `MISTRAL_API_KEY` | Included in the template for future playground experiments |

## Test-Driving the Demos

Once your virtual env is active and your keys are locked and loaded, you're good to go. Make sure to run all commands straight from the repository root.

### 1. Chat Models & Conversational Bots

#### Quick-and-Dirty Zero-Shot Chat

```bash
python chatmodels/chat.py
```

Shoots a quick prompt over to `gpt-4o-mini` using LangChain's sleek `init_chat_model` helper. Perfect for a quick sanity check to make sure your OpenAI pipe is working.

#### CLI Persona Chatbot

```bash
python chatmodels/chatbot.py
```

Fires up an interactive terminal chat session with attitude. Pick your flavor: *funny*, *sad*, or *angry*. When you're ready to call it quits, just punch in `0` to wrap up and exit.

#### Cloud Hugging Face Inference

```bash
python chatmodels/huggingface.py
```

Taps into cloud-hosted Hugging Face models using LangChain's Hub integration. Double-check that your Hugging Face token has inference permissions before running this one.

#### Running Local Models On Your Own Metal

```bash
python chatmodels/localmodel.py
```

Loads `TinyLlama-1.1B` straight into local memory for offline text generation. The first spin will take a few minutes while it downloads the model weights from Hugging Face, so grab a coffee!

### 2. Embedding Models & Semantic Search

```bash
python embeddingmodels/embeddings.py
python embeddingmodels/hf_embeddings.py
```

Turn natural language strings into high-dimensional vector coordinates:
- `embeddings.py`: Taps into OpenAI's snappy `text-embedding-3-small` model to cook up 1536-dimensional vectors.
- `hf_embeddings.py`: Computes dense embeddings 100% locally with the popular `BAAI/bge-small-en-v1.5` sentence transformer.

### 3. End-to-End Projects

#### Wrangling Messy Data with Pydantic

```bash
python Projects/movie_data_cleaner.py
```

Feeds rambling, unstructured movie descriptions to `gpt-4o-mini` and forces the LLM to spit out structured, strictly validated data matching a Pydantic schema (movie title, director, release year, rating, and genres).

#### PDF Summarization Pipeline

```bash
python Projects/RAG_project/main.py
```

Slurps up a PDF, breaks it down into chunks using `RecursiveCharacterTextSplitter`, and asks the LLM to kick back a clean, bulleted executive summary.

#### Standalone Document Loaders & Splitters

Want to kick the tires on document loading and chunking in isolation? Run these:

```bash
python Projects/RAG_project/document_loaders/pdf.py
python Projects/RAG_project/document_loaders/text.py
python Projects/RAG_project/document_loaders/web_page.py
```

- `pdf.py`: Cracks open a PDF using `PyPDFLoader` and slices it into token-based windows using `TokenTextSplitter` (`chunk_size=100`, `chunk_overlap=10`).
- `text.py`: Ingests a UTF-8 text file with `TextLoader` and chunks it using `CharacterTextSplitter`.
- `web_page.py`: Fetches any live URL using `WebBaseLoader` (powered by BeautifulSoup) and strips out the noise to grab pure readable text.

### 4. Vector Stores & Similarity Retrieval (Chroma DB)

```bash
python Projects/vectorstores/vectorstore.py
```

A complete, production-style vector indexing and retrieval pipeline powered by Chroma:
1. **Document Loading**: Ingests our PDF via `PyPDFLoader`.
2. **Text Chunking**: Chops the document into bite-sized segments with `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=100`).
3. **Embedding & Storage**: Computes OpenAI embeddings and saves the vector index locally into the `chroma-db/` folder.
4. **Similarity Search**: Runs nearest-neighbor search (`vectorstore.similarity_search`) to grab the most relevant chunks.
5. **Retriever Mode**: Converts the vector store into a full-fledged LangChain retriever (`vectorstore.as_retriever()`) and pulls context with `retriever.invoke()`.

## Heads Up & Known Gotchas

Here are a few quick practical tips to keep you out of trouble:

- **Heads Up on RAG Scope**: We've got document ingestion, chunking, embeddings, Chroma storage, and vector retrieval all wired up. The next step to build a full question-answering RAG app is plugging the retrieved context dynamically into a final generation prompt.
- **Double-Check Local File Paths**: Some scripts use absolute Windows paths in the `filepath` variable for quick local testing. Be sure to swap in the path that matches your machine's setup before running.
- **Local Chroma DB Folders**: Running the vector store scripts will create local database directories (`chroma-db/` and `rag-project-chroma-db/`). These are already tucked away in `.gitignore` so you don't commit chunky binary files. If you change your documents or switch embedding models, just blow away these folders and regenerate fresh.
- **Quick Sanity Check in `main.py`**: Although `main.py` creates recursive chunks, it currently passes the first page (`docs[0]`) to the model for a quick sanity check. Feel free to tweak the prompt input to loop through whatever chunks you want.
- **Hosted Model Availability**: Cloud endpoints on Hugging Face and OpenAI can change, deprecate, or experience downtime. If a call fails, double-check your API quotas and endpoint status.
- **Raw Console Output**: Everything prints straight to `stdout` for fast debugging. No fancy web UI or heavyweight server needed—just pure, simple terminal output.
- **Loose Package Versions**: `requirements.txt` leaves versions unpinned so you get the latest compatible goodies from the LangChain ecosystem.

## License

This project is open-sourced under the friendly and permissive [MIT License](LICENSE). Feel free to fork it, hack on it, and build cool stuff with it.

Got questions or ran into a bug? Feel free to open an issue or drop a PR.

Happy hacking! 🚀
