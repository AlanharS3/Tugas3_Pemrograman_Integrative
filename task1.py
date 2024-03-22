def main():
    # Buka file untuk dibaca
    with open('indata.txt', 'r') as file:
        # Baca semua baris dari file
        lines = file.readlines()

        # Inisialisasi jumlah
        total = 0

        # Iterasi setiap baris
        for line in lines:
            # Konversi setiap baris menjadi integer dan tambahkan ke total
            total += int(line)

    # Cetak total dengan pemisah koma dan dua angka desimal
    print("{:,.2f}".format(total))

if __name__ == "__main__":
    main()
