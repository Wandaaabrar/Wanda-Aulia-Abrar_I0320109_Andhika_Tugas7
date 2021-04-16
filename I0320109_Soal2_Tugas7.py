#perhitungan mencari perpindahan Sea
import math
print("1. Sea mengendarai mobil ke arah utara sejauh 6 km. \nKemudian Sea  berbelok ke arah barat sejauh 4 km. \nBerapakah perpindahan yang dialami Sea?")
a = 6
b = 4
c = a ** 2 + b **2
print("Perpindahan Sea adalah ", math.sqrt(c))

# mencari nilai terbesar dan terkecil dari hasil panen koin shopee
print("\n2. Setelah menanam pohon koin shopee selama 3 hari,Wanda telah mengetahui jumlah koin yang didapatkannya. Pada hari pertama Wanda mendapat 70 koin, hari kedua dapat 150 koin, dan hari ketiga 90 koin.")
pertama = 70
kedua = 150
ketiga = 90
print("Jumlah koin tertinggi yang didapat Wanda = ", max(pertama, kedua, ketiga))
print("Jumlah koin terendah yang didapat Wanda = ", min(pertama, kedua, ketiga))

# mencari harga mutlak suatu nilai
a = 1209
b = -103
c = 444
print("\n3. Tentukan harga mutlak bilangan dibawah ini!")
print("a= ", a)
print("b= ", b)
print("c= ", c)
print("\n|a|= ", abs(a))
print("|b|= ", abs(b))
print("|c|= ", abs(c))