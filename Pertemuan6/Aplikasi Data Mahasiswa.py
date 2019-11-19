nim = []
nama = []
alamat = []
kelas = []

pilihan = 1
while pilihan != 0:
    print("1. Menambah data Mahasiswa")
    print("2. Mengubah data Mahasiswa")
    print("3. Menghapus data Mahasiswa")
    print("4. Melihat data Mahasiswa")
    print("5. Keluar")

    pilihan = int(input("masukan pilihan anda : "))
    print('')
    print('')
    print('')
    if pilihan == 1:
        tmbhnim = input("Tambahkan nim : ")
        nim.append({'nim': tmbhnim})
        tmbhnama = input("Tambahkan nama : ")
        nama.append({'nama': tmbhnama})
        tmbhalamat = input("Tambahkan Alamat : ")
        alamat.append({'Alamat': tmbhalamat})
        tmbhkelas = input("Tambahkan Kelas : ")
        kelas.append({'Kelas': tmbhalamat})

    elif pilihan == 2:
        ubhnim = input("Ubah nim : ")
        nim.append({'nim' : ubhnim})
        ubhnama = input("Ubah Nama : ")
        nama.append({'nama' : ubhnama})
        ubhalamat = input("Ubah Alamat")
        ubhalamat.append({'alamat' : ubhalamat})
        ubhkelas = input("kelas : ")
        ubhkelas.append({'kelas' : ubhkelas})

    elif pilihan == 3:
        masnim = input("masukan nim : ")
        for i in range(len(nim)):
            if masnim == nim[i]['nim']:
                print(i)
                del nim[i]
                del nama[i]
                del alamat[i]
                del kelas[i]
                break
    elif pilihan == 4:
        penentu = True
        for i in range(len(nim)):
            if penentu:
                print("nim\tnama\talamat")
            print(nim[i]['nim'], '\t', nama[i]['nama'], '\t', alamat[i]['alamat'], '\t', kelas[i]['kelas'])
            penentu = False
    print('')
    print('')
    print('')
    print('')