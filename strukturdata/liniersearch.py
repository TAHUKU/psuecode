def linear_search(list_data, target):
    # n adalah panjang list
    for i in range(len(list_data)):
        # Cek apakah elemen saat ini sama dengan target
        if list_data[i] == target:
            return i  # Kembalikan indeks jika ketemu
            
    return -1  # Kembalikan -1 jika tidak ketemu sampai akhir

# Data acak (tidak perlu di-sort!)
data = [10, 50, 30, 100, 80, 20, 70]
target = 70

hasil = linear_search(data, target)

if hasil != -1:
    print(f"Target {target} ditemukan pada indeks ke-{hasil}")
else:
    print("Target tidak ditemukan")