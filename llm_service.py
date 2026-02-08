"""LLM Service for Groq API integration"""
import streamlit as st  
import os
from groq import Groq
from dotenv import load_dotenv
from prompts import CODE_ANALYSIS_PROMPT, SPEC_ANALYSIS_PROMPT

# Load environment variables
load_dotenv()

class LLMService:
    """Service for interacting with Groq API"""
    
    def __init__(self):
        """Initialize Groq client"""
        api_key = st.secrets.get("GROQ_API_KEY") or os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("GROQ_API_KEY not found in environment variables")
        
        self.client = Groq(api_key=api_key)
        self.model = "llama-3.1-8b-instant"  # Fast and efficient for security analysis
    
    def analyze_code(self, code: str) -> str:
        """
        Analyze code for security vulnerabilities
        
        Args:
            code: Code snippet to analyze
            
        Returns:
            Analysis results with vulnerabilities and fixes
        """
        prompt = CODE_ANALYSIS_PROMPT.format(code=code)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are an expert Application Security Engineer focused on identifying code vulnerabilities."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3  # Lower temperature for more focused analysis
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"Error analyzing code: {str(e)}"
    
    def analyze_spec(self, spec: str) -> str:
        """
        Analyze GenAI specification for vulnerabilities using OWASP and ATLAS
        
        Args:
            spec: Application specification to analyze
            
        Returns:
            Analysis results mapped to OWASP Top 10 for LLM and ATLAS
        """
        prompt = SPEC_ANALYSIS_PROMPT.format(spec=spec)
        
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": "You are a Security Architect specializing in GenAI and LLM Agents, with expertise in OWASP LLM Top 10 and MITRE ATLAS framework."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3  # Lower temperature for more focused analysis
            )
            
            return response.choices[0].message.content
        
        except Exception as e:
            return f"Error analyzing specification: {str(e)}"
