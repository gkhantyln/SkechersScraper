# Skechers Product Scraper
Bu Python betiği, Skechers web sitesindeki ürün bilgilerini çekerek, bu bilgileri bir Excel dosyasına kaydetmek için kullanılır. Betik, çoklu sayfa ve kategori desteği sağlar ve rastgele kullanıcı ajanları kullanarak HTTP istekleri yapar.

## İçindekiler
- [Özellikler](#özellikler)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

## Özellikler
- Belirli bir web sitesindeki ürün bilgilerini çekme.
- Çoklu sayfa ve kategori desteği.
- Rastgele kullanıcı ajanları kullanarak HTTP istekleri yapma.
- Ürün bilgilerini (başlık, ad, kod, fiyat, resim linkleri) Excel dosyasına kaydetme.
- İşlemi kullanıcı tarafından iptal etme desteği.


## Gereksinimler
Bu betiği çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:
- `requests`
- `beautifulsoup4`
- `xlsxwriter`


Kurulum:
```bash
pip install requests beautifulsoup4 xlsxwriter
```

## Kurulum
Bu depozitoryayı klonlayın:
```bash
git clone https://github.com/gkhantyln/SkechersScraper.git
cd SkechersScraper
```

## Kullanım
1 - Python betiğini çalıştırın:
```bash
python requestsBS4.py
python requestsBS4_csv.py
```
2 - Başlangıç ve Bitiş Sayfalarıı Girin:
```bash
Başlangıç sayfasını girin: 1
Bitiş sayfasını girin: 5
Kaç sayfa ilerlemek istiyorsunuz: 10
```
3 - İşlemi başlatın ve betiğin ürün bilgilerini çekmesini bekleyin.
Örnek Çıktı:
Betik çalıştığında, aşağıdaki gibi bir çıktı alabilirsiniz:
```bash
Program Başlatıldı ...
Ürün Linkleri Çekiliyor | Kategori = https://www.siteadi.com.tr/kadin-c-1 | Sayfa = 1 | Ürün Sayısı = 20
Ürün Bilgileri Çekiliyor :  Ürün Başlığı
...
```

## Katkıda Bulunma
Katkılarınızı memnuniyetle karşılıyoruz! Lütfen bir pull request gönderin veya bir issue açın.

## Lisans
Bu proje MIT Lisansı ile lisanslanmıştır - daha fazla bilgi için `LICENSE` dosyasına bakın.

