import time
from functools import partial, reduce
from typing import Any, Callable, Dict, List

# Yorum Satırı: Hangisi Daha Okunaklı?
# Liste üreteçleri (list comprehensions) ve sum() gibi Pythonic yapılar;
# map(), filter() ve reduce() fonksiyonlarına göre çok daha okunaklı, açık ve
# lambda kullanımına ihtiyaç duymadığı için anlaşılması çok daha kolaydır.


def buyuk_harfli_gezegenler_map(gezegenler: List[str]) -> List[str]:
    """map kullanarak gezegen adlarını büyük harfe çevirir."""
    return list(map(lambda g: g.upper(), gezegenler))


def buyuk_harfli_gezegenler_comprehension(gezegenler: List[str]) -> List[str]:
    """Liste üreteci kullanarak gezegen adlarını büyük harfe çevirir."""
    return [g.upper() for g in gezegenler]


def en_az_iki_baglantili_filter(baglantilar: Dict[str, List[str]]) -> List[str]:
    """filter kullanarak en az iki bağlantısı olan gezegenleri bulur."""
    return list(filter(lambda g: len(baglantilar[g]) >= 2, baglantilar))


def en_az_iki_baglantili_comprehension(
    baglantilar: Dict[str, List[str]]
) -> List[str]:
    """Liste üreteci kullanarak en az iki bağlantısı olan gezegenleri bulur."""
    return [g for g, komsular in baglantilar.items() if len(komsular) >= 2]


def toplam_baglanti_reduce(baglantilar: Dict[str, List[str]]) -> int:
    """reduce kullanarak toplam bağlantı sayısını hesaplar."""
    return reduce(lambda acc, komsular: acc + len(komsular), baglantilar.values(), 0)


def toplam_baglanti_sum(baglantilar: Dict[str, List[str]]) -> int:
    """sum() kullanarak toplam bağlantı sayısını hesaplar."""
    return sum(len(komsular) for komsular in baglantilar.values())


# --- partial Kullanımı ---
def yolculuk(baslangic: str, bitis: str, hiz: int) -> str:
    """Yolculuk mesajı üreten örnek fonksiyon."""
    return f"{baslangic} noktasından {bitis} noktasına {hiz} hızıyla gidiliyor."


# hiz=3 parametresi sabitlenmiş yeni fonksiyon
hizli_yolculuk = partial(yolculuk, hiz=3)


# --- BONUS (+10 Puan): Zamanlayıcı Üreteci ve Meşgul Bekleme (Busy Waiting) ---
def zamanlayici(aralik: float):
    """Belirli aralıklarla sinyal veren üreteç."""
    son_zaman = time.time()
    while True:
        simdi = time.time()
        if simdi - son_zaman >= aralik:
            son_zaman = simdi
            yield simdi


def saat_simulasyonu():
    """10 saniye boyunca her 2 saniyede 'tik', her 5 saniyede 'tak' yazar.

    Neden "Meşgul Bekleme" (Busy Waiting)?
    Bu döngü, sürenin dolup dolmadığını kontrol etmek için CPU'yu sürekli %100 yükte
    çalıştırarak döngü atar (polling yapar). CPU hiç dinlenmez.

    time.sleep() Farkı:
    time.sleep(n) işletim sistemine "bu iş parçacığını n saniye boyunca uyut" çağrısı yapar.
    İşletim sistemi bu sürede CPU kaynaklarını diğer işlemlere devreder, CPU tüketimi %0 olur.
    """
    baslangic = time.time()
    tik_zamanlayici = zamanlayici(2)
    tak_zamanlayici = zamanlayici(5)

    print("Saat simülasyonu başladı (10 saniye)...")
    while time.time() - baslangic <= 10:
        # Zamanlayıcılardan adım al
        next(tik_zamanlayici, None)
        next(tak_zamanlayici, None)


if __name__ == "__main__":
    # Test çalıştırması
    gezegenler = ["dünya", "centauri", "sirius", "orion", "kara_delik"]
    baglantilar = {
        "dünya": ["sirius", "orion"],
        "sirius": ["dünya", "orion", "centauri"],
        "orion": ["dünya", "sirius", "centauri"],
        "centauri": ["sirius", "orion"],
        "kara_delik": [],
    }

    print("Map:", buyuk_harfli_gezegenler_map(gezegenler))
    print("Comprehension:", buyuk_harfli_gezegenler_comprehension(gezegenler))
    print("Filter:", en_az_iki_baglantili_filter(baglantilar))
    print("Comprehension:", en_az_iki_baglantili_comprehension(baglantilar))
    print("Reduce:", toplam_baglanti_reduce(baglantilar))
    print("Sum:", toplam_baglanti_sum(baglantilar))
    print("Partial:", hizli_yolculuk("dünya", "sirius"))