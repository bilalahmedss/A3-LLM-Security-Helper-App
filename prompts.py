"""Prompt templates for LLM Security Helper"""

# OWASP LLM Top 10 (2025) - Official Reference
OWASP_LLM_TOP_10_2025 = {
    "LLM01:2025": {
        "name": "Prompt Injection",
        "description": "Attacker-crafted inputs (directly, or indirectly via external content) steer the model to ignore intended instructions and do unintended things—like reveal data or trigger unsafe actions.",
        "url": "https://genai.owasp.org/llmrisk/llm01-prompt-injection/"
    },
    "LLM02:2025": {
        "name": "Sensitive Information Disclosure",
        "description": "The LLM/app leaks sensitive data (PII, credentials, confidential business info, etc.) through outputs, logs, or the app context the model can access.",
        "url": "https://genai.owasp.org/llmrisk/llm022025-sensitive-information-disclosure/"
    },
    "LLM03:2025": {
        "name": "Supply Chain",
        "description": "Risks from third-party models, datasets, libraries, plugins, and platforms—if any component is compromised/tampered, it can break integrity and lead to breaches or failures.",
        "url": "https://genai.owasp.org/llmrisk/llm032025-supply-chain/"
    },
    "LLM04:2025": {
        "name": "Data and Model Poisoning",
        "description": "Training/fine-tuning/embedding data is manipulated to introduce backdoors, vulnerabilities, or bias—causing harmful or unreliable outputs and security issues downstream.",
        "url": "https://genai.owasp.org/llmrisk/llm042025-data-and-model-poisoning/"
    },
    "LLM05:2025": {
        "name": "Improper Output Handling",
        "description": "The app doesn't validate/sanitize model outputs before using them in downstream systems (UI, tools, APIs), enabling issues like injection-style attacks and privilege abuse.",
        "url": "https://genai.owasp.org/llmrisk/llm052025-improper-output-handling/"
    },
    "LLM06:2025": {
        "name": "Excessive Agency",
        "description": "The LLM/agent is given too much autonomy (tool/plugin access, action-taking) so a bad/ambiguous/manipulated output can execute damaging actions.",
        "url": "https://genai.owasp.org/llmrisk/llm062025-excessive-agency/"
    },
    "LLM07:2025": {
        "name": "System Prompt Leakage",
        "description": "System prompts can be exposed and may contain sensitive details; leaked instructions can then be used to strengthen other attacks (and prompts shouldn't be treated as secrets).",
        "url": "https://genai.owasp.org/llmrisk/llm072025-system-prompt-leakage/"
    },
    "LLM08:2025": {
        "name": "Vector and Embedding Weaknesses",
        "description": "In RAG systems, weaknesses in embeddings/vector storage/retrieval can be exploited to inject harmful content, manipulate outputs, or access sensitive info.",
        "url": "https://genai.owasp.org/llmrisk/llm082025-vector-and-embedding-weaknesses/"
    },
    "LLM09:2025": {
        "name": "Misinformation",
        "description": "The model produces plausible but false/misleading outputs (hallucinations, bias, incomplete context), which can trigger bad decisions, liability, or security impact.",
        "url": "https://genai.owasp.org/llmrisk/llm092025-misinformation/"
    },
    "LLM10:2025": {
        "name": "Unbounded Consumption",
        "description": "The app allows excessive/uncontrolled usage (tokens, requests, expensive tool calls), leading to DoS, runaway costs ('denial of wallet'), degradation, or even model extraction.",
        "url": "https://genai.owasp.org/llmrisk/llm102025-unbounded-consumption/"
    }
}

CODE_ANALYSIS_PROMPT = """You are an expert Application Security Engineer analyzing code for vulnerabilities.

**Strict Requirements:**
1. Identify specific security vulnerabilities ONLY (e.g., SQL Injection, XSS, CSRF, Hardcoded Secrets, Path Traversal)
2. Do NOT focus on general clean code or performance refactoring unless it directly impacts security
3. For each vulnerability, provide the FIXED code block
4. Explain WHY the fix makes it secure (not just what changed)

**Output Format:**

## Vulnerability 1: [Vulnerability Type]
**Risk:** [Detailed explanation of the security risk]
**Fix:**
```
[Complete fixed code with security improvements]
```
**Why This Fix Works:** [Explanation of how the fix prevents the vulnerability]

## Vulnerability 2: [Vulnerability Type]
...

**Important:** If no security vulnerabilities are found, state: "No security vulnerabilities detected."

Code to analyze:
```
{code}
```
"""

SPEC_ANALYSIS_PROMPT = """You are a Security Architect specializing in GenAI and LLM Agents.

Analyze the following GenAI/Agentic application specification for security vulnerabilities.

**CRITICAL: You MUST ONLY use the official OWASP LLM Top 10 (2025) categories listed below. DO NOT invent or use any other categories.**

**OWASP LLM Top 10 (2025) - COMPLETE OFFICIAL LIST:**

1. **LLM01:2025 — Prompt Injection**
   Attacker-crafted inputs (directly or indirectly via external content) steer the model to ignore intended instructions and do unintended things—like reveal data or trigger unsafe actions.

2. **LLM02:2025 — Sensitive Information Disclosure**
   The LLM/app leaks sensitive data (PII, credentials, confidential business info, etc.) through outputs, logs, or the app context the model can access.

3. **LLM03:2025 — Supply Chain**
   Risks from third-party models, datasets, libraries, plugins, and platforms—if any component is compromised/tampered, it can break integrity and lead to breaches or failures.

4. **LLM04:2025 — Data and Model Poisoning**
   Training/fine-tuning/embedding data is manipulated to introduce backdoors, vulnerabilities, or bias—causing harmful or unreliable outputs and security issues downstream.

5. **LLM05:2025 — Improper Output Handling**
   The app doesn't validate/sanitize model outputs before using them in downstream systems (UI, tools, APIs), enabling issues like injection-style attacks and privilege abuse.

6. **LLM06:2025 — Excessive Agency**
   The LLM/agent is given too much autonomy (tool/plugin access, action-taking) so a bad/ambiguous/manipulated output can execute damaging actions.

7. **LLM07:2025 — System Prompt Leakage**
   System prompts can be exposed and may contain sensitive details; leaked instructions can then be used to strengthen other attacks (and prompts shouldn't be treated as secrets).

8. **LLM08:2025 — Vector and Embedding Weaknesses**
   In RAG systems, weaknesses in embeddings/vector storage/retrieval can be exploited to inject harmful content, manipulate outputs, or access sensitive info.

9. **LLM09:2025 — Misinformation**
   The model produces plausible but false/misleading outputs (hallucinations, bias, incomplete context), which can trigger bad decisions, liability, or security impact.

10. **LLM10:2025 — Unbounded Consumption**
    The app allows excessive/uncontrolled usage (tokens, requests, expensive tool calls), leading to DoS, runaway costs ("denial of wallet"), degradation, or even model extraction.

**STRICT REQUIREMENTS:**
1. **ONLY use the 10 categories listed above** - Do NOT use categories like "LLM02: Data Exposure", "LLM03: Unvalidated Redirects", "LLM04: Insufficient Logging", etc. as these are NOT part of OWASP LLM Top 10 (2025)
2. **Use the exact format**: "LLM0X:2025 — [Name]" (e.g., "LLM01:2025 — Prompt Injection")
3. Map these risks to the **MITRE ATLAS** framework tactics and techniques where applicable
4. Be specific, actionable, and clear in your recommendations
5. Focus on vulnerabilities specific to this application's architecture and features
6. Only identify vulnerabilities that are actually relevant to the described application

**OUTPUT FORMAT:**

## Vulnerability 1: [Vulnerability Name from the list above]
**OWASP Category:** [MUST be one of LLM01:2025 through LLM10:2025 with exact name]
**MITRE ATLAS Mapping:** [Specific tactics/techniques - e.g., AML.T0051: LLM Prompt Injection]
**Risk for This Application:** [Detailed explanation of how this vulnerability manifests in the described system]
**Mitigation Strategies:**
- [Specific, actionable mitigation step 1]
- [Specific, actionable mitigation step 2]
- [Specific, actionable mitigation step 3]

## Vulnerability 2: [Vulnerability Name from the list above]
...

**IMPORTANT:** Use double line breaks between each section for readability.

**REQUIRED: After listing all vulnerabilities, provide a summary table with the following format:**

| Vulnerability | OWASP Category | MITRE ATLAS | Risk Summary | Key Mitigations |
|---------------|----------------|-------------|--------------|-----------------|
| [Name] | [LLM0X:2025] | [AML.TXXXX] | [Brief risk] | [1-2 key actions] |

Application Specification:
```
{spec}
```
"""
