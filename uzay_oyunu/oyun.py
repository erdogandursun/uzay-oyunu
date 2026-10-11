import json
from typing import Any


def galaksi_kur(
    gezegenler: list[str],
    baglantilar: dict[str, list[str]],
    baslangic: str,
    **kwargs: Any 
) -> dict[str, Any]:
    """Galaksi haritasını ve başlangıç durumunu kurar.

    Args:
        gezegenler: Mevcut gezegenlerin listesi.
        baglantilar: Her gezegenden gidilebilecek diğer yerlerin sözlüğü.
        baslangic: Oyuna başlanacak gezegen adı.
        **kwargs: Ek parametreler (ör. yakit).

    Returns:
        dict: Galaksi durum sözlüğü (gezegenler, baglantilar, konum, yakit vb.).

    Raises:
        ValueError: Başlangıç gezegeni gezegenler listesinde yoksa.
    """
    if baslangic not in gezegenler:
        raise ValueError(f"Başlangıç gezegeni '{baslangic}' gezegenler listesinde bulunamadı!")

    yakit = kwargs.get("yakit", 50)

    galaksi: dict[str, Any] = {
        "gezegenler": gezegenler,
        "baglantilar": baglantilar,
        "konum": baslangic,
        "yakit": yakit,
    }

    for anahtar, deger in kwargs.items():
        if anahtar != "yakit":
            galaksi[anahtar] = deger 

    return galaksi  
def envanter_metni(credits: bool, engines: bool, copilot: bool) -> str:
    esyalar: list[str] = []
    if credits:
        esyalar.append("bol kredi")
    if engines:
        esyalar.append("guclu motorlar")
    if copilot:
        esyalar.append("yetenekli bir pilot")

    if not esyalar:
        return ""

    return f"Sende: {', '.join(esyalar)}"


def hedef_menusu(hedefler: list[str]) -> str:
    satirlar = ["Nereye gitmek istersin?"]
    for i, hedef in enumerate(hedefler, start=1):
        satirlar.append(f"[{i}] {hedef}")
    return "\n".join(satirlar)
def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Depoya yakıt miktarı ekler ve güncel listeyi döndürür.

    Args:
        miktar: Eklenecek yakıt miktarı.
        depo: Mevcut yakıt deposu listesi (varsayılan None).

    Returns:
        list[int]: Güncellenmiş yakıt deposu listesi.
    """
    if depo is None:
        depo = [] 
    depo.append(miktar)
    return depo 