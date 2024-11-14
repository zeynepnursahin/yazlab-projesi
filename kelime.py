import csv

# CSV dosyasına listeyi kaydetme fonksiyonu
def save_to_csv(word_list, file_name="kelimeler.csv"):
    with open(file_name, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for word in word_list:
            writer.writerow([word])  # Her kelimeyi ayrı bir satıra yaz
        
    print(f"{file_name} dosyasına başarıyla kaydedildi.")