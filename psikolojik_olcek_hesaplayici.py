
# GEP1316 - Odev 3
# Psikolojik Olcek Puani Hesaplayicisi

# Kullanicidan ad veya takma ad alinir.
ad = input("Adiniz veya takma adiniz: ")

# Uc ornek olcek maddesinin puanlari alinir.
puan1 = int(input("1. madde puani (1-5): "))
puan2 = int(input("2. madde puani (1-5): "))
puan3 = float(input("3. madde puani (1-5): "))

# Puanlarin gecerli aralikta olup olmadigi kontrol edilir.
gecerli = (
    1 <= puan1 <= 5
    and 1 <= puan2 <= 5
    and 1 <= puan3 <= 5
)

# Gecerli puanlar icin toplam ve ortalama hesaplanir.
if gecerli:
    toplam = puan1 + puan2 + puan3
    ortalama = toplam / 3

    print(f"Merhaba {ad}!")
    print(f"Toplam puaniniz: {toplam:g}")
    print(f"Ortalama puaniniz: {ortalama:.2f}")
else:
    print("Hata: Puanlar 1 ile 5 arasinda olmalidir.")
