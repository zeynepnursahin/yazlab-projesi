import time
import random
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
from tarama import clean_and_process_text
from tok import process_and_stem_text
from kelime import save_to_csv
from database import insert_words_from_tokenize

chrome_driver_path = "./chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3")
# options.add_argument("--headless")
# options.add_argument("--disable-gpu")

# WebDriver başlatma
driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)

try:
    # Google'ı açma
    driver.get("https://www.google.com")

    # Arama kutusuna query (konu) yazma
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "q"))
    )
    search_query = "egzama hastalığı"
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    # Arama sonuçlarını bekleme
    search_results = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.XPATH, '//h3/ancestor::a'))
    )

    # Eğer sonuç varsa rastgele bir site seç ve tıkla
    if search_results:
        random_site = random.choice(search_results)
        random_site.click()

        # HTML kaynağını al
        html = driver.page_source
        cleaned_content=clean_and_process_text(html)
        tokenize=process_and_stem_text(cleaned_content)
        insert_words_from_tokenize(tokenize)
        current_url = driver.current_url
    else:
        print("Arama sonucu bulunamadı.")
except Exception as e:
    print(f"Hata oluştu: {e}")
finally:
    driver.quit()