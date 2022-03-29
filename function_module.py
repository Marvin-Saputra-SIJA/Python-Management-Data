
#this module created for saving the function
from dataclasses import dataclass

#this function is used to display data from list
def student_data(data_siswa):
    for siswa in data_siswa:
       print("==========DATA SISWA 11 SIJA===========")
       print (f"Nama: {siswa['nama']}")
       print (f"Kelas: {siswa['kelas']}")
       print (f"Absen: {siswa['absen']}")
       print (f"nilai: {siswa['nilai']}")

#this function is used to input data from user 
def input_data():
    print("Input your data on down bellow!")
    name = input("Nama: ")
    kelas = input("Kelas: ")
    absen = int(input("Absen: "))
    nilai = int(input("Nilai: "))
    data_input = {
        "nama" : name,
        "kelas": kelas,
        "absen": absen, 
        "nilai": nilai
    }
    return data_input
    
       
    