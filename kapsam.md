# Python Kapsam (Scope) ve LEGB Kuralı

Python değişken ararken LEGB sırasını izler: Local -> Enclosing -> Global -> Built-in. 

--- 

## Örnek 1: Global Değişkeni Okuma

```python 
x = 10

def f():
    print(x)

f()