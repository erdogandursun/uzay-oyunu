from uzay_oyunu.dekoratorler import sure_olc


def test_sure_olc_sonuc_degismeden_donuyor_mu():

    @sure_olc
    def topla(a, b):
        """Toplama işlemi yapar."""
        return a + b

    assert topla(3, 5) == 8


def test_sure_olc_adli_argumanlar_calisiyor_mu():

    @sure_olc
    def selamlama(isim, mesaj="Merhaba"):
        return f"{mesaj}, {isim}!"

    assert selamlama(isim="Ahmet", mesaj="Selam") == "Selam, Ahmet!"


def test_sure_olc_metadata_korunuyor_mu():

    @sure_olc
    def ornek_fonksiyon():
        """Bu örnek bir dokümantasyon metnidir."""
        pass

    assert ornek_fonksiyon.__name__ == "ornek_fonksiyon"
    assert ornek_fonksiyon.__doc__ == "Bu örnek bir dokümantasyon metnidir."