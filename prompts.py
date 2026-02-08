"""Prompt templates for LLM Security Helper"""

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

**Strict Requirements:**
1. Identify potential vulnerabilities based on the **OWASP Top 10 for LLM Applications (2023)**
2. Map these risks to the **MITRE ATLAS** (Adversarial Threat Landscape for Artificial-Intelligence Systems) framework tactics and techniques where applicable
3. Be specific, actionable, and clear in your recommendations
4. Focus on vulnerabilities specific to this application's architecture and features

**Output Format:**

## Vulnerability 1: [Vulnerability Name]
**OWASP Category:** [e.g., LLM01: Prompt Injection]
**MITRE ATLAS Mapping:** [Specific tactics/techniques - e.g., AML.T0051: LLM Prompt Injection]
**Risk for This Application:** [Detailed explanation of how this vulnerability manifests in the described system]
**Mitigation Strategies:**
- [Specific, actionable mitigation step 1]
- [Specific, actionable mitigation step 2]
- [Specific, actionable mitigation step 3]

## Vulnerability 2: [Vulnerability Name]
...

**IMPORTANT:** Use double line breaks between each section for readability.

**Note:** Provide a comprehensive analysis covering multiple OWASP LLM categories. Use table format if it improves clarity for mapping multiple vulnerabilities.

Application Specification:
```
{spec}
```
"""
