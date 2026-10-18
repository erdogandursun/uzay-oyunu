import itertools 
from uzay_oyunu.akis import fibonacci 
def test_fibonacci_next(): 
    g = fibonacci() 
    assert (next(g), next(g), next(g)) == (0, 1, 1) 
def test_fibonacci_islice(): 
    sonuc = list(itertools.islice(fibonacci(), 12))
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    assert sonuc == beklenen 
def test_fibonacci_takewhile(): 
    sonuc = list(itertools.takewhile(lambda x: x < 100, fibonacci())) 
    beklenen = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] 
    assert sonuc == beklenen 
def test_fibonacci_uretec_durumu(): 
    g = fibonacci() 
    ilk_bes = list(itertools.islice(g, 5))
    sonraki_bes = list(itertools.islice(g, 5))
    assert ilk_bes == [0, 1, 1, 2, 3]
    assert sonraki_bes == [5, 8, 13, 21, 34]
    assert ilk_bes != sonraki_bes 
    