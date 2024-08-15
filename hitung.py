from rich.console import Console
from rich.panel import Panel
from termcolor import colored

# HEADER TOOLS
def print_header():
    console = Console()
    console.print(Panel.fit("[bold magenta]KALKULATOR[/bold magenta]\n[cyan]Mesin hitung sederhana[/cyan]", 
                            title="Welcome", 
                            subtitle="Santri IT", 
                            border_style="green"))

print_header()

# ITEM KALKULATOR
print('')
print('[1] Tambah \t [+]')
print('[2] Kurang \t [-]')
print('[3] Kali \t [x]')
print('[4] Bagi \t [:]')
print('=' * 26)
print('=' * 26)


# OPERASI TOOLS
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
    exit()


bilangan_1 = eval(input(colored("[1] Angka pertama : ",'yellow')))
bilangan_2 = eval(input(colored("[2] Angka kedua : ",'yellow')))
print("")

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
