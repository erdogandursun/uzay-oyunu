from uzay_oyunu.araclar import hamle_sayaci, en_bagli_gezegenler 


def test_hamle_sayaci():
    sayac = hamle_sayaci()
    assert sayac() == 1
    assert sayac() == 2
    assert sayac() == 3

    yeni_sayac = hamle_sayaci()
    assert yeni_sayac() == 1


def test_en_bagli_gezegenler():
    galaksi = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "sirius": ["a", "b", "c", "d"],       # 4 bağlantı
            "centauri": ["a", "b", "c"],           # 3 bağlantı
            "dünya": ["a", "b", "c"],              # 3 bağlantı (centauri ile eşit, c alfabede d'den önce gelir)
            "orion": ["a", "b"],                   # 2 bağlantı
            "kara_delik": ["a"],                   # 1 bağlantı
        }
    }
    sirali = en_bagli_gezegenler(galaksi)
    assert sirali == ["sirius", "centauri", "dünya", "orion", "kara_delik"]