def gorev_kaydi(
    baslik: str,
    *adimlar: str,
    oncelik: str = "normal",
    **ekler: str
) -> None:
    """Görev başlığını, adımlarını ve ek ayrıntıları biçimlendirerek ekrana basar.

    Args:
        baslik: Görevin başlığı.
        *adimlar: Görevin sırayla tamamlanması gereken adımları.
        oncelik: Sadece isimle (keyword-only) verilebilen öncelik derecesi.
        **ekler: Göreve ait ek anahtar-değer bilgileri (örn. sorumlu).
    """
    print(f"[{oncelik.upper()}] {baslik}")

    for i, adim in enumerate(adimlar, start=1):
        print(f"{i}. {adim}")

    for anahtar, deger in ekler.items():
        print(f" {anahtar}: {deger}")


if __name__ == "__main__":
    gorev_kaydi(
        "Kara deliğe atla",
        "Kredi kazan",
        "Pilot bul",
        "Hiperdrive al",
        oncelik="yüksek",
        sorumlu="Ayşe",
    )

    print("-" * 30)

    gorev_listesi = ["Kredi kazan", "Pilot bul", "Hiperdrive al"]
    ek_bilgiler = {"sorumlu": "Ayşe"}

    gorev_kaydi(
        "Kara deliğe atla",
        *gorev_listesi,
        oncelik="yüksek",
        **ek_bilgiler 
    )