import re
from collections import Counter


def extract_keywords(text, top_n=15):
    try:
        if not text.strip():
            return []

        stopwords = {
            "the", "is", "in", "and", "to", "of", "a", "an", "for", "on", "with",
            "that", "this", "it", "as", "at", "by", "from", "or", "be", "are",
            "was", "were", "has", "have", "had", "will", "would", "can", "could",
            "should", "may", "might", "into", "about", "than", "then", "them",
            "their", "there", "which", "what", "when", "where", "who", "whom",
            "how", "why", "not", "but", "if", "also", "such", "these", "those"
        }

        words = re.findall(r"\b[a-zA-Z]{3,}\b", text.lower())
        filtered_words = [w for w in words if w not in stopwords]

        freq = Counter(filtered_words)
        return [word for word, _ in freq.most_common(top_n)]

    except Exception as e:
        return [f"Keyword Error: {str(e)}"]