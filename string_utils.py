import re

def slugify(text):
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    return re.sub(r'[-\s]+', '-', text)

def truncate(text, length=100, suffix='...'):
    if len(text) <= length:
        return text
    return text[:length].rsplit(' ', 1)[0] + suffix

def extract_emails(text):
    return re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', text)

def extract_urls(text):
    return re.findall(r'https?://[^\s<>"{}|\\^`\[\]]+', text)

def word_count(text):
    return len(text.split())
