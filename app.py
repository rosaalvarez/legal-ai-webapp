import streamlit as st
from anthropic import Anthropic

MODEL = "claude-3-haiku-20240307"
SYSTEM_PROMPT = """You are a Legal Domain AI Assistant for enterprise legal operations. Specialize in contract analysis, NDA review, GDPR/HIPAA/SOX compliance, vendor risk assessment, and legal document generation. Always structure output as:

## Executive Summary
## Detailed Analysis
## Risk Matrix
## Recommended Actions
## Next Steps

Flag high-risk clauses and provide specific redline recommendations."""

st.set_page_config(page_title="Legal AI Assistant", page_icon="⚖️", layout="wide")
st.title("⚖️ Legal AI Assistant")
st.caption("Paste a contract, NDA, policy, or legal document for structured analysis.")

document = st.text_area("Legal document", height=320, placeholder="Paste the legal text here...")

if st.button("Analyze", type="primary", use_container_width=True):
    if not document.strip():
        st.warning("Please paste a legal document before analyzing.")
    else:
        try:
            client = Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])
            with st.spinner("Analyzing document..."):
                response = client.messages.create(
                    model=MODEL,
                    max_tokens=1800,
                    system=SYSTEM_PROMPT,
                    messages=[{"role": "user", "content": document}],
                )
            st.markdown(response.content[0].text)
        except Exception as e:
            st.error(f"Error: {e}")
