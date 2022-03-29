#This is program for management data 11 SIJA 

#import program for function_module
import function_module

data_siswa = []
    
#Looping for user options 
while True: 
    print ("Selamat Datang di Applikasi management DATA")
    print("Daftar Pilihan Data")
    print("1.Data Siswa")
    print("2.Tambah Data")
    print("3.Hapus Data")
    print("4.Cari Data")
    print("0.Keluar Applikasi")

#Creating input program for input data and access to the menu
    options = int(input("Tolong masukkan kode untuk mengakses menu: "))

#if clause statement program
    if options == 0:
        break
    elif options == 1:
        siswa = function_module.student_data(data_siswa)
        print (siswa)
    elif options == 2: 
        data_input = function_module.input_data()
        data_siswa.append(data_input)
        


print ("Program selesai. Terimakasih, selamat jumpa!")







