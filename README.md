# A3 - LLM Security Helper

AI-powered security analysis tool for code vulnerabilities and GenAI application specifications using OWASP LLM Top 10 and MITRE ATLAS frameworks.

---

## 🎯 Features

### Part 1: Code Security Vulnerability Analysis ⚡

- Identifies **security-specific vulnerabilities** (SQL Injection, XSS, CSRF, Hardcoded Secrets, Path Traversal)
- Provides **fixed code** with security improvements
- Explains **why the fix works** (not just what changed)
- Focuses on security, not general code quality

### Part 2: GenAI Specification Security Assessment ⚡

- Maps vulnerabilities to **OWASP Top 10 for LLM Applications (2023)**
- Provides **MITRE ATLAS** threat actor perspective
- Delivers **actionable mitigation strategies** (3 per vulnerability)
- Analyzes architecture, data flow, and user interactions

---

## 📋 Prerequisites

- Python 3.8 or higher
- Groq API Key ([Get one for free](https://console.groq.com))
- pip

---

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
# Navigate to project directory
cd "A3-LLM Security Helper App"

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Key

Create a `.env` file in the project root:

```bash
GROQ_API_KEY=your_groq_api_key_here
```


### 3. Run the Application

```bash
streamlit run app.py
```

Then open your browser to: `http://localhost:8501`

---

## 💻 Usage Examples

### Part 1: Code Security Analysis

1. Navigate to the **"Part 1: Code Security Analysis"** tab
2. Paste your code snippet (any language)
3. Click **"🔍 Analyze Code"**
4. Review:
   - Identified vulnerabilities
   - Fixed code blocks
   - Security explanations



### Part 2: GenAI Specification Analysis

1. Navigate to the **"Part 2: GenAI Spec Analysis"** tab
2. Describe your GenAI application:
   - Architecture (frontend, backend, LLM integration)
   - Features (user interactions, data access)
   - Data flow (how data moves through the system)
3. Click **"🔍 Analyze Spec"**
4. Review:
   - OWASP LLM Top 10 mappings
   - ATLAS threat perspectives
   - Risk assessments
   - Mitigation strategies



## 📁 Project Structure

```
A3-LLM Security Helper App/
├── app.py              # Main Streamlit application
├── llm_service.py      # Groq API integration & caching
├── prompts.py          # Enhanced prompt templates
├── requirements.txt    # Python dependencies
├── .env                # API key (not committed)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

---

## 🔧 Technical Details

### LLM Configuration

| Component | Technology | Details |
|-----------|-----------|---------|
| **LLM Provider** | Groq | Fast inference API |
| **Model** | Llama 3.1 8B Instant | Optimized for speed |
| **Max Tokens** | Unlimited | Complete responses |
| **Temperature** | 0.3 | Balanced creativity |
| **Caching** | Yes | Client cached with `@st.cache_resource` |

### Security Analysis Frameworks

| Framework | Version | Purpose |
|-----------|---------|---------|
| **OWASP LLM Top 10** | 2023 | LLM-specific vulnerabilities |
| **MITRE ATLAS** | Latest | Adversarial ML threat landscape |

### Architecture

- **Frontend**: Streamlit (Python-based web framework)
- **Backend**: Groq API via `groq` Python SDK
- **Prompt Engineering**:
  - Strict requirements framing
  - Structured output format
  - Security-focused instructions
  - ATLAS perspective integration
- **Environment**: `.env` for secure API key management


---





## 👨‍💻 Author

**Bilal Ahmed** (08018)  
Assignment 3 - Generative AI Course
