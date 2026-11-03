<div align="center">

# 🧠 GenAI Revision Repository

<p align="center">
  <strong>Comprehensive revision repository for Generative AI, Large Language Models (LLMs), LangChain, Vector Embeddings, and Real-world NLP Projects.</strong>
</p>

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![LangChain](https://img.shields.io/badge/LangChain-v0.3%2B-1C3C3C?logo=langchain&logoColor=white)](https://python.langchain.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?logo=openai&logoColor=white)](https://openai.com/)
[![HuggingFace](https://img.shields.io/badge/HuggingFace-Models%20%26%20Endpoints-FFD21E?logo=huggingface&logoColor=black)](https://huggingface.co/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub](https://img.shields.io/badge/GitHub-AbhinavEliac-181717?logo=github&logoColor=white)](https://github.com/AbhinavEliac/Genai_revision)

---

### 👤 Author Information

| 🏷️ Detail | 📌 Information |
| :--- | :--- |
| **Author** | **Abhinav Gupta** |
| **Email** | [![Email](https://img.shields.io/badge/Email-abhinavgupta15.ag%40gmail.com-D14836?logo=gmail&logoColor=white)](mailto:abhinavgupta15.ag@gmail.com) |
| **GitHub Profile** | [![GitHub Profile](https://img.shields.io/badge/GitHub-AbhinavEliac-181717?logo=github&logoColor=white)](https://github.com/AbhinavEliac) |
| **Repository** | [![Repo](https://img.shields.io/badge/Repo-Genai__revision-blue?logo=git&logoColor=white)](https://github.com/AbhinavEliac/Genai_revision) |

---

</div>

## 📖 Overview

This repository serves as a focused, hands-on revision guide for core **Generative AI** concepts, workflows, and integrations. It covers:

- **Chat Models & LLM Orchestration**: Unified model initialization using LangChain `init_chat_model`, multi-turn conversational agents with stateful message history, and persona-driven system prompts.
- **Remote & Local Inference**: Interfacing with OpenAI cloud models, Hugging Face Serverless Endpoints (`deepseek-ai/DeepSeek-V4.1-Flash-1017`), and local Hugging Face pipelines (`TinyLlama/TinyLlama-1.1B-Chat-v1.0`).
- **Vector Embeddings**: Generating dense vector representations using both proprietary APIs (OpenAI `text-embedding-3-small`) and open-source embedding models (`BAAI/bge-small-en-v1.5`).
- **Applied GenAI Projects**: Practical end-to-end applications demonstrating advanced prompt engineering, deterministic extraction, and structured output parsing.

---

## 📂 Repository Structure

```text
Genai_revision/
│
├── chatmodels/
│   ├── chat.py                 # Basic LangChain chat model invocation with GPT-4o-mini
│   ├── chatbot.py              # Interactive "ChatBot 360" multi-persona agent with session memory
│   ├── huggingface.py          # HuggingFace Serverless Endpoint integration (DeepSeek)
│   └── localmodel.py           # On-device local inference via Hugging Face Pipeline (TinyLlama)
│
├── embeddingmodels/
│   ├── embeddings.py           # OpenAI dense vector embeddings (text-embedding-3-small)
│   └── hf_embeddings.py        # Open-source Hugging Face embeddings (bge-small-en-v1.5)
│
├── Projects/
│   └── movie_data_cleaner.py   # Structured Movie Information Extractor using ChatPromptTemplate
│
├── .env.example                # Environment variables template for API keys
├── .gitignore                  # Git ignore rules for environments, secrets, and caches
├── .gitkeep                   # Placeholder keeping repository directory structure intact
├── LICENSE                     # MIT License
├── README.md                   # Project documentation and guide
└── requirements.txt            # Full list of dependencies (LangChain, PyTorch, Transformers, etc.)
```

---

## 🛠️ Modules & Features

### 1. 💬 Chat Models (`chatmodels/`)

- **`chat.py`**:
  Demonstrates quick LLM abstraction using LangChain's `init_chat_model` with temperature and max token configurations.
- **`chatbot.py` (`ChatBot 360`)**:
  A multi-persona CLI conversational bot. Users can select personality modes:
  - `1`: 🎭 **Hilarious AI Agent** (Comedic, playful tone)
  - `2`: 😢 **Sad AI Agent** (Melancholic tone)
  - `3`: 😠 **Angry AI Agent** (Gruff, impatient tone)
  Maintains conversational context using LangChain `SystemMessage`, `HumanMessage`, and `AIMessage`.
- **`huggingface.py`**:
  Cloud endpoint execution leveraging `ChatHuggingFace` and `HuggingFaceEndpoint` without requiring local GPU hardware.
- **`localmodel.py`**:
  Offline, on-device execution using HuggingFace's `pipeline` and `HuggingFacePipeline` with quantized or lightweight models (e.g., TinyLlama 1.1B).

### 2. 🧬 Embedding Models (`embeddingmodels/`)

- **`embeddings.py`**:
  Uses `OpenAIEmbeddings` (`text-embedding-3-small`) with custom dimensional output (e.g., 64-dim) to generate dense vector embeddings for semantic search and retrieval.
- **`hf_embeddings.py`**:
  Uses local/open-source `HuggingFaceEmbeddings` with `BAAI/bge-small-en-v1.5` for cost-effective, high-accuracy semantic embeddings.

### 3. 🎬 Applied GenAI Projects (`Projects/`)

- **`movie_data_cleaner.py` (Structured Movie Information Extractor)**:
  - Uses `ChatPromptTemplate.from_messages` to construct strict system instructions and dynamic prompt variables (`{paragraph}`).
  - Employs zero-temperature (`temperature=0`) inference with `gpt-4o-mini` for deterministic, hallucination-free output.
  - Automatically parses messy, unstructured movie summaries into a clean, standardized format:
    - Title, Director, Release Date, Genre, Plot, Theme, Setting/Location, Lead Actors, and Plot Summary.
    - Handles missing data gracefully with `Null` indicators without inventing facts.

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/AbhinavEliac/Genai_revision.git
cd Genai_revision
```

### 2. Set Up a Virtual Environment

```bash
# Windows
python -m venv env
.\env\Scripts\activate

# macOS / Linux
python3 -m venv env
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy the `.env.example` file to `.env` and fill in your API credentials:

```bash
cp .env.example .env
```

Edit `.env`:

```env
OPENAI_API_KEY=your_openai_api_key_here
GROQ_API_KEY=your_groq_api_key_here
GEMINI_API_KEY=your_gemini_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_token_here
```

---

## 💻 Running the Examples

### 🤖 ChatBot 360 (Multi-Persona Conversational Bot)

```bash
python chatmodels/chatbot.py
```

### 💬 Basic Chat Invocation

```bash
python chatmodels/chat.py
```

### 🤗 Hugging Face Cloud Inference

```bash
python chatmodels/huggingface.py
```

### 🖥️ Local Model Inference

```bash
python chatmodels/localmodel.py
```

### 📐 Generating Embeddings

```bash
# OpenAI Embeddings
python embeddingmodels/embeddings.py

# Hugging Face Embeddings
python embeddingmodels/hf_embeddings.py
```

### 🎬 Movie Data Cleaner & Information Extractor

```bash
python Projects/movie_data_cleaner.py
```

---

## 📬 Contact & Support

Created by **Abhinav Gupta** — feel free to reach out for collaborations, discussions, or questions!

- **Email**: [abhinavgupta15.ag@gmail.com](mailto:abhinavgupta15.ag@gmail.com)
- **GitHub**: [@AbhinavEliac](https://github.com/AbhinavEliac)
- **Repo**: [Genai_revision](https://github.com/AbhinavEliac/Genai_revision)

---

<div align="center">
  <sub>Built with ❤️ for GenAI Mastery & Continuous Learning.</sub>
</div>
