from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer
import nltk
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True)

def summarize_regulatory_text(text, sentences=2):
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    summarizer = LsaSummarizer()
    summary = summarizer(parser.document, sentences_count=sentences)
    return " ".join(str(sentence) for sentence in summary)

if __name__ == "__main__":
    sample_text = """
    The Central Bank has issued new guidelines requiring all financial 
    institutions to implement enhanced due diligence procedures for 
    high-risk customers. Institutions must maintain detailed records 
    of all transactions exceeding $10,000 and report suspicious 
    activities within 24 hours of detection. Non-compliance will 
    result in penalties ranging from fines to license revocation. 
    All institutions must complete implementation by Q4 2025.
    """
    print("SUMMARY:")
    print(summarize_regulatory_text(sample_text))

