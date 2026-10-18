import itertools 
from uzay_oyunu.akis import ( 
    ayristir, 
    fibonacci, 
    rota_sayaci, 
    satirlari_oku, 
    uzun_yolculuklar, 
    yakit_gostergesi, 
) 

from uzay_oyunu.akis import fibonacci, yakit_gostergesi  
def test_fibonacci_next(): 
    g = fibonacci() 
    assert (next(g), next(g), next(g)) == (0, 1, 1) 
def test_fibonacci_islice(): 
    sonuc = list(itertools.islice(fibonacci(), 12))
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert sonuc == beklenen 
def test_fibonacci_takewhile(): 
    sonuc = list(itertools.takewhile(lambda x: x < 100, fibonacci())) 
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
    assert sonuc == beklenen 
def test_fibonacci_uretec_durumu(): 
    g = fibonacci() 
    ilk_bes = list(itertools.islice(g, 5))
    sonraki_bes = list(itertools.islice(g, 5))
    assert ilk_bes == [0, 1, 1, 2, 3]
    assert sonraki_bes == [5, 8, 13, 21, 34]
    assert ilk_bes != sonraki_bes 
def test_yakit_gostergesi(): 
    sonuc = list(yakit_gostergesi(100, 30)) 
    assert sonuc == [70, 40, 10, 0] 


def test_yakit_gostergesi_tam_bolunen(): 
    sonuc = list(yakit_gostergesi(100, 50)) 
    assert sonuc == [50, 0] 
def test_veri_boru_hatti():
    dosya_yolu = "veri/seyir.txt"

    toplam_yakit = sum(y for _, _, y in ayristir(satirlari_oku(dosya_yolu)))
    assert toplam_yakit == 88

    kayitlar = ayristir(satirlari_oku(dosya_yolu))
    hedefler = [h for _, h, _ in uzun_yolculuklar(kayitlar, 10)]
    assert hedefler == ["sirius", "centauri", "orion", "kara_delik"]

def test_rota_sayaci(): 
    baglantilar = {
        "dünya": ["sirius", "orion", "centauri"],
        "sirius": ["dünya", "orion", "centauri"],
        "orion": ["dünya", "sirius", "centauri"],
        "centauri": ["dünya", "sirius", "orion"],
    }
    say = rota_sayaci(baglantilar)
    say.cache_clear()
    assert say("dünya", 3) == 27 