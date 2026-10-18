from uzay_oyunu.istatistik import (
    buyuk_harfli_gezegenler_comprehension,
    buyuk_harfli_gezegenler_map,
    en_az_iki_baglantili_comprehension,
    en_az_iki_baglantili_filter,
    hizli_yolculuk,
    toplam_baglanti_reduce,
    toplam_baglanti_sum,
)


def test_istatistik_fonksiyonlari():
    gezegenler = ["dünya", "centauri", "sirius", "orion", "kara_delik"]
    baglantilar = {
        "dünya": ["sirius", "orion"],
        "sirius": ["dünya", "orion", "centauri"],
        "orion": ["dünya", "sirius", "centauri"],
        "centauri": ["sirius", "orion"],
        "kara_delik": [],
    }

    beklenen_buyuk = ["DÜNYA", "CENTAURI", "SIRIUS", "ORION", "KARA_DELIK"]
    assert buyuk_harfli_gezegenler_map(gezegenler) == beklenen_buyuk
    assert buyuk_harfli_gezegenler_comprehension(gezegenler) == beklenen_buyuk

    beklenen_en_az_iki = ["dünya", "sirius", "orion", "centauri"]
    assert set(en_az_iki_baglantili_filter(baglantilar)) == set(beklenen_en_az_iki)
    assert set(en_az_iki_baglantili_comprehension(baglantilar)) == set(
        beklenen_en_az_iki
    )

    assert toplam_baglanti_reduce(baglantilar) == 10
    assert toplam_baglanti_sum(baglantilar) == 10

    assert (
        hizli_yolculuk("dünya", "sirius")
    )