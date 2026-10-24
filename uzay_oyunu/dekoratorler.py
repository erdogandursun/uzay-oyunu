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
def sinirla(alt: float, ust: float):

    def dekorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            if args:
                deger = args[0]
                if not (alt <= deger <= ust):
                    raise ValueError(
                        f"{func.__name__}: {deger} değeri {alt}-{ust} aralığında değil"
                    )
            return func(*args, **kwargs)

        return wrapper

    return dekorator


# --- BONUS (+10 Puan): Custom Önbellek Dekoratörü ---
def hafiza(maxsize: int | None = None):

    def dekorator(func: Callable[..., Any]) -> Callable[..., Any]:
        onbellek: Dict[Tuple[Any, ...], Any] = {}

        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            # Argümanları tuple olarak anahtar yap
            anahtar = args + tuple(sorted(kwargs.items()))

            if anahtar in onbellek:
                return onbellek[anahtar]

            sonuc = func(*args, **kwargs)

            # Maxsize sınırı kontrolü
            if maxsize is not None and len(onbellek) >= maxsize:
                # En eski girdiyi (ilk eklenen anahtarı) sil
                ilk_anahtar = next(iter(onbellek))
                del onbellek[ilk_anahtar]

            onbellek[anahtar] = sonuc
            return sonuc

        return wrapper

    return dekorator 
