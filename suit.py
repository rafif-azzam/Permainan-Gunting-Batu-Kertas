import random

print("==============")
print("Permainan Suit")
print("==============")

print("")
def permainan():
    print("Pilihan : ")
    print("1. Gunting")
    print("2. Batu")
    print("3. Kertas")
    print("pencet huruf jika ingin keluar")

    kamu = int(input("Masukkan Pilihanmu : "))
    kom = random.choice(["Gunting", "Batu", "Kertas" ])
    if kamu == 1:
        print("Kamu     : Gunting")
        print("Komputer : ", kom)
        if kom == "Gunting":
            print("\tSeri")
        if kom == "Batu":
            print("\tKamu kalah")
        if kom == "Kertas":
            print("\tKamu menang")

    if kamu == 2:
        print("Kamu     : Batu")
        print("Komputer : ", kom)
        if kom == "Gunting":
            print("\tKamu menang")
        if kom == "Batu":
            print("\tSeri")
        if kom == "Kertas":
            print("\tKamu kalah")

    if kamu == 3:
        print("Kamu     : Kertas")
        print("Komputer : ", kom)
        if kom == "Gunting":
            print("\tKamu kalah")
        if kom == "Batu":
            print("\tKamu menang")
        if kom == "Kertas":
            print("\tSeri")

    if kamu >= 4:
        print("Pilihan tidak tersedia")
    if kamu == 0:
        print("Mode cheat diaktifkan(belum bisa digunakan)")
        pilihan()
        permainan()

while True:
    permainan()