from uzay_oyunu.oyun import envanter_metni, hedef_menusu 


def test_envanter_metni_bos():
    assert envanter_metni(False, False, False) == ""


def test_envanter_metni_tek_esya():
    assert envanter_metni(True, False, False) == "Sende: bol kredi"
    assert envanter_metni(False, True, False) == "Sende: guclu motorlar"
    assert envanter_metni(False, False, True) == "Sende: yetenekli bir pilot"


def test_envanter_metni_coklu_esya():
    sonuc = envanter_metni(True, False, True)
    assert sonuc == "Sende: bol kredi, yetenekli bir pilot"

    hepsi = envanter_metni(True, True, True)
    assert hepsi == "Sende: bol kredi, guclu motorlar, yetenekli bir pilot"


def test_hedef_menusu_bos():
    beklenen = "Nereye gitmek istersin?"
    assert hedef_menusu([]) == beklenen 


def test_hedef_menusu_coklu_hedef():
    hedefler = ["centauri", "sirius"]
    beklenen = "Nereye gitmek istersin?\n[1] centauri\n[2] sirius"
    assert hedef_menusu(hedefler) == beklenen 
import pytest 
from uzay_oyunu.oyun import galaksi_kur 


def test_galaksi_kur_varsayilan_yakit():
    g = galaksi_kur(["mars"], {"mars": []}, "mars")
    assert g["yakit"] == 50
    assert g["konum"] == "mars"


def test_galaksi_kur_ozel_yakit():
    veri = {
        "gezegenler": ["dünya", "mars"],
        "baglantilar": {"dünya": ["mars"], "mars": ["dünya"]},
        "baslangic": "dünya",
        "yakit": 100,
    }
    g = galaksi_kur(**veri)
    assert g["konum"] == "dünya"
    assert g["yakit"] == 100


def test_galaksi_kur_hatali_baslangic():
    with pytest.raises(ValueError):
        galaksi_kur(["dünya"], {"dünya": []}, "jupiter")

def yakit_ekle(miktar: int, depo: list[int] | None = None) -> list[int]:
    """Depoya yakıt miktarı ekler ve güncel listeyi döndürür."""
    if depo is None:
        depo = []
    depo.append(miktar)
    return depo 
