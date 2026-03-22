# RegDoc-Summarizer 📄

A Python-based NLP tool that automatically summarizes regulatory and compliance documents into clear, concise plain English.

---

## The Problem

Compliance teams and financial institutions deal with dense, lengthy regulatory documents daily — policy circulars, compliance guidelines, central bank directives. Reading and extracting key information from these manually is time-consuming and prone to human error.

## The Solution

RegDoc-Summarizer uses Natural Language Processing (NLP) to automatically identify and extract the most important sentences from any regulatory document, reducing pages of dense text into actionable summaries in seconds.

---

## Demo

**Input:**
```
The Central Bank has issued new guidelines requiring all financial institutions 
to implement enhanced due diligence procedures for high-risk customers. 
Institutions must maintain detailed records of all transactions exceeding $10,000 
and report suspicious activities within 24 hours of detection. Non-compliance will 
result in penalties ranging from fines to license revocation. All institutions must 
complete implementation by Q4 2025.
```

**Output:**
```
The Central Bank has issued new guidelines requiring all financial institutions 
to implement enhanced due diligence procedures for high-risk customers. 
Non-compliance will result in penalties ranging from fines to license revocation.
```

---

## Features

- Summarizes regulatory documents into 2-5 key sentences
- Works on any plain text compliance or policy document
- Lightweight — no heavy model downloads required
- Fast — runs locally with no internet dependency
- Easily extendable to process PDF documents

---

## Tech Stack

- **Python 3.12**
- **Sumy** — NLP summarization library
- **NLTK** — Natural language toolkit
- **LSA (Latent Semantic Analysis)** — Summarization algorithm

---

## Installation

```bash
# Clone the repository
git clone https://github.com/PraiseAgboola/RegDoc-Summarizer.git
cd RegDoc-Summarizer

# Install dependencies
pip install sumy nltk
```

---

## Usage

```python
from summarizer import summarize_regulatory_text

text = """
Your regulatory document text goes here.
"""

summary = summarize_regulatory_text(text, sentences=2)
print(summary)
```

Or run directly:

```bash
python summarizer.py
```

---

## Use Cases

- **RegTech companies** — Automate compliance document review
- **Financial institutions** — Quickly digest central bank circulars
- **Legal teams** — Extract key obligations from regulatory filings
- **Fintech startups** — Monitor and summarize MAS, CBN, SEC guidelines

---

## Roadmap

- [ ] Add PDF file input support
- [ ] Build a simple web interface
- [ ] Integrate transformer-based models (BART, T5) for more intelligent summaries
- [ ] Support for multiple regulatory jurisdictions (MAS, CBN, SEC, FCA)
- [ ] Batch processing for multiple documents

---

## Author

**Praise Agboola**  
Final year undergraduate | Aspiring ML Engineer & Strategist  
Interested in the intersection of NLP, RegTech, and financial infrastructure  

[GitHub](https://github.com/PraiseAgboola) • [LinkedIn](https://www.linkedin.com/in/praise-agboola-393921248/)

---

## License

MIT License — feel free to use, modify, and build on this project.