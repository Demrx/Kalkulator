from termcolor import colored

print('=' * 31)
print(colored("Kalkulator sederhana By : Demrx",'light_green'))
print('=' * 31)
print(' 1. Tambah \t [+]')
print(' 2. Kurang \t [-]')
print(' 3. Kali \t [x]')
print(' 4. Bagi \t [:]')
print('=' * 31)
print('=' * 31)

operasi = input('[?] Pilih operasi (1/2/3/4) : ')
if operasi == '1':
    print('[+] User memilih penjumlahan')
elif operasi == '2':
    print('[-] User memilih pengurangan')
elif operasi == '3':
    print('[x] User memilih perkalian')
elif operasi == '4':
    print('[:] User memilih pembagian')
else:
    print(colored("[!] Tidak valid",'red'))


bilangan_1 = eval(input(colored("[1] Angka pertama : ",'yellow')))
bilangan_2 = eval(input(colored("[2] Angka kedua : ",'yellow')))

#logika

if operasi == '1':
    hasil = bilangan_1 + bilangan_2
    print(f'[=] Hasil dari {bilangan_1} + {bilangan_2} = {hasil}')
elif operasi == '2':
    hasil = bilangan_1 - bilangan_2
    print(f'[=] Hasil dari {bilangan_1} - {bilangan_2} = {hasil}')
elif operasi == '3':
    hasil = bilangan_1 * bilangan_2
    print(f'[=] Hasil dari {bilangan_1} x {bilangan_2} = {hasil}')
elif operasi == '4':
    hasil = bilangan_1 / bilangan_2
    print(f'[=] Hasil dari {bilangan_1} : {bilangan_2} = {hasil}')
else:
    print(colored("[!] Tidak valid!",'red'))
