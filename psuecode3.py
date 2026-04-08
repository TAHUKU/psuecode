A = int(input("Masukkan nilai A: "))
B = int(input("Masukkan nilai B: "))
C = int(input("Masukkan nilai C: "))

bilangan_terbesar = A

if B > bilangan_terbesar:
    bilangan_terbesar = B

if C > bilangan_terbesar:
    bilangan_terbesar = C

print("Bilangan terbesar adalah:", bilangan_terbesar)