import pytest
from uzay_oyunu.komutlar import KOMUTLAR, komut, komut_envanter, komut_harita, komut_yardim


def test_komut_kayit_ve_duplike_kontrolu():

    @komut("test_komut", "test açıklaması")
    def ornek_komut(durum):
        return "ok"

    assert "test_komut" in KOMUTLAR
    assert KOMUTLAR["test_komut"][1] == "test açıklaması"

    # Aynı adla tekrar kayıt yapıldığında ValueError fırlatmalı
    with pytest.raises(ValueError):

        @komut("test_komut", "çakışan komut")
        def cakisan_komut(durum):
            pass


def test_yardim_komutu():
    durum = {}
    cikti = komut_yardim(durum)
    assert "yardim komutları listeler" in cikti
    assert "envanter eşyalarını gösterir" in cikti
    assert "harita gidebileceğin gezegenleri gösterir" in cikti


test_durum = {
    "konum": "dünya",
    "baglantilar": {
        "dünya": ["orion", "sirius"],
    },
    "credits": 100,
    "engines": 2,
    "copilot": True,
}


def test_envanter_komutu():
    cikti = komut_envanter(test_durum)
    assert "100" in cikti
    assert "2" in cikti


def test_harita_komutu():
    cikti = komut_harita(test_durum)
    assert "orion" in cikti
    assert "sirius" in cikti