buah = ("apel", "jeruk", "ceri", "durian", "apel", "mangga")

#Program mengmabil tuple ke 2-5
print(buah[2:5]) 

#Manipulasi tuple buah agar item "durian" dapat dihapus
list_buah = list(buah) #2
list_buah.pop(3)
buah = tuple(list_buah)
print(buah)

#Manipulasi tuple untuk menambahkan item "manggis" diantara item "jeruk" dan "ceri"
list_buah = list(buah)
list_buah.insert(2, "manggis")
buah = tuple(list_buah)
print(buah)