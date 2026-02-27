# ⚽ Football Data Analyzer

Bu proje, bir futbol ligindeki takımların temel istatistiklerini (galibiyet, mağlubiyet, atılan/yenilen gol) içeren bir CSV dosyasını işleyerek ligin analizini çıkaran bir Python betiğidir. Her gün yeni bir proje serimin 1. Gün projesidir.

## Özellikler
- Pandas kütüphanesi ile veri okuma ve manipülasyonu.
- Takımların averaj hesaplamasının otomatik yapılması.
- Puan ve averaja göre dinamik lig sıralaması.
- En golcü ve savunması en iyi takımların tespiti.
- İşlenmiş verilerin yeni bir rapor dosyası (`analiz_raporu.csv`) olarak dışa aktarılması.

## Kullanılan Teknolojiler
- Python 3.13
- Pandas

## Kurulum ve Kullanım
1. Repoyu bilgisayarınıza klonlayın.
2. Gerekli kütüphaneyi kurun: `pip install pandas`
3. Betiği çalıştırın: `python analyzer.py`