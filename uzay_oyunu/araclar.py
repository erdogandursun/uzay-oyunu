"""Yardımcı araçlar modülü."""

import functools
import time
from typing import Any, Callable


def hamle_sayaci() -> Callable[[], int]:
    """Her çağrıldığında 1 artan bir sayaç fonksiyonu döndürür."""
    sayac = 0

    def arttir() -> int:
        nonlocal sayac
        sayac += 1
        return sayac

    return arttir


def en_bagli_gezegenler(galaksi: dict[str, Any]) -> list[str]:
    """Gezegenleri bağlantı sayısına göre azalan, eşitlikte alfabetik sıralar."""
    gezegenler: list[str] = galaksi.get("gezegenler", list(galaksi["baglantilar"].keys()))
    baglantilar: dict[str, list[str]] = galaksi["baglantilar"]

    return sorted(
        gezegenler,
        key=lambda g: (-len(baglantilar.get(g, [])), g)
    )


def sure_olc(fonksiyon: Callable[..., Any]) -> Callable[..., Any]:
    """Verilen fonksiyonun çalışma süresini ölçen sarmalayıcı."""
    @functools.wraps(fonksiyon)
    def sarmalayici(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = fonksiyon(*args, **kwargs)
        bitis = time.perf_counter()
        sure = bitis - baslangic
        print(f"{fonksiyon.__name__} süresi: {sure:.6f} saniye")
        return sonuc

    return sarmalayici


if __name__ == "__main__":
    g = {
        "gezegenler": ["dünya", "centauri", "sirius", "orion", "kara_delik"],
        "baglantilar": {
            "sirius": ["a", "b", "c", "d"],
            "centauri": ["a", "b", "c"],
            "dünya": ["a", "b", "c"],
            "orion": ["a", "b"],
            "kara_delik": ["a"],
        },
    }

    # İstenen deneme adımı:
    en_bagli_gezegenler = sure_olc(en_bagli_gezegenler)
    print(en_bagli_gezegenler(g)) 