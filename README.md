# ⚔️ GenAI Revision // The Grand Armory of the Realm

> *“Hark, ye weary wanderers and valiant squires of the digital kingdom! Lay down thy rusty implements and gaze upon true steel. No courtly charlatans or hollow sorcery dwell here—only tempered Python blades, consecrated vector runes, and the noble craft of Generative Chivalry.”*

Draw near the blacksmith’s forge. **GenAI Revision** is a royal proving ground and sanctified armory of standalone Python implements, wrought to master the arcane mysteries of the LangChain order and the great Oracle Spirits of our age. Here, we strip away the deceptive perfumes of the royal court to wrestle directly with raw token flames, local warhorse steeds of silicon, mystical geometric projections, and subterranean parchment vaults.

Every scroll within this keep is an independent weapon of war. Each script stands upon its own honor—bidding thee furnish signet seals when summoned, demanding ample grain and memory of thy steed, and bellowing unvarnished battle heraldry directly into thy command terminal.

## 📜 The Royal Index of Tomes

- [The Heraldry of the Citadel](#-the-heraldry-of-the-citadel)
- [Tithes & Knightly Clearances](#-tithes--knightly-clearances)
- [Consecration of the Proving Grounds](#-consecration-of-the-proving-grounds)
- [Tournaments & Martial Demos](#-tournaments--martial-demos)
  - [I. The Whispering Oracles (Chat Models)](#i-the-whispering-oracles-chat-models)
  - [II. High Celestial Runes (Embeddings)](#ii-high-celestial-runes-embeddings)
  - [III. Crusades of the Realm (Projects)](#iii-crusades-of-the-realm-projects)
  - [IV. The Sunken Catacombs (Vector Stores)](#iv-the-sunken-catacombs-vector-stores)
- [Perils of the Quest & Dragon Hazards](#-perils-of-the-quest--dragon-hazards)
- [The Sovereign Charter](#-the-sovereign-charter)

## 🏰 The Heraldry of the Citadel

Behold the map of our ancestral fortress, chamber by chamber:

```text
.
├── chatmodels/
│   ├── chat.py                     # A swift, honorable parry: zero-shot consultation of the OpenAI Oracle
│   ├── chatbot.py                  # The Tavern Jester: an interactive automaton of three volatile tempers
│   ├── huggingface.py              # A carrier pigeon dispatched to distant Hugging Face strongholds
│   └── localmodel.py               # The Warhorse: TinyLlama stabled and stabled directly in local silicon
├── embeddingmodels/
│   ├── embeddings.py               # Inscribing words into high-dimensional geometric constellations via OpenAI
│   └── hf_embeddings.py            # The BGE runic cipher conjured from the Hugging Face monastery
├── Projects/
│   ├── movie_data_cleaner.py       # Imposing the iron law of Pydantic upon chaotic bardic tavern tales
│   ├── RAG_project/
│   │   ├── main.py                 # Distilling great scholarly scrolls into concise royal intelligence
│   │   ├── create_db.py            # Slicing the grand parchment and burying it into the Chroma crypts
│   │   ├── covariance_vs_correlation.txt # An exhaustive mathematical treatise for enlightened paladins
│   │   ├── deep-learning-material-dept-ece-ase-blr-1.pdf # The Grand Grimoire of Deep Learning (21MB of sacred lore)
│   │   ├── deep_learning_and_transformers.pdf           # The ancient parchment of Attention & Transformers
│   │   └── document_loaders/
│   │       ├── pdf.py              # The Cleaver of Scrolls: slicing tomes into precise token allotments
│   │       ├── text.py             # Slicing raw chronicle parchments along strict character borders
│   │       └── web_page.py         # Scouting enemy web fortifications via WebBaseLoader
│   └── vectorstores/
│       └── vectorstore.py          # The Vault of Templars: Chroma indexation, spatial jousting, and retrieval
├── .env.example                   # The parchment template of secret royal signet seals
├── LICENSE                         # The King's Holy MIT Charter of Chivalric Freedom
└── requirements.txt                # The inventory of rations and provisions for the campaign
```

## 🗝️ Tithes & Knightly Clearances

Before thou shalt unsheathe these blades, certify that thy castle battlements possess the requisite provisions:

- **Thy Steed’s Engine**: Python 3.10 or higher, armed with `venv` and the trusty `pip` courier.
- **The Armory Manifest**: The holy supplies cataloged within [`requirements.txt`](requirements.txt).
- **Thy Warhorse’s Stables (VRAM & Silicon)**: The local beast in `localmodel.py` summoneth `TinyLlama/TinyLlama-1.1B-Chat-v1.0` straight into thy machine’s memory. Ensure thine iron harness hath sufficient RAM, disk space, and PyTorch armor plates.
- **Royal Signet Seals (API Keys)**: Remote Oracles demand proof of royal lineage:
  - `OPENAI_API_KEY`: Bestows passage to consult OpenAI oracles, craft rune embeddings, and scour Chroma vaults.
  - `HUGGINGFACEHUB_API_TOKEN`: The encrypted sigil required to petition distant Hugging Face towers.
- **The Royal Courier’s Road**: An open internet bridge to summon model weights from across the seas and commune with cloud spires.

## ⚙️ Consecration of the Proving Grounds

### 1. Infiltrate the Outer Courtyard

Ride forth and clone the ancestral keep unto thine own estate:

```bash
git clone https://github.com/AbhinavEliac/Genai_revision.git
cd Genai_revision
```

### 2. Erect a Holy Warding Circle (Virtual Chamber)

Lest conflicting potions poison thy king's land, establish a sanctified virtual grove:

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

### 3. Equip Thy Armor (Dependencies)

Bestow upon thy environment the consecrated metal of LangChain and its allies:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Inscribe Thy Secret Signet Ring (.env)

Duplicate the sacred template to forge thy clandestine `.env` vault:

**Windows PowerShell**

```powershell
Copy-Item .env.example .env
```

**macOS / Linux**

```bash
cp .env.example .env
```

Engrave thine authentic royal tokens into `.env`. Guard this parchment under pain of dungeon exile—never pledge it to Git or display it upon the public town square!

| Royal Signet Seal | Province of Dominion |
| :--- | :--- |
| `OPENAI_API_KEY` | Empowers `chat.py`, `embeddings.py`, `movie_data_cleaner.py`, `RAG_project`, and `vectorstores/vectorstore.py` |
| `HUGGINGFACEHUB_API_TOKEN` | Grants safe passage to the distant citadel of `chatmodels/huggingface.py` |
| `GROQ_API_KEY`, `GEMINI_API_KEY`, `MISTRAL_API_KEY` | Kept in the royal vaults for future crusades; untouched by present skirmishes |

## 🔬 Tournaments & Martial Demos

Ride forth into the courtyard and test thy mettle. Each trial is autonomous—thou mayest joust in whichever arena thy heart desireth.

### I. The Whispering Oracles (Chat Models)

```bash
python chatmodels/chat.py
```

**The Swift Courier**: Dispatcheth a single, unvarnished query unto the oracle `gpt-4o-mini` utilizing the LangChain order's `init_chat_model`. A rapid test of thy royal OpenAI alliance.

```bash
python chatmodels/chatbot.py
```

**The Tavern Automaton**: Enter into spirited dialogue with an automaton possessed of three volatile humours: caustic wit (*funny*), melancholic despair (*sad*), or raging fury (*angry*). Declare thy chosen temper upon entry; whisper `0` when thy patience hath reached its end.

```bash
python chatmodels/huggingface.py
```

**The Distant Beacon**: Lighteth the beacons to commune with remote Hugging Face fortresses across the misty hills. Demands an active seal and granted ingress.

```bash
python chatmodels/localmodel.py
```

**Summoning the Warhorse**: Bypasses all foreign kings to summon `TinyLlama-1.1B` directly into thine own castle’s keep. The first invocation bridles the beast from across the seas; thereafter, pure local iron generates prophetic speech upon thy hearth.

### II. High Celestial Runes (Embeddings)

```bash
python embeddingmodels/embeddings.py
python embeddingmodels/hf_embeddings.py
```

Transmute human verse into high-dimensional star constellations:
- `embeddings.py`: Projects queries into the celestial sphere of OpenAI’s `text-embedding-3-small`.
- `hf_embeddings.py`: Inscribes local coordinate runes employing BAAI’s famed `bge-small-en-v1.5` craft.

### III. Crusades of the Realm (Projects)

```bash
python Projects/movie_data_cleaner.py
```

**The Inquisitor of Ballads**: Feeds rambling, disorderly bardic ballads of cinema into `gpt-4o-mini`, binding the unruly tongue with the unbreakable iron collar of a Pydantic schema (title, director, year of release, star rating, and heraldic genres).

```bash
python Projects/RAG_project/main.py
```

**The Royal Scribe’s Distillation**: Unrolls dense scholarly manuscripts of deep learning, slices the lore into digestible fragments, and bids `gpt-4o-mini` forge a concise bulleted summary for the High Council.

#### Slicing of Scrolls & Lexical Guillotines

To inspect the guillotine blades that slice documents into chunks before battle:

```bash
python Projects/RAG_project/document_loaders/pdf.py
python Projects/RAG_project/document_loaders/text.py
python Projects/RAG_project/document_loaders/web_page.py
```

- `pdf.py`: Cleaves academic codices page by page using `TokenTextSplitter` (`chunk_size=100`, `chunk_overlap=10`).
- `text.py`: Slices raw UTF-8 treatises along sharp character borders via `CharacterTextSplitter`.
- `web_page.py`: Sends out royal scouts via `WebBaseLoader` to strip away the HTML ramparts and seize pure text.

### IV. The Sunken Catacombs (Vector Stores)

```bash
python Projects/vectorstores/vectorstore.py
```

A complete crusade demonstrating the sacred art of spatial indexing and top-$k$ nearest-neighbor jousting within the Chroma crypts:
1. **Unrolling the Codex**: Reads the sacred treatise on deep learning and transformers via `PyPDFLoader`.
2. **The Cleaver’s Work**: Slices the parchment into tactical squads of tokens using `RecursiveCharacterTextSplitter` (`chunk_size=1000`, `chunk_overlap=100`).
3. **Consecration & Burial**: Forges embeddings via `OpenAIEmbeddings` and buries the index deep within the subterranean Chroma catacomb (`chroma-db/`).
4. **The Celestial Joust**: Conducts cosine similarity jousts (`vectorstore.similarity_search`) to locate nearest neighbor allies.
5. **The Royal Retriever**: Bestows upon the catacomb the mantle of a royal retriever (`vectorstore.as_retriever()`), summoning relevant scrolls upon royal decree (`retriever.invoke()`).

## ⚠️ Perils of the Quest & Dragon Hazards

- **The Quest for Sovereign RAG**: Loading of scrolls, cleaving of tokens, runic embedding, and subterranean Chroma retrieval are fully mastered. The final crusade before thee is weaving the retriever directly into a generation lance, slaying hallucinations once and for all.
- **Absolute Castle Paths**: Certain loader scrolls invoke absolute Windows roadmaps. Adjust `filepath` declarations to match thine own castle’s geography before sounding the war horn.
- **The Cursed Catacomb Caches**: Engaging the vector store scripts spawns enchanted local vaults (`chroma-db/` and `rag-project-chroma-db/`), which are banished from git chronicles. Cleanse these crypts if thou changest thine embedding runes or sacred texts!
- **First-Page Royal Audiences**: Though `main.py` wieldeth the power to cleave all scrolls, its baseline incantation currently presents only the first page unto the Oracle for swift sanity verification.
- **Capricious Cloud Spirits**: Foreign endpoints and remote Hugging Face spires may alter their wards or demand tribute without forewarning. If a remote spirit rejecteth thy plea, verify thy seals.
- **Unadorned Terminal Heraldry**: Output belloweth straight unto `stdout`. There be no gilded web tapestries, no decadent graphic interfaces—only the raw clatter of steel against stone.
- **Unpinned Provisions**: The scroll of `requirements.txt` carries no rigid version shackles. Fresh crusades shall summon the latest enchantments from the LangChain guild.

## 🛡️ The Sovereign Charter

This fortress and its armory are bestowed under the holy and benevolent [MIT License](LICENSE). Take these swords, forge thine own arms, defend thy kingdom, and conquer new frontiers. *Non nobis, Domine, sed nomini Tuo da gloriam!*
