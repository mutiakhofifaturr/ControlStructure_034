a = float(input("\nMasukkan bilangan pertama: "))
b = float(input("\nMasukkan bilangan kedua: "))
c = float(input("\nMasukkan bilangan ketiga: "))

if a >= b and a >= c:
    print("Angka terbesar adalah:", a)
elif b >= a and b >= c:
    print("Angka terbesar adalah:", b)
else :
    print("Angka terbesar adalah:", c)
