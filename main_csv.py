import csv
from bs4 import BeautifulSoup
import requests
import random
import time
import threading

user_agents = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
]


lock = threading.Lock()


def process_url(url, all_links):
    try:

        headers = {'User-Agent': random.choice(user_agents)}
        

        response = requests.get(url, headers=headers)
        response.raise_for_status()


        soup = BeautifulSoup(response.text, 'html.parser')
        

        product_links = soup.select('.cl-product-images')
        links = [link['href'] for link in product_links]


        if links:
            with lock:
                all_links.extend(links)

            return len(links)
        else:
            return 0

    except Exception as e:
        print("Hata:", e)
        return 0


def process_product_info(link, writer):
    try:

        headers = {'User-Agent': random.choice(user_agents)}
        

        response = requests.get(link, headers=headers)
        response.raise_for_status()


        soup = BeautifulSoup(response.text, 'html.parser')


        title = soup.title.string
        print("Ürün Bilgileri Çekiliyor : ", title)

        product_name = soup.select_one(".cl-product-title").contents[0].strip()
        product_code = soup.select_one(".cl-product-title span").text.strip()
        product_price = soup.select_one(".cl-product-price span").text.strip()
        

        product_images = soup.select('[data-fancybox="cl-product-gallery"]')
        image_links = [image['href'] for image in product_images]


        writer.writerow([title, product_name, product_code, product_price] + image_links + [link])

    except Exception as e:
        print("Hata:", e)


urun_kategori_listesi = [
    'https://www.skechers.com.tr/kadin-c-1'
    'https://www.skechers.com.tr/erkek-c-2',
    'https://www.skechers.com.tr/cocuk-c-3',
    'https://www.skechers.com.tr/koleksiyonlar-c-4',
    'https://www.skechers.com.tr/spor-giyim-c-6100',
    'https://www.skechers.com.tr/kullanim-alanina-gore-c-8070',
    'https://www.skechers.com.tr/sezon-indirimi-c-7001'
]

start_page = int(input("Başlangıç sayfasını girin: "))
end_page = int(input("Bitiş sayfasını girin: "))
pages_to_fetch = int(input("Kaç sayfa ilerlemek istiyorsunuz: "))


with open('urun_bilgileri.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Sayfa Başlığı', 'Ürün Adı', 'Ürün Kodu', 'Ürün Fiyatı', 'Resim 1', 'Resim 2', 'Resim 3', 'Resim 4', 'Resim 5', 'Resim 6', 'Resim 7', 'Resim 8', 'Resim 9', 'Resim 10', 'Ürün Linki'])
    

    try:
        print("Program Başlatıldı ...")
        for urun_kategori in urun_kategori_listesi:
            for page_number in range(start_page, start_page + pages_to_fetch):

                url = f'{urun_kategori}?pagenumber={page_number}'

                all_links = []
                product_count = process_url(url, all_links)
                print(f'Ürün Linkleri Çekiliyor | Kategori = {urun_kategori} | Sayfa = {page_number} | Ürün Sayısı = {product_count}')
                

                time.sleep(0.1)


                for link in all_links:
                    process_product_info("https://www.skechers.com.tr"+link, writer)

    except KeyboardInterrupt:
        print("İşlem kullanıcı tarafından iptal edildi.")
