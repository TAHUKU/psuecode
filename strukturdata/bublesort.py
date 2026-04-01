def bubble_sort(arr):
    n = len(arr)
    # Proses mengapungkan angka terbesar ke kanan
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Tukar posisi jika angka kiri lebih besar dari kanan
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2  # Rumus pembagian indeks (bulat ke bawah)
        
        if arr[mid] == target:
            return mid  # Berhasil menemukan indeksnya!
        elif arr[mid] < target:
            low = mid + 1  # Target di kanan, geser pagar kiri
        else:
            high = mid - 1 # Target di kiri, geser pagar kanan
            
    return -1  # Data tidak ditemukan

# --- UJI COBA ---
data_acak = [64, 34, 25, 12, 22, 11, 90]
target = 10

# 1. Rapikan dulu
data_urut = bubble_sort(data_acak)
print(f"Data Terurut: {data_urut}")

# 2. Cari target
hasil = binary_search(data_urut, target)

if hasil != -1:
    print(f"Angka {target} ditemukan pada indeks ke-{hasil}")
else:
    print(f"Angka {target} tidak ada dalam data.")