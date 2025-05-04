# Langkah 1: Menulis ke file
with open('data1.txt', 'w') as file:
    file.write("Baris pertama\n")
    file.write("Baris kedua\n")
    file.write("Baris ketiga\n")

# Langkah 2: Membaca isi file dan menampilkannya
with open('data1.txt', 'r') as file:
    isi_file = file.read()
    print("Isi file:")
    print(isi_file)
