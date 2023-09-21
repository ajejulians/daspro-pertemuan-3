buah = ["apel", "jeruk", "ceri", "durian", "apel", "mangga"]

#program mengambil list ke 2-5
print(buah[2:5]) #1

#Hapus item "apel" yang kedua
buah.pop(4)
print(buah) 

#Ganti item "ceri" menjadi "cherry"
buah[2] = "cherry"
print(buah) 

#Tambahkan item dengan nama "strawberry" ke dalam index ke-3
buah.insert(3, "strawberry")
print(buah) 

#Urutkan item pada list sesuai abjad
buah.sort()
print(buah) #5

