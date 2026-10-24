from functools import lru_cache
from uzay_oyunu.dekoratorler import say, sure_olc


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