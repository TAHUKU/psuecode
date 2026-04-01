# 1.variable untuk menampung total
total_keseluruhan = 0

while True: 
    barang = input("Masukkan nama barang: ")
    harga = int(input("Masukkan harga barang: "))
    jumlah = int(input("Masukkan jumlah barang: "))

    # 2. Menghitung barang dan tambah ke variable total_keseluruhan
    subtotal = harga * jumlah
    total_keseluruhan += subtotal

    barang_baru = input("Apakah ada barang yang ingin di tambah? (ya/tidak): ").lower()

    # 3. Cek apakah harus berhenti
    if barang_baru == "tidak":
        break

# 4. Tampilkan nota hasil belanja
print("--- NOTA BELANJA ---")
print(f"Total yang harus dibayar: Rp {total_keseluruhan}")
