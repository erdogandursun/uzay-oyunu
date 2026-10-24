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
def say(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        wrapper.cagri += 1
        return func(*args, **kwargs)

    wrapper.cagri = 0
    return wrapper 
def log_cagri(func: Callable[..., Any]) -> Callable[..., Any]:

    @wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        # Argümanları biçimlendirme
        arg_str_list = [repr(a) for a in args]
        kwarg_str_list = [f"{k}={v!r}" for k, v in kwargs.items()]
        tum_argumanlar = ", ".join(arg_str_list + kwarg_str_list)

        print(f"-> {func.__name__}({tum_argumanlar})")
        sonuc = func(*args, **kwargs)
        print(f"<- {func.__name__} = {sonuc!r}")
        return sonuc 

    return wrapper 