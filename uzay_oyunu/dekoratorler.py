from functools import wraps 
import time 
from typing import Any, Callable 


def sure_olc(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        baslangic = time.perf_counter()
        sonuc = func(*args, **kwargs)
        bitis = time.perf_counter()
        gecen_sure = bitis - baslangic 
        print(f"{func.__name__}: {gecen_sure:.4f} sn")
        return sonuc 

    return wrapper 