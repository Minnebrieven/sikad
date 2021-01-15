#nama : MOCH FIKRI RAMADHAN
#nim : 0110120014
#prodi : Sistem Informasi 02
def nim_parser():
    while True:
        nim = input("Masukan NIM anda = ")
        if len(nim) == 10:
            break
        else:
            print("NIM Salah!")

    nim_tahun = nim[5:7]
    nim_urut = nim[7:]
    return (nim_tahun, nim_urut)

def sks_parser(thn):
    if thn == 20:
        print("Anda Angkatan Pertama, anda bisa mengambil 20 SKS")
        return 20
    elif thn == 19:
        print("Anda Angkatan Kedua, anda bisa mengambil 22 SKS")
        return 22
    elif thn == 18:
        print("Anda Angkatan Ketiga, anda bisa mengambil 24 SKS")
        return 24
    elif thn == 17:
        print("Anda Angkatan Keempat, anda bisa mengambil 26 SKS")
        return 26
    else:
        print("Anda tidak termasuk diangkatan!")
        return 0

def sks_chooser(sks):
    choosed_sks = []
    sks_counter = 0
    sks_left = sks
    while True:
        if sks_left == 0 or sks == 0:
            break
        print("\nJumlah SKS yang telah diambil : ", sks_counter, "\nSisa SKS yang bisa diambil : ", sks_left)
        matkul = input("Masukan nama Matkul yang ingin diambil. Masukan X untuk selesai : ")
        if matkul == "x" or matkul == "X":
            confirm = input("Apakah anda yakin ingin selesai? (yes/no) : ")
            if confirm == "y" or confirm =="yes":
                break
            else:
                continue
        else:
            the_sks = int(input("Masukan beban SKS matkul : "))
            if the_sks > sks_left:
                print("Gagal - SKS yang tersisa : ",sks_left)
            else:    
                choosed_sks.append([matkul, the_sks])
                sks_counter += the_sks
                sks_left -= the_sks
    return choosed_sks

def view_sks(item):
    if item == []:
        pass
    else:
        print("\n===Matkul dan SKS yang telah diambil===")
        for i in item:
            print("Matkul : ",i[0], " - ",i[1], " SKS")

def main():
    print("===Fitur Pengisian Rencana Studi===")
    tahun, urut = nim_parser()
    matkul_sks = sks_chooser(sks_parser(int(tahun)))
    view_sks(matkul_sks)

main()
