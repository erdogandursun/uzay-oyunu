from functools import wraps
from typing import Any, Callable, Dict, Tuple

# Komutların kaydedileceği küresel sözlük: {komut_adi: (fonksiyon, aciklama)}
KOMUTLAR: Dict[str, Tuple[Callable[..., Any], str]] = {}


def komut(ad: str, aciklama: str = ""):

    def dekorator(func: Callable[..., Any]) -> Callable[..., Any]:
        if ad in KOMUTLAR:
            raise ValueError(f"'{ad}' isimli komut zaten kayıtlı!")

        KOMUTLAR[ad] = (func, aciklama)

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            return func(*args, **kwargs)

        return wrapper

    return dekorator


# --- ÖRNEK KOMUTLAR ---


@komut("yardim", "komutları listeler")
def komut_yardim(durum: Dict[str, Any]) -> str:
    satirlar = [f"{ad} {bilgi[1]}" for ad, bilgi in sorted(KOMUTLAR.items())]
    return "\n".join(satirlar)


@komut("envanter", "eşyalarını gösterir")
def komut_envanter(durum: Dict[str, Any]) -> str:
    """Oyuncunun envanterindeki eşyaları gösterir."""
    credits = durum.get("credits", 0)
    engines = durum.get("engines", 1)
    copilot = "Var" if durum.get("copilot") else "Yok"
    return (
        f"Kredi: {credits}, Motor Seviyesi: {engines}, Yardımcı Pilot: {copilot}"
    )


@komut("harita", "gidebileceğin gezegenleri gösterir")
def komut_harita(durum: Dict[str, Any]) -> str:
    konum = durum.get("konum", "")
    baglantilar = durum.get("baglantilar", {})
    komsular = baglantilar.get(konum, [])
    return ", ".join(komsular)