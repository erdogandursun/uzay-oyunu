from functools import lru_cache 
from typing import Dict, Iterator, List, Tuple 
from typing import Iterator, Tuple 
from typing import Iterator 
def fibonacci() -> Iterator[int]: 
    a, b = 0, 1
    while True:
        yield a 
        a, b = b, a + b 
def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]: 
    mevcut_yakit = yakit 
    while mevcut_yakit > 0: 
        mevcut_yakit -= tuketim 
        if mevcut_yakit <= 0: 
            yield 0 
            break 
        yield mevcut_yakit 
def satirlari_oku(yol: str) -> Iterator[str]:
    with open(yol, "r", encoding="utf-8") as f:
        for satir in f:
            temiz = satir.strip()
            if temiz and not temiz.startswith("#"):
                yield temiz 


def ayristir(satirlar: Iterator[str]) -> Iterator[Tuple[str, str, int]]:
    for satir in satirlar:
        parcalar = satir.split("->")
        kaynak = parcalar[0].strip()
        hedef_ve_yakit = parcalar[1].strip().split()
        hedef = hedef_ve_yakit[0].strip()
        yakit = int(hedef_ve_yakit[1])
        yield (kaynak, hedef, yakit)


def uzun_yolculuklar(
    kayitlar: Iterator[Tuple[str, str, int]], esik: int 
) -> Iterator[Tuple[str, str, int]]:
    for kayit in kayitlar:
        if kayit[2] > esik:
            yield kayit         
def rota_sayaci(baglantilar: Dict[str, List[str]]):

    @lru_cache(maxsize=None)
    def rota_sayisi(gezegen: str, adim: int) -> int:
        if adim == 0:
            return 1
        toplam = 0
        for komsu in baglantilar.get(gezegen, []):
            toplam += rota_sayisi(komsu, adim - 1)
        return toplam 

    return rota_sayisi 