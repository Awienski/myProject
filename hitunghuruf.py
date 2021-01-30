#Diketahui 
kalimat = 'saya mau makan sate bersama teman saya setelah lulus dari sekolah dasar'
huruf = 'a'

# menggunakan function dari python yaitu count
n = kalimat.count(huruf)
print('Cara 2 :')
print(f"hasil hitung huruf '{huruf}' muncul sebanyak {n} kali")

# menggunakan fungsi buatan sendiri
def hitungHurufdariKalimat(huruf, kalimat):
    n = 0
    for x in kalimat:
        if x == huruf:
            n+=1
    return n

# cetak dengan memanggil fungsi dan menghitung jumlah berdasarkan
hasil = hitungHurufdariKalimat(huruf, kalimat)
print('Cara 2 :')
print(f"hasil hitung huruf '{huruf}' muncul sebanyak {hasil} kali")

