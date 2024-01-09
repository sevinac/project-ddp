from tkinter import *
from tkinter import messagebox

def cekTotal():
    try:
        harga = int(inpHarga.get())
        jumlah_barang = int(inpJumlahBarang.get())
        member = list(members.keys())[grupMember.get()]

        diskon = 0
        if member == "Silver":
            diskon = 10
        elif member == "Gold":
            diskon = 25
        elif member == "Platinum":
            diskon = 50
        elif member == "Diamond":
            diskon = 75

        total_harga = harga * jumlah_barang * (1 - diskon / 100)
        messagebox.showinfo("Data Form", f"Member: {member}, Harga Total (setelah diskon): {total_harga}")
    except ValueError:
        messagebox.showerror("Error", "Masukkan harga dan jumlah barang dengan benar")

root = Tk()
root.title("PROGRAM KASIR SEDERHANA")
root.geometry("600x400")

lblHarga = Label(root, text="Input harga barang: ")
lblHarga.grid(column=0, row=0)
inpHarga = Entry(root, width=25)
inpHarga.grid(column=1, row=0)

lblJumlahBarang = Label(root, text="Input jumlah barang: ")
lblJumlahBarang.grid(column=0, row=1)
inpJumlahBarang = Entry(root, width=25)
inpJumlahBarang.grid(column=1, row=1)

members = {"None": 0, "Silver": 1, "Gold": 2, "Platinum": 3, "Diamond": 4}

lblMember = Label(root, text="Pilih jenis member: ")
lblMember.grid(column=0, row=3, pady=5)
grupMember = IntVar()
rowRadio = 3
for key, val in members.items():
    Radiobutton(root, text=key, variable=grupMember, value=val).grid(column=1, row=rowRadio, sticky=W)
    rowRadio += 1
grupMember.set(0)

btn = Button(root, text="Hitung", background="green", foreground="white", width=15, command=cekTotal)
btn.grid(column=0, pady=5)

root.mainloop()