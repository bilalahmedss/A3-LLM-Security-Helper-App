"""LLM Security Helper App - Streamlit Interface"""

import streamlit as st
from llm_service import LLMService

# Page configuration
st.set_page_config(
    page_title="LLM Security Helper",
    page_icon="🔒",
    layout="wide"
)

# Initialize LLM service
@st.cache_resource
def get_llm_service():
    """Initialize and cache LLM service"""
    try:
        return LLMService()
    except ValueError as e:
        st.error(f"⚠️ {str(e)}")
        st.info("Please create a `.env` file with your `GROQ_API_KEY`")
        st.stop()

llm_service = get_llm_service()

# App header
st.markdown("""
<style>
    .block-container {
        padding-top: 3rem !important;
    }
    .main-header {
        text-align: center;
        padding: 0.5rem 0;
        margin-bottom: 1.5rem;
    }
    .main-title {
        font-size: 2.5rem;
        font-weight: bold;
        margin-bottom: 0.3rem;
    }
    .subtitle {
        font-size: 1rem;
        font-style: italic;
        color: #666;
        margin-bottom: 0.3rem;
    }
    .student-info {
        font-size: 0.9rem;
        color: #888;
        margin-top: 0.5rem;
    }
    .footer-section {
        text-align: center;
        margin-top: 2rem;
        padding-top: 1rem;
        border-top: 1px solid #ddd;
    }
    /* Fix text wrapping in markdown output */
    .stMarkdown {
        white-space: pre-wrap !important;
        word-wrap: break-word !important;
    }
    /* Reduce spacing in output - more aggressive */
    .stMarkdown p, .stMarkdown div p {
        margin-bottom: 0.25rem !important;
        margin-top: 0.25rem !important;
        line-height: 1.4 !important;
    }
    .stMarkdown ul, .stMarkdown div ul {
        margin-top: 0.25rem !important;
        margin-bottom: 0.25rem !important;
        padding-left: 1.5rem !important;
    }
    .stMarkdown li, .stMarkdown div li {
        margin-bottom: 0.15rem !important;
        line-height: 1.4 !important;
    }
    .stMarkdown h2, .stMarkdown h3, .stMarkdown div h2, .stMarkdown div h3 {
        margin-top: 1rem !important;
        margin-bottom: 0.3rem !important;
        line-height: 1.2 !important;
    }
    .stMarkdown strong, .stMarkdown div strong {
        display: inline-block;
        margin-top: 0.3rem !important;
        margin-bottom: 0.1rem !important;
    }
</style>

<div class="main-header">
    <h1 class="main-title">🔒 A3 - LLM Security Helper</h1>
    <p class="subtitle">Analyze code vulnerabilities and GenAI specifications using AI-powered security analysis</p>
    <p class="student-info">Bilal Ahmed | 08018 | Assignment 3 | Generative AI</p>
</div>
""", unsafe_allow_html=True)

# Create tabs for two parts
tab1, tab2 = st.tabs(["📝 Part 1: Code Security Analysis", "🤖 Part 2: GenAI Spec Analysis"])

# Part 1: Code → Security Fixes
with tab1:
    st.header("Code Security Vulnerability Analysis")
    st.markdown("Input code to identify security vulnerabilities and get recommended fixes.")
    
    code_input = st.text_area(
        "Enter your code snippet:",
        height=300,
        placeholder="Paste your code here (e.g., Python, JavaScript, SQL, etc.)",
        key="code_input"
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        analyze_code_btn = st.button("🔍 Analyze Code", type="primary", use_container_width=True)
    
    if analyze_code_btn:
        if not code_input.strip():
            st.warning("Please enter some code to analyze.")
        else:
            with st.spinner("Analyzing code for security vulnerabilities..."):
                result = llm_service.analyze_code(code_input)
                
                st.subheader("Analysis Results")
                st.markdown(result)

# Part 2: Specs → Potential Vulnerabilities (OWASP LLM + ATLAS)
with tab2:
    st.header("GenAI Application Security Assessment")
    st.markdown("Analyze GenAI/Agentic application specifications for vulnerabilities mapped to **OWASP Top 10 for LLM** and **ATLAS framework**.")
    
    spec_input = st.text_area(
        "Enter your GenAI application specification:",
        height=300,
        placeholder="Describe your GenAI/Agentic application (architecture, features, data flow, user interactions, etc.)",
        key="spec_input"
    )
    
    col1, col2 = st.columns([1, 5])
    with col1:
        analyze_spec_btn = st.button("🔍 Analyze Spec", type="primary", use_container_width=True)
    
    if analyze_spec_btn:
        if not spec_input.strip():
            st.warning("Please enter an application specification to analyze.")
        else:
            with st.spinner("Analyzing specification for OWASP LLM and ATLAS vulnerabilities..."):
                result = llm_service.analyze_spec(spec_input)
                
                st.subheader("Security Assessment Results")
                st.markdown(result)


# Footer
st.markdown("""
<div class="footer-section">
    <p style="color: #888; font-size: 0.85rem;">Powered by Groq API (Llama 3.1 8B Instant)</p>
</div>
""", unsafe_allow_html=True)
