# Dekoratör Sırası ve Çağrı Sayısı Analizi (Görev 2)

Özyinelemeli (recursive) Fibonacci fonksiyonu üzerinde `fib(20)` çağrısı yapıldığında dekoratör sıralamasının ürettiği çağrı sayıları ve nedenleri:

## 1. Yalnızca `@say`
- **Çağrı Sayısı:** 21891
- **Açıklama:** Herhangi bir önbellekleme (memoization) yapılmadığı için Fibonacci ağacındaki her alt problem tekrar tekrar hesaplanır. Bu durum $O(2^n)$ zaman karmaşıklığına yol açar ve `fib(20)` için fonksiyon tam 21,891 kez çağrılır.

## 2. `@say` Üstte, `@lru_cache` Altta
- **Çağrı Sayısı:** 39
- **Açıklama:** `@say` dekoratörü en dışta yer aldığı için, dışarıdan veya iç özyinelemeli (recursive) adımlardan gelen **HER çağrıyı** doğrudan sayaç kaydeder. `@lru_cache` alt katmanda çalıştığından, hesaplanmış bir değer istendiğinde önbellekten dönse bile çağrı önce `@say` katmanından geçtiği için sayaca yansır.

## 3. `@lru_cache` Üstte, `@say` Altta
- **Çağrı Sayısı:** 21
- **Açıklama:** `@lru_cache` en dışta olduğu için gelen çağrıları önce kendisi karşılar. Eğer istenen parametre önbellekte mevcutsa (cache hit), içteki `@say` fonksiyonuna hiç uğramadan sonucu doğrudan döndürür. Bu nedenle `@say` sayacı (`fib.__wrapped__.cagri`) yalnızca önbellekte bulunamayan ve **gerçekten hesaplanan** benzersiz durumlar için (0'dan 20'ye kadar olan 21 durum) tetiklenir. 