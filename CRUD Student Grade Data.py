
import sys
import csv
import tabulate
import os
import pyinputplus as pypi

# Fungsi untuk menampilkan data nilai
def ShowData(dbDataNilai):  
    print("\nData Nilai Kelulusan SMP Maju Jaya Yogyakarta\n")
    data = list(dbDataNilai.values())[1:]
    header = dbDataNilai['column']
    print(tabulate.tabulate(data, header, tablefmt="outline"))
    print("\n")
    
def SubMenu ():
    
    print("\nData Nilai Kelulusan Siswa SMP Maju Jaya\n")  # Menampilkan Judul
    while True:
        # Menampilkan tampilan sub menu utama program menu
        choice = ["Menampilkan Daftar Data Nilai Keseluruhan", 
                  "Search Daftar Data Nilai Siswa", 
                  "Kembali ke Menu Utama"]
        response = pypi.inputMenu(choices=choice, numbered=True)
        if response == choice[0]:
            ShowData(dbDataNilai)
        elif response == choice[1]:
            CariData()
        elif response == choice[2]:
            MainMenu = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu Utama ?(yes/no) ')
            if MainMenu == "yes":
                main()
            elif MainMenu == "no":
                SubMenu(dbDataNilai)
            
def CariData ():
    print("\nSearch Daftar Data Nilai Siswa\n")
    while True:
        choice = ["Seacrh Daftar Data Kelulusan",
                "Seacrh Daftar Data Siswa",
                "Kembali"]
        response = pypi.inputMenu(choices=choice, numbered= True)
        if response == choice[0]:
            Ket = pypi.inputStr(prompt='Masukkan keterangan (Lulus/Tidak Lulus): ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
            print("Daftar data yang dicari")
            for i, value in enumerate(dbDataNilai.values()):
                if Ket in value:                  
                    print (f"""
                            NIS\t\t : {value[0]}
                            Nama Siswa\t : {value[1]}
                            Nilai Akhir\t : {value[7]}
                            Keterangan\t : {value[8]}\n
                            """)
                    continue
                
                elif i == len(dbDataNilai) - 1:
                    print ("Daftar data yang dicari tidak tersedia")
                    break
                
        elif response == choice[1]:
            # menampilkan daftar data nilai siswa tertentu
            NamaSiswa = pypi.inputStr(prompt='Masukkan nama siswa: ', applyFunc=lambda x: x.title(), blockRegexes=[r'[0-9]'])
            for i, value in enumerate (dbDataNilai.values()):       
                if i == 0:              
                    continue
                if NamaSiswa in value:
                    print("Daftar data yang dicari")            
                    print (f"""
                        NIS\t\t : {value[0]}
                        Nama Siswa\t : {value[1]}
                        Nilai KKM\t : {value[2]}
                        Nilai BIndo\t : {value[3]}
                        Nilai BIng\t :  {value[4]}
                        Nilai IPA\t : {value[5]}
                        Nilai MTK\t : {value[6]}
                        Nilai Akhir\t : {value[7]}
                        Keterangan\t : {value[8]}\n
                        """)
                    break
                elif i == len(dbDataNilai) - 1:
                    print ("Daftar data yang dicari tidak tersedia")
                    CariData()
                
        elif response == choice[2]:
            MainMenu = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu utama ?(yes/no) ')
            if MainMenu == "yes":
                main()
            elif MainMenu == "no":
                CariData()    

def AddData():
    # menu menambah data daftar nilai siswa baru
    while True:
        choice =["Menampilkan Daftar Data Keseluruhan",
                 "Menambah Daftar Data Siswa", 
                 "Kembali ke Menu Utama"]
        response =pypi.inputMenu(choices=choice, numbered=True)
        if response == choice[0]:
            ShowData(dbDataNilai)
        
        elif response == choice[1]:
            while True:
                print("""
                      Petunjuk pengisian Nomor Induk Siswa (NIS)
                      Contoh:
                            NIS = 2023001
                      =======Penjelasan Contoh=======
                      Dua angka pertama tahun masuk siswa (2020) = 20
                      Dua angka berikutnya tahun lulus siswa (2023) = 23
                      Tiga angka terakhir nomor pendaftaraan siswa 001
                      """)
                indukSiswa= pypi.inputInt(prompt='Masukan NIS Siswa : ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                if indukSiswa in dbDataNilai.keys():
                    print("Nomor Induk Siswa Telah Tersedia")
                    continue
                elif len(str(indukSiswa)) < 7:
                        print("Nomor Induk Siswa harus 7 digit")
                        continue
                elif len(str(indukSiswa)) > 7:
                        print("Nomor Induk Siswa harus maksimal 7 digit")
                        continue
                else:
                    print("Masukkan Data Baru")
                    NamaSiswa = pypi.inputStr(prompt='Masukkan Nama Siswa: ', applyFunc=lambda x: x.capitalize(), blockRegexes=[r'[0-9]'])
                    NKKM = pypi.inputFloat(prompt='Masukkan Nilai KKM: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                    NBIndo = pypi.inputFloat(prompt='Masukkan Nilai Bahasa Indonesia: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                    NBIng = pypi.inputFloat(prompt='Masukkan Nilai Bahasa Inggris: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                    NIPA = pypi.inputFloat(prompt='Masukkan Nilai IPA: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                    NMTK = pypi.inputFloat(prompt='Masukkan Nilai MTK: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                    NA = (NBIndo + NBIng + NIPA + NMTK )/4
          
                    if NA >= NKKM:
                        Ket = "LULUS"
                    else:
                        Ket = "Tidak Lulus"
                    dbDataNilai.update({
                        indukSiswa: [
                            indukSiswa,
                            NamaSiswa,
                            NKKM,
                            NBIndo,
                            NBIng,
                            NIPA,
                            NMTK,
                            NA,
                            Ket
                            ]
                        }
                    )
                    ShowData(dbDataNilai)
                    break
    
        elif response == choice[2]:
            MainMenu = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu Utama ?(yes/no) ')
            if MainMenu == "yes":
                main()
            elif MainMenu == "no":
                AddData()
        
def UbahData():
    while True:
        choice = ["Menampilkan Daftar Data Keseluruhan",
                  "Edit Daftar Data Nilai Siswa", 
                  "Kembali ke Menu Utama"]
        response = pypi.inputMenu(choices=choice, numbered=True)
        if response == choice[0]:
            ShowData(dbDataNilai)
            
        elif response == choice [1]:
            while True:
                print("""
                      Petunjuk pengisian Nomor Induk Siswa (NIS)
                      Contoh:
                            NIS = 2023001
                      =======Penjelasan Contoh=======
                      Dua angka pertama tahun masuk siswa (2020) = 20
                      Dua angka berikutnya tahun lulus siswa (2023) = 23
                      Tiga angka terakhir nomor pendaftaraan siswa 001
                      """)
                indukSiswa= pypi.inputInt(prompt='Masukan NIS Siswa : ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                if len(str(indukSiswa)) < 7:
                        print("Nomor Induk Siswa harus 7 digit")
                        continue
                elif len(str(indukSiswa)) > 7:
                        print("Nomor Induk Siswa harus maksimal 7 digit")
                        continue
                elif indukSiswa not in dbDataNilai.keys():
                        print("Nomor Induk Siswa Tidak Tersedia")
                        continue
                else:
                    while True:
                        choice = ["Nilai KKM", "Nilai Bahasa Indonesia", "Nilai Bahasa Inggris", "Nilai IPA", "Nilai Matematika"]
                        response = pypi.inputMenu(choices=choice, numbered=True)
                        if response == choice[0]:
                            updateval = pypi.inputFloat(prompt='Masukkan Nilai KKM: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                        elif response == choice[1]:
                            updateval = pypi.inputFloat(prompt='Masukkan Nilai Bahasa Indonesia: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                        elif response == choice [2]:
                            updateval = pypi.inputFloat(prompt='Masukkan Nilai Bahasa Inggris: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                        elif response == choice[3]:
                            updateval = pypi.inputFloat(prompt='Masukkan Nilai IPA: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                        elif response == choice[4]:
                            updateval = pypi.inputFloat(prompt='Masukkan Nilai MTK: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
                        
                        dbDataNilai[indukSiswa][choice.index(response) + 2] = updateval
                        
                        # proses menghitung nilai
                        NBINA = dbDataNilai[indukSiswa][3]
                        NBING = dbDataNilai[indukSiswa][4]
                        NIPA = dbDataNilai[indukSiswa][5]
                        NMTK= dbDataNilai[indukSiswa][6]
                        NilaiAkhirUpdate = (NBINA + NBING + NIPA + NMTK )/4
        
                        if NilaiAkhirUpdate > dbDataNilai[indukSiswa][2]:
                            StatusUpdate = "Lulus"
                        else:
                            StatusUpdate = "Tidak Lulus"
                
                        dbDataNilai[indukSiswa][7] = NilaiAkhirUpdate
                        dbDataNilai[indukSiswa][8] = StatusUpdate
                        break
                    break
                            
        elif response == choice[2]:
            MainMenu = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu Utama ?(yes/no) ')
            if MainMenu == "yes":
                main()
            elif MainMenu == "no":
                UbahData()        
        
def delete():
    while True:
        choice = ["Menampilkan Daftar Data Keseluruhan",
                  "Hapus Daftar Data Nilai Siswa", 
                  "Kembali ke Menu Utama"]
        response =pypi.inputMenu(choices=choice, numbered=True)
        if response == choice[0]:
           ShowData(dbDataNilai)
        
        elif response == choice[1]:       
            print("""
                      Petunjuk pengisian Nomor Induk Siswa (NIS)
                      Contoh:
                            NIS = 2023001
                      =======Penjelasan Contoh=======
                      Dua angka pertama tahun masuk siswa (2020) = 20
                      Dua angka berikutnya tahun lulus siswa (2023) = 23
                      Tiga angka terakhir nomor pendaftaraan siswa 001
                      """)
            indukSiswa= pypi.inputInt(prompt='Masukkan nomor data induk siswa yang ingin dihapus: ', greaterThan=0,blockRegexes=[r'[a-zA-Z]'])
            if len(str(indukSiswa)) < 7:
                print("Nomor Induk Siswa harus 7 digit")
                continue
            elif len(str(indukSiswa)) > 7:
                print("Nomor Induk Siswa harus maksimal 7 digit")
                continue
                # Menghapus data berdasarkan nomor induk siswa
            else:     
                for i, value in enumerate (dbDataNilai.copy().values()):           
                    if indukSiswa in value:
                        print("Data nilai siswa yang akan dihapus")
                        print (f"""
                            NIS\t\t : {value[0]}
                            Nama Siswa\t : {value[1]}
                            Nilai KKM\t : {value[2]}
                            Nilai BIndo\t : {value[3]}
                            Nilai BIng\t :  {value[4]}
                            Nilai IPA\t : {value[5]}
                            Nilai MTK\t : {value[6]}
                            Nilai Akhir\t : {value[7]}
                            Keterangan\t : {value[8]}\n
                            """)
                        responsedelete = pypi.inputYesNo(prompt="Apakah anda akan tetap melanjutkan ? (yes/no) ")
                        # print(responsedelete)
                        if responsedelete == "yes":
                            del dbDataNilai[indukSiswa]
                            # print(dbDataNilai)
                            ShowData(dbDataNilai)
                            delete()
                        elif responsedelete == "no":
                            delete()
                            
                    elif i == len(dbDataNilai) - 1:
                        print("Nomor Induk Siswa Tidak Dapat Ditemukan")
                        delete()
                        break
                
        elif response == choice[2]:
            MainMenu = pypi.inputYesNo(prompt='Apakah anda ingin kembali ke menu Utama ?(yes/no) ')
            if MainMenu == "yes":
                main()
            elif MainMenu == "no":
                delete()
                
def main():
    global db
    while True:
        # Menampilkan tampilan utama program
        print(
            """
Report Data Kelulusan di SMP Maju Jaya
"""
        )
        # Input fitur yang akan dijalankan
        prompt = "Masukan angka menu yang ingin dijalankan\n"
        choice = ["Menampilkan Daftar Data Nilai Siswa", 
                  "Menambah Daftar Data Nilai Siswa", 
                  "Mengubah Daftar Data Nilai Siswa", 
                  "Menghapus Daftar Data Nilai Siswa", 
                  "Exit"]
        response = pypi.inputMenu(prompt=prompt, choices=choice, numbered=True)
        print(response)
        # Fitur menampilkan daftar nilai siswa
        if response == choice[0]:
            SubMenu()
        # Fitur menambahkan daftar nilai siswa
        elif response == choice[1]:
            AddData()
        # Fitur mengubah daftar nilai siswa
        elif response == choice[2]:
            UbahData()
        # Fitur menghapus daftar nilai siswa
        elif response == choice[3]:
            delete()
        # Fitur exit program
        else:
            keluar = pypi.inputYesNo ("Anda yakin ingin keluar? (yes/no) ")
            if keluar == "no":
                main()
                continue
            else:
                keluar == "yes"
                sys.exit()
                
    # Importing database file
        fileDataNilai = open(pathDataNilai, "w")
    # Keep database up to date
        writerDataNilai = csv.writerDataNilai(fileDataNilai, lineterminator='\n', delimiter=';')
        columns = list(dbDataNilai.values())[0] # termasuk kolom dan data
        dbDataNilai = list(dbDataNilai.values())[1:]
        writerDataNilai.writerow(columns) #db.values()
        dbDataNilai = list(dbDataNilai.values())[1:]
        for i in dbDataNilai:
            writerDataNilai.writerow(i)
            
if __name__ == "__main__":
    
    # Setting the path of database file
    pathDataNilai = r'D:\JCDS-Purwadhika\capstone_project\Modul1\DataNilai.csv'
    # Check the database contents, if empty, display a message.
    if os.path.getsize(pathDataNilai) == 0:
        print('Database is empty, please enter available Data first')
    else:
        # Importing database file
        fileDataNilai = open(pathDataNilai)
        readerDataNilai = csv.reader(fileDataNilai, delimiter=";")
        headingsDataNilai = next(readerDataNilai)
        dbDataNilai = {"column": headingsDataNilai}
        
        for row in readerDataNilai:
            dbDataNilai.update(
                {
                    int(row[0]): [
                        int(row[0]), 
                        str(row[1]), 
                        float(row[2]), 
                        float(row[3]),
                        float(row[4]),
                        float(row[5]),
                        float(row[6]),
                        float(row[7]),
                        str(row[8])
                    ]
                }
            )
        # Close the database file
        fileDataNilai.close()
        # Run main program
        main()
        1
    # Close the program
    sys.exit()
