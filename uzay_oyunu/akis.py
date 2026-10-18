from typing import Iterator 
def fibonacci() -> Iterator[int]: 
    a, b = 0, 1
    while True:
        yield a 
        a, b = b, a + b 
def yakit_gostergesi(yakit: int, tuketim: int) -> Iterator[int]: 
    mevcut_yakit = yakit 
    while mevcut_yakit > 0: 
        mevcut_yakit -= tuketim 
        if mevcut_yakit <= 0: 
            yield 0 
            break 
        yield mevcut_yakit 
        