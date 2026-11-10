# GenAI Revision // End-to-End Implementation Repository

> *Respected Developers and Colleagues: Kindly find below a comprehensive repository containing hands-on, end-to-end Python implementations for GenAI and LangChain ecosystem revision. Please go through the documentation and do the needful for local setup.*

---

Welcome to the **GenAI Revision** repository. This initiative has been developed with the primary objective of providing practical, module-wise revision on Generative AI concepts, foundation models, and LangChain orchestration.

Instead of deploying one single bulky monolithic application, we have deliberately structured this as independent, plug-and-play Python scripts. Each script is self-contained only, so that you can run, debug, and understand the core logic without any confusion. Kindly note that certain scripts require third-party API credentials, local model weight downloads, and proper internet connectivity.

Please find below the detailed walkthrough for your kind reference.

## Table of Contents

- [Project Architecture & Directory Hierarchy](#project-architecture--directory-hierarchy)
- [Pre-requisites & Machine Specifications](#pre-requisites--machine-specifications)
- [Step-by-Step Environment Setup Guide](#step-by-step-environment-setup-guide)
- [Module-wise Execution & Demo Walkthrough](#module-wise-execution--demo-walkthrough)
  - [1. Chat Models & Conversational Agents](#1-chat-models--conversational-agents)
  - [2. Embedding Models & Vector Projections](#2-embedding-models--vector-projections)
  - [3. End-to-End Applied Projects](#3-end-to-end-applied-projects)
  - [4. Vector Store Implementation & Similarity Search (Chroma)](#4-vector-store-implementation--similarity-search-chroma)
- [Crucial Points & Limitations to be Kept in Mind](#crucial-points--limitations-to-be-kept-in-mind)
- [Licensing & Usage Terms](#licensing--usage-terms)

## Project Architecture & Directory Hierarchy

Kindly take a look at the below folder structure to understand the module placement properly:

```text
.
├── chatmodels/
│   ├── chat.py                     # Basic chat completion using LangChain's init_chat_model
│   ├── chatbot.py                  # Multi-turn interactive chatbot featuring three distinct personas
│   ├── huggingface.py              # Hosted inference via Hugging Face Hub endpoint integration
│   └── localmodel.py               # Local execution of TinyLlama model directly on machine hardware
├── embeddingmodels/
│   ├── embeddings.py               # Dense vector generation utilizing OpenAI text-embedding-3-small
│   └── hf_embeddings.py            # Local embeddings pipeline using BAAI/bge-small-en-v1.5
├── Projects/
│   ├── movie_data_cleaner.py       # Extraction of structured JSON from unstructured text into Pydantic schema
│   ├── RAG_project/
│   │   ├── main.py                 # PDF loading, recursive character chunking, and executive summarization
│   │   ├── create_db.py            # Ingestion script to chunk and persist document vectors into Chroma DB
│   │   ├── covariance_vs_correlation.txt # In-depth descriptive statistical guide prepared for reference
│   │   ├── deep-learning-material-dept-ece-ase-blr-1.pdf # Comprehensive deep learning course document
│   │   ├── deep_learning_and_transformers.pdf           # Transformer architectural notes PDF
│   │   └── document_loaders/
│   │       ├── pdf.py              # PDF document loading and token-based chunking (TokenTextSplitter)
│   │       ├── text.py             # Plain text ingestion and chunking (CharacterTextSplitter)
│   │       └── web_page.py         # Web scraping and DOM text extraction via WebBaseLoader
│   └── vectorstores/
│       └── vectorstore.py          # End-to-end Chroma vector DB persistence, k-NN search, and retriever setup
├── .env.example                   # Standard template for secret environment variable keys
├── LICENSE                         # Permissive MIT License terms
└── requirements.txt                # Consolidated package requirements list
```

## Pre-requisites & Machine Specifications

Before initiating the execution, request you to kindly cross-check whether your local workstation meets the following technical pre-requisites:

- **Python Environment**: Python version 3.10 or higher must be pre-installed on the system along with standard `pip` and `venv` support.
- **Package Inventory**: All required third-party libraries mentioned in [`requirements.txt`](requirements.txt) should be installed on priority basis.
- **Hardware & Memory Requirements**: 
  - For running [`chatmodels/localmodel.py`](chatmodels/localmodel.py), the `TinyLlama/TinyLlama-1.1B-Chat-v1.0` model weights will get downloaded locally.
  - Kindly ensure sufficient free RAM (minimum 8 GB recommended), adequate disk space, and PyTorch compatibility so that no out-of-memory issue will arise.
- **Secret Credentials & API Access**:
  - `OPENAI_API_KEY`: Required on priority for OpenAI chat models, vector embeddings, and Chroma retrieval workflows.
  - `HUGGINGFACEHUB_API_TOKEN`: Mandatory for invoking remote hosted endpoints on the Hugging Face Hub.
- **High-Speed Internet Connectivity**: Active internet connection is required for initial model downloads, hosted API calls, and web scraping utilities.

## Step-by-Step Environment Setup Guide

Kindly follow the below step-by-step procedure in sequential order to avoid any dependency conflicts or environment issues:

### Step 1: Clone the Codebase onto Your System

First and foremost, please open your terminal and clone the repository locally:

```bash
git clone https://github.com/AbhinavEliac/Genai_revision.git
cd Genai_revision
```

### Step 2: Create and Activate a Fresh Virtual Environment

In order to keep the system packages clean and isolated, request you to kindly create a dedicated virtual environment:

**For Windows Users (PowerShell):**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**For macOS / Linux Users:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Upgrade Pip and Install Necessary Packages

Kindly run the below commands to upgrade `pip` and install all project dependencies without any hitch:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Step 4: Configure the Environment Variables File

Please do one thing: create a local `.env` configuration file by duplicating the provided sample template:

**For Windows (PowerShell):**

```powershell
Copy-Item .env.example .env
```

**For macOS / Linux:**

```bash
cp .env.example .env
```

Now, kindly open the `.env` file in your preferred editor and update the dummy placeholder values with your actual working API keys.

> **Kindly Note:** Under no circumstances should you commit your populated `.env` file to Git or share it over email/Slack. Please keep all secret keys confidential only.

| Environment Key | Required For |
| :--- | :--- |
| `OPENAI_API_KEY` | Used across `chat.py`, `embeddings.py`, `movie_data_cleaner.py`, `RAG_project`, and `vectorstores/vectorstore.py` |
| `HUGGINGFACEHUB_API_TOKEN` | Required strictly for `chatmodels/huggingface.py` |
| `GROQ_API_KEY`, `GEMINI_API_KEY`, `MISTRAL_API_KEY` | Available in template for future testing and upgradations; not utilized in current scripts |

## Module-wise Execution & Demo Walkthrough

Once your environment is properly activated and keys are in place, you may proceed with script execution. Kindly run all scripts directly from the project root directory.

### 1. Chat Models & Conversational Agents

#### Standard Zero-Shot Completion

```bash
python chatmodels/chat.py
```

Dispatches a straightforward prompt query to `gpt-4o-mini` using the unified `init_chat_model` interface of LangChain. Highly recommended for sanity testing of your OpenAI connection.

#### Interactive Persona Chatbot

```bash
python chatmodels/chatbot.py
```

Launches a command-line interactive chat session with built-in prompt personas: *funny*, *sad*, or *angry*. When prompted, kindly select your preferred persona option. Once testing is complete, please enter `0` to gracefully exit the conversation loop.

#### Hosted Hugging Face Model Integration

```bash
python chatmodels/huggingface.py
```

Invokes remote model endpoints hosted on Hugging Face infrastructure via LangChain's Hub integration. Please verify your token has proper inference access beforehand.

#### Local On-Premise Model Execution

```bash
python chatmodels/localmodel.py
```

Loads the `TinyLlama-1.1B` model directly into system memory for local text generation without sending data to external cloud services. During the initial run, model weights will get downloaded from Hugging Face, so kindly be patient for a few minutes.

### 2. Embedding Models & Vector Projections

```bash
python embeddingmodels/embeddings.py
python embeddingmodels/hf_embeddings.py
```

These scripts convert textual sentences into dense numerical coordinate vectors:
- `embeddings.py`: Utilizes OpenAI's standard `text-embedding-3-small` model to compute 1536-dimensional embeddings.
- `hf_embeddings.py`: Runs the popular `BAAI/bge-small-en-v1.5` sentence transformer model locally via Hugging Face embeddings.

### 3. End-to-End Applied Projects

#### Structured Data Extraction with Pydantic

```bash
python Projects/movie_data_cleaner.py
```

Takes unorganized, raw movie descriptions as input and leverages `gpt-4o-mini` along with LangChain output parsers to extract validated information into a strict Pydantic model (containing movie title, director, release year, rating, and parsed genres).

#### Document Summarization Pipeline

```bash
python Projects/RAG_project/main.py
```

Ingests a sample PDF document, chunks the extracted text using `RecursiveCharacterTextSplitter`, and prompts the LLM to generate a clean, bulleted executive summary.

#### Standalone Document Loaders & Text Splitters

In case you wish to test text chunking and parsing in isolation, kindly execute the respective scripts:

```bash
python Projects/RAG_project/document_loaders/pdf.py
python Projects/RAG_project/document_loaders/text.py
python Projects/RAG_project/document_loaders/web_page.py
```

- `pdf.py`: Loads the PDF using `PyPDFLoader` and splits pages into precise token windows via `TokenTextSplitter` (`chunk_size=100`, `chunk_overlap=10`).
- `text.py`: Loads a UTF-8 text file with `TextLoader` and splits into character chunks via `CharacterTextSplitter` (`chunk_size=100`, `chunk_overlap=10`).
- `web_page.py`: Fetches web content using `WebBaseLoader` (utilizing `bs4`) and extracts clean readable text.

### 4. Vector Store Implementation & Similarity Search (Chroma)

```bash
python Projects/vectorstores/vectorstore.py
```

Demonstrates a complete, professional vector search and retrieval workflow utilizing Chroma vector database:
1. **Document Loading**: Ingests the PDF using `PyPDFLoader`.
2. **Text Chunking**: Breaks large documents into manageable text slices with `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=100`).
3. **Embedding & On-Disk Storage**: Generates OpenAI embeddings and saves the vector index locally into the `chroma-db/` folder.
4. **Similarity Search**: Performs top-$k$ nearest-neighbor similarity search (`vectorstore.similarity_search`).
5. **Retriever Conversion**: Wraps the database as a standard LangChain retriever (`vectorstore.as_retriever()`) and queries it seamlessly via `retriever.invoke()`.

## Crucial Points & Limitations to be Kept in Mind

Kindly take note of the following operational points to ensure smooth execution without any hiccups:

- **RAG Pipeline Scope**: The present codebase demonstrates complete document ingestion, text chunking, vector embedding, Chroma storage, and retrieval. In order to achieve a 100% end-to-end question-answering system, the retrieved document chunks need to be piped dynamically into a final generation chain prompt.
- **Local File Paths**: Certain scripts have hardcoded absolute Windows paths in the `filepath` variable for initial convenience. Kindly update the file path according to your local machine directory structure before executing.
- **Chroma Storage Folders**: Scripts create local database folders (`chroma-db/` and `rag-project-chroma-db/`). These have already been added to `.gitignore` so that binary SQLite files will not get committed. In case you change documents or embedding models, kindly delete these folders and re-run.
- **Single Page Summarization Demo**: In `main.py`, although recursive chunking is fully performed, the current summary prompt passes `docs[0]` for immediate sanity check. You may modify the prompt input to iterate over all chunks as per your project requirement.
- **Third-Party Model Upgrades & Deprecations**: Hosted model IDs on Hugging Face and OpenAI are subject to provider availability and deprecation policies. In case an endpoint returns an error, kindly cross-verify model status on their respective developer portals.
- **Direct Terminal Output**: All scripts output results directly to `stdout` for rapid debugging. No separate frontend UI or backend server is deployed as this is strictly intended for revision and learning purposes.
- **Package Version Flexibility**: The `requirements.txt` file does not enforce strict version pins, allowing you to install the latest compatible updates from the LangChain ecosystem.

## Licensing & Usage Terms

This project is made available under the standard and permissive terms of the [MIT License](LICENSE). You are fully at liberty to clone, modify, and integrate these examples into your enterprise or personal projects.

In case of any doubts or clarifications, please feel free to open an issue or raise a pull request.

**Thanks and Regards,**  
*GenAI Revision Team*
