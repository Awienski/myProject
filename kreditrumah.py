prices = {
    'rose' : 120000000,
    'gold' : 300000000,
    'pltn' : 360000000,
}
dp = 20/100
dp = int(dp)
kredit = {
    1 : 12,
    2 : 18,
    3 : 24,
}

print('\n*** PILIHAN TIPE RUMAH ***')
print('Tipe        Harga          Dp')
for item in prices:
    print(f'{item} \t {prices[item]} \t {int(prices[item]*20/100)}')

print('\n*** SIMULASI KREDIT ***')
print('No.        Jangka')
for k in kredit:
    print(f'{k} \t {kredit[k]}')

print('\n*** PILIH TIPE RUMAH ANDA ***')
N = input('Nama tipe(rose, gold, pltn) : ')
K = input('Jangka waktu Pembayaran(1,2,3) : ')
K = int(K)
N = str(N)

def cetak(item):
    print(f'\nTipe yang dipilih : {N}')
    print(f'Harga Rumah : {prices[item]}')
    print(f'Uang muka : {prices[item]*20/100}')
    sisa = prices[item] - (prices[item]*20/100)
    print(f'Sisa : {sisa}')
    print(f'Lama kredit : {kredit[K]} bulan')
    angsuran = sisa/ kredit[K]
    angsuran = int(angsuran)
    print(f'Angusran : {angsuran}')
    print('\n*** TABEL ANGSURAN ***')
    print('Bulan Ke-   Angsuran \t Sisa')
    for item in range(kredit[K]):
        sisa -= angsuran
        sisa = int(sisa)
        print(f'{item+1}\t\t{angsuran} \t {sisa}')

for item in prices:
    if N == item:
        cetak(item)
    elif N == item:
        cetak(item)
    elif N == item:
        cetak(item)

    
