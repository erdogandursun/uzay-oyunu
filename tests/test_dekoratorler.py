from functools import lru_cache
from uzay_oyunu.dekoratorler import say, sure_olc
from uzay_oyunu.dekoratorler import log_cagri, say, sure_olc
from functools import lru_cache
import pytest
from uzay_oyunu.dekoratorler import hafiza, sinirla


def test_sinirla_dekoratoru():

    @sinirla(0, 100)
    def yakit_harca_test(miktar):
        return 100 - miktar

    # Normal ve sınır değerler
    assert yakit_harca_test(30) == 70
    assert yakit_harca_test(0) == 100
    assert yakit_harca_test(100) == 0

    # Aralık dışı değerler (ValueError bekleniyor)
    with pytest.raises(ValueError) as exc_info:
        yakit_harca_test(150)
    assert "150 değeri 0-100 aralığında değil" in str(exc_info.value)

    with pytest.raises(ValueError):
        yakit_harca_test(-10)


def test_hafiza_vs_lru_cache_bonus():

    cagri_hafiza = 0
    cagri_lru = 0

    @hafiza(maxsize=2)
    def kare_hafiza(x):
        nonlocal cagri_hafiza
        cagri_hafiza += 1
        return x * x

    @lru_cache(maxsize=2)
    def kare_lru(x):
        nonlocal cagri_lru
        cagri_lru += 1
        return x * x

    # İlk çağrılar
    assert kare_hafiza(2) == kare_lru(2) == 4
    assert kare_hafiza(3) == kare_lru(3) == 9

    # Önbellekten dönmeli (çağrı sayıları artmamalı)
    assert kare_hafiza(2) == kare_lru(2) == 4
    assert cagri_hafiza == 2
    assert cagri_lru == 2

    # Maxsize (2) dolduğu için en eski (2) silinecek, 4 eklenecek
    assert kare_hafiza(4) == kare_lru(4) == 16
    assert cagri_hafiza == 3
    assert cagri_lru == 3 

def test_log_cagri_dekoratoru(capsys): 

    @log_cagri
    def yolculuk(hedef, hiz=1):
        return f"{hedef} hiz={hiz}"

    sonuc = yolculuk("orion", hiz=3)

    assert sonuc == "orion hiz=3"

    captured = capsys.readouterr()
    assert "-> yolculuk('orion', hiz=3)" in captured.out 
    assert "<- yolculuk = 'orion hiz=3'" in captured.out 

# --- GÖREV 1 TESTLERİ ---
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


# --- GÖREV 2 TESTLERİ ---
def test_say_dekoratoru():

    @say
    def kare_al(x):
        return x * x

    assert kare_al.cagri == 0
    kare_al(4)
    kare_al(5)
    assert kare_al.cagri == 2


def test_dekorator_siralamasi_fibonacci():

    # 1. Yalnızca @say
    @say
    def fib1(n):
        if n < 2:
            return n
        return fib1(n - 1) + fib1(n - 2)

    fib1(20)
    assert fib1.cagri == 21891

    # 2. @say üstte, @lru_cache altta
    @say
    @lru_cache(maxsize=None)
    def fib2(n):
        if n < 2:
            return n
        return fib2(n - 1) + fib2(n - 2)

    fib2(20)
    assert fib2.cagri == 39

    # 3. @lru_cache üstte, @say altta
    @lru_cache(maxsize=None)
    @say
    def fib3(n):
        if n < 2:
            return n
        return fib3(n - 1) + fib3(n - 2)

    fib3(20)
    assert fib3.__wrapped__.cagri == 21