from bs4 import BeautifulSoup
import zeyrek
from nltk.tokenize import word_tokenize
import nltk
from nltk.corpus import stopwords
import ssl

# Gerekli veri kümelerini indir
nltk.download('punkt_tab')
nltk.download('stopwords')

# Türkçe stopword'leri set olarak al
try:
    stop_words = set(stopwords.words("turkish"))
except Exception as e:
    print("Stopword yüklemede hata oluştu:", e)

# Zeyrek Morfolojik Analizleyici
analyzer = zeyrek.MorphAnalyzer()

def clean_and_process_text(html_content):
    # HTML'den temizleme işlemi
    soup = BeautifulSoup(html_content, "html.parser")
    for script in soup(["script", "style"]):
        script.extract()

    cleaned_content = soup.get_text(separator="\n")
    cleaned_content = "\n".join(line.strip() for line in cleaned_content.splitlines() if line.strip())

    # Tokenizasyon ve stopwords temizleme
    words = word_tokenize(cleaned_content)
    filtered_words = [word for word in words if word.lower() not in stop_words]

    # Zeyrek ile kök bulma işlemi
    processed_words = []
    for word in filtered_words:
        analysis = analyzer.analyze(word)
        if analysis:
            lemma = analysis[0][0].lemma
            processed_words.append(lemma)
        else:
            processed_words.append(word)  # Köken bulunamazsa orijinal kelimeyi kullanıyoruz

    # İşlenmiş kelimeleri birleştirip bütünlüğü koruyoruz
    processed_content = " ".join(processed_words)

    return processed_content