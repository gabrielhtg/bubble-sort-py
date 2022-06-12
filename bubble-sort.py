import colorama
from colorama import Fore
from colorama import Style
import os
os.system("clear")

colorama.init()
print(Fore.YELLOW + Style.BRIGHT + "-----------------------------------------------------" + Style.RESET_ALL)
print(Fore.CYAN + Style.BRIGHT + "    Program ini akan mengurutkan angka yang anda\n   masukkan dari terkecil ke terbesar menggunakan\n               algoritma bubble sort." + Style.RESET_ALL)
print(Fore.YELLOW + Style.BRIGHT + "-----------------------------------------------------" + Style.RESET_ALL)
n = int(input("Masukkan banyak angka yang akan diurutkan : "))
arr = []
print(Fore.YELLOW + Style.BRIGHT + "-----------------------------------------------------" + Style.RESET_ALL)

for i in range(n) :
    print("    - Masukkan angka ke-" + str(i + 1), ": ", end="")
    arr.append(int(input()))

print(Fore.YELLOW + Style.BRIGHT + "-----------------------------------------------------" + Style.RESET_ALL)
print(Fore.RED + Style.BRIGHT + "Sebelum diurutkan   " + Fore.RESET, Fore.YELLOW + "-->" + Style.RESET_ALL, end=' ')
for i in range(n) :
    print(arr[i], end='')
    
    if i != (n-1) :
        print(end=", ")
print(Fore.YELLOW + Style.BRIGHT + "\n-----------------------------------------------------" + Style.RESET_ALL)

for i in range(n) :
    for j in range(n-i-1) :
        if arr[j] > arr[j + 1] :
            temp = arr[j + 1]
            arr[j + 1] = arr[j]
            arr[j] = temp

print(Fore.GREEN + Style.BRIGHT + "Setelah diurutkan   " + Fore.RESET, Fore.YELLOW + "-->" + Style.RESET_ALL, end=' ')
for i in range(n) :
    print(arr[i], end='')

    if i != (n-1) :
        print(end=", ")
print(Fore.YELLOW + Style.BRIGHT + "\n-----------------------------------------------------" + Style.RESET_ALL)