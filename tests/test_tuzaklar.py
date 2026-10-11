from uzay_oyunu.oyun import yakit_ekle


def test_yakit_ekle_bagimsiz_cagrilar():
    depo1 = yakit_ekle(10)
    assert depo1 == [10]

    depo2 = yakit_ekle(20)
    assert depo2 == [20] 
    