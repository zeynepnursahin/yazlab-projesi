import mysql.connector

# MySQL veritabanına bağlanın
def insert_words_from_tokenize(tokenize_list):
    # Veritabanı bağlantısı kurma
    db_connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="zey345,,A",
        database="saglik"
    )

    cursor = db_connection.cursor()

    # Tabloyu oluştur
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS kelimeler (
        id INT AUTO_INCREMENT PRIMARY KEY,
        kelime VARCHAR(255) UNIQUE
    )
    """)

    for kelime in tokenize_list:
        try:
            # Kelimeyi veritabanına ekle (tekrarları engellemek için UNIQUE kullanıldı)
            cursor.execute("INSERT IGNORE INTO kelimeler (kelime) VALUES (%s)", (kelime,))
        except mysql.connector.Error as err:
            print(f"Hata: {err}")

    # Veritabanı işlemlerini kaydet (commit)
    db_connection.commit()
    print(f"{len(tokenize_list)} kelime veritabanına kaydedildi.")

    # Bağlantıyı kapat
    cursor.close()
    db_connection.close()


