from tkinter import*
import sqlite3
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox

root = Tk()
root.title("Python CRUD dengan SQLite")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 900
height = 500
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

#==================================METHODS============================================
def Database():
    global conn, cursor
    conn = sqlite3.connect('responsicrud.db')
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS `member` (mem_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, nim INTEGER, nama TEXT, gender TEXT, alamat TEXT, username TEXT, password TEXT)")
    
def Buat():
    if  NIM.get() == "" or NAMA.get() == "" or GENDER.get() == "" or ALAMAT.get() == "" or USERNAME.get() == "" or PASSWORD.get() == "":
        txt_result.config(text="Harap isi data dengan lengkap!", fg="red")
    else:
        Database()
        cursor.execute("INSERT INTO `member` (nim, nama, gender, alamat, username, password) VALUES(?, ?, ?, ?, ?, ?)", (str(NIM.get()), str(NAMA.get()), str(GENDER.get()), str(ALAMAT.get()), str(USERNAME.get()), str(PASSWORD.get())))
        tree.delete(*tree.get_children())
        cursor.execute("SELECT * FROM `member` ORDER BY `nama` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        conn.commit()
        NIM.set("")
        NAMA.set("")
        GENDER.set("")
        ALAMAT.set("")
        USERNAME.set("")
        PASSWORD.set("")
        cursor.close()
        conn.close()
        txt_result.config(text="Membuat data!", fg="green")

def Baca():
    tree.delete(*tree.get_children())
    Database()
    cursor.execute("SELECT * FROM `member` ORDER BY `nama` ASC")
    fetch = cursor.fetchall()
    for data in fetch:
        tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
    cursor.close()
    conn.close()
    txt_result.config(text="Berhasil membaca data dari database", fg="black")

def Perbarui():
    Database()
    if GENDER.get() == "":
        txt_result.config(text="Pilih jenis kelamin!", fg="red")
    else:
        tree.delete(*tree.get_children())
        cursor.execute("UPDATE `member` SET `nim` = ?, `nama` = ?, `gender` =?,  `alamat` = ?,  `username` = ?, `password` = ? WHERE `mem_id` = ?", (str(NIM.get()), str(NAMA.get()), str(GENDER.get()), str(ALAMAT.get()), str(USERNAME.get()), str(PASSWORD.get()), int(mem_id)))
        conn.commit()
        cursor.execute("SELECT * FROM `member` ORDER BY `nama` ASC")
        fetch = cursor.fetchall()
        for data in fetch:
            tree.insert('', 'end', values=(data[0], data[1], data[2], data[3], data[4], data[5], data[6]))
        cursor.close()
        conn.close()
        NIM.set("")
        NAMA.set("")
        GENDER.set("")
        ALAMAT.set("")
        USERNAME.set("")
        PASSWORD.set("")
        btn_create.config(state=NORMAL)
        btn_read.config(state=NORMAL)
        btn_update.config(state=DISABLED)
        btn_delete.config(state=NORMAL)
        txt_result.config(text="Berhasil memperbarui data", fg="black")


def OnSelected(event):
    global mem_id;
    curItem = tree.focus()
    contents =(tree.item(curItem))
    selecteditem = contents['values']
    mem_id = selecteditem[0]
    NIM.set("")
    NAMA.set("")
    GENDER.set("")
    ALAMAT.set("")
    USERNAME.set("")
    PASSWORD.set("")
    NIM.set(selecteditem[1])
    NAMA.set(selecteditem[2])
    ALAMAT.set(selecteditem[4])
    USERNAME.set(selecteditem[5])
    PASSWORD.set(selecteditem[6])
    btn_create.config(state=DISABLED)
    btn_read.config(state=DISABLED)
    btn_update.config(state=NORMAL)
    btn_delete.config(state=DISABLED)

def Hapus():
    if not tree.selection():
       txt_result.config(text="Pilih item terlebih dahulu", fg="red")
    else:
        result = tkMessageBox.askquestion('Python CRUD dengan SQLite', 'Apakah Anda yakin ingin menghapus record ini?', icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents =(tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            Database()
            cursor.execute("DELETE FROM `member` WHERE `mem_id` = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
            txt_result.config(text="Berhasil menghapus data", fg="black")
            
    
def Keluar():
    result = tkMessageBox.askquestion('Python CRUD dengan SQLite', 'Anda yakin ingin keluar?', icon="warning")
    if result == 'yes':
        root.destroy()
        exit()

#==================================VARIABEL==========================================
NIM = StringVar()
NAMA = StringVar()
GENDER = StringVar()
ALAMAT = StringVar()
USERNAME = StringVar()
PASSWORD = StringVar()

#==================================BINGKAI==============================================
Top = Frame(root, width=900, height=50, bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=300, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500, bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=100, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)
RadioGroup = Frame(Forms)
Male = Radiobutton(RadioGroup, text="Pria", variable=GENDER, value="Pria", font=('arial', 16)).pack(side=LEFT)
Female = Radiobutton(RadioGroup, text="Wanita", variable=GENDER, value="Wanita", font=('arial', 16)).pack(side=LEFT)

#==================================LABEL WIDGET=======================================
txt_title = Label(Top, width=900, font=('arial', 24), text = "Python CRUD dengan SQLite")
txt_title.pack()
txt_nim = Label(Forms, text="NIM:", font=('arial', 16), bd=15)
txt_nim.grid(row=0, sticky="e")
txt_nama = Label(Forms, text="Nama:", font=('arial', 16), bd=15)
txt_nama.grid(row=1, sticky="e")
txt_gender = Label(Forms, text="Gender:", font=('arial', 16), bd=15)
txt_gender.grid(row=2, sticky="e")
txt_alamat = Label(Forms, text="Alamat:", font=('arial', 16), bd=15)
txt_alamat.grid(row=3, sticky="e")
txt_username = Label(Forms, text="Username:", font=('arial', 16), bd=15)
txt_username.grid(row=4, sticky="e")
txt_password = Label(Forms, text="Password:", font=('arial', 16), bd=15)
txt_password.grid(row=5, sticky="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

#==================================MASUKKAN WIDGET=======================================
nim = Entry(Forms, textvariable=NIM, width=30)
nim.grid(row=0, column=1)
nama = Entry(Forms, textvariable=NAMA, width=30)
nama.grid(row=1, column=1)
RadioGroup.grid(row=2, column=1)
alamat = Entry(Forms, textvariable=ALAMAT, width=30)
alamat.grid(row=3, column=1)
username = Entry(Forms, textvariable=USERNAME, width=30)
username.grid(row=4, column=1)
password = Entry(Forms, textvariable=PASSWORD, show="*", width=30)
password.grid(row=5, column=1)

#==================================TOMBOL WIDGET=====================================
btn_create = Button(Buttons, width=10, text="Buat", command=Buat)
btn_create.pack(side=LEFT)
btn_read = Button(Buttons, width=10, text="Baca", command=Baca)
btn_read.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="Perbarui", command=Perbarui, state=DISABLED)
btn_update.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="Hapus", command=Hapus)
btn_delete.pack(side=LEFT)
btn_exit = Button(Buttons, width=10, text="Keluar", command=Keluar)
btn_exit.pack(side=LEFT)

#==================================DAFTAR/LIST WIDGET========================================
scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=("MemberID", "NIM", "Nama", "Gender", "Alamat", "Username", "Password"), selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)
tree.heading('MemberID', text="MemberID", anchor=W)
tree.heading('NIM', text="NIM", anchor=W)
tree.heading('Nama', text="Nama", anchor=W)
tree.heading('Gender', text="Gender", anchor=W)
tree.heading('Alamat', text="Alamat", anchor=W)
tree.heading('Username', text="Username", anchor=W)
tree.heading('Password', text="Password", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=0)
tree.column('#2', stretch=NO, minwidth=0, width=80)
tree.column('#3', stretch=NO, minwidth=0, width=120)
tree.column('#4', stretch=NO, minwidth=0, width=80)
tree.column('#5', stretch=NO, minwidth=0, width=150)
tree.column('#6', stretch=NO, minwidth=0, width=120)
tree.column('#7', stretch=NO, minwidth=0, width=120)
tree.pack()
tree.bind('<Double-Button-1>', OnSelected)

#==================================INISIALISASI=====================================
if __name__ == '__main__':
    root.mainloop()
