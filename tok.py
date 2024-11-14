import zeyrek
import re

# Zeyrek kök bulucu başlat
analyzer = zeyrek.MorphAnalyzer()

# Temizlenmiş içeriği kelimelere ayırma ve köklerine indirgeme fonksiyonu
def process_and_stem_text(text):
    # Kelimeleri ayırarak bir liste oluşturma
    words = re.findall(r'\b\w+\b', text.lower())  # Tüm kelimeleri küçük harfe çevir ve listele
    stemmed_words = set()  # Set yapısı, tekrar eden köklerin eklenmesini engeller
    
    # Her kelimenin kökünü bulma
    for word in words:
        analysis = analyzer.analyze(word)
        if analysis:
            root = analysis[0][0].lemma  # İlk analizin kökünü al
            stemmed_words.add(root)
        else:
            stemmed_words.add(word)  # Kök bulunamazsa orijinal hali ekle
    
    return list(stemmed_words)
