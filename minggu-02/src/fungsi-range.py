print ("range (5) ")
for i in range(5):
    print(i)


#Titik akhir yang diberikan tidak pernah menjadi bagian dari urutan yang dihasilkan; range(10) menghasilkan 10 nilai,
print ("range (5,10) ")
for i in range(5,10):
    print(i)

#Untuk beralih pada indeks urutan, Anda dapat menggabungkan range() dan len()
print ("Gabungan Range() Len()")
a = ['Mary', 'had', 'a', 'little', 'lamb']
for i in range(len(a)):
    print(i, a[i])
