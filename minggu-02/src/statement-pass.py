#Pernyataan pass tidak melakukan apa-apa. Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan. Sebagai contoh:
print("Sibuk-tunggu interupsi keyboard (Ctrl + C)")
while True:
    pass  # Busy-wait for keyboard interrupt (Ctrl+C)

#Ini biasanya digunakan untuk membuat kelas minimal:
print("biasanya digunakan untuk membuat kelas minimal (Ctrl + C)")
class MyEmptyClass:
    pass

print(":keyword: !pass diabaikan secara diam-diam:")
def initlog(*args):
    pass   # Remember to implement this!
