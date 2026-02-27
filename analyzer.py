import pandas as pd


def analiz_yap(dosya_yolu):
    print("Futbol Veri Analiz Aracı Başlatılıyor...\n")

    # 1. Veriyi Oku
    try:
        df = pd.read_csv(dosya_yolu)
    except FileNotFoundError:
        print(f"Hata: {dosya_yolu} bulunamadı!")
        return

    # 2. Yeni Veri Üret (Averaj Hesaplama)
    df['Averaj'] = df['Atilan_Gol'] - df['Yenilen_Gol']

    # 3. Puan Durumuna Göre Sırala
    df_sirali = df.sort_values(by=['Puan', 'Averaj'], ascending=[False, False])

    print("🏆 Güncel Puan Durumu (İlk 3):")
    print(df_sirali[['Takim', 'Puan', 'Averaj']].head(3).to_string(index=False))
    print("-" * 30)

    # 4. En Golcü Takımı Bul
    en_golcu = df.loc[df['Atilan_Gol'].idxmax()]
    print(f"⚽ En Golcü Takım: {en_golcu['Takim']} ({en_golcu['Atilan_Gol']} Gol)")

    # 5. Savunması En İyi Takım (En az gol yiyen)
    en_iyi_savunma = df.loc[df['Yenilen_Gol'].idxmin()]
    print(f"🛡️ En İyi Savunma: {en_iyi_savunma['Takim']} ({en_iyi_savunma['Yenilen_Gol']} Gol Yedi)")
    print("-" * 30)

    # 6. Analiz Sonucunu Dışa Aktar
    cikis_dosyasi = 'analiz_raporu.csv'
    df_sirali.to_csv(cikis_dosyasi, index=False)
    print(f"✅ Detaylı analiz raporu '{cikis_dosyasi}' olarak kaydedildi!")


if __name__ == "__main__":
    analiz_yap('super_lig_verileri.csv')