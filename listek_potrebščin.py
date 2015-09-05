from tkinter import *

import os

teden = []
mesec = []
class Aplikacija:
    def __init__(self, master):
        
        teden = []
        mesec= []
        
        self.frame = Frame()
        self.frame.grid()

        

        self.izdelek = StringVar(master)

        okence_izdelek = Label(self.frame, text = "Kupiti moram:")
        okence_izdelek.grid(row=3, column = 0, sticky = W)

        izdelek = Entry(self.frame, textvariable = self.izdelek)
        izdelek.grid(row=3, column = 1, sticky = E)

        prazna1 = Label(self.frame, text = "")
        prazna1.grid(row=2, column = 1, columnspan = 8)

        self.cena = DoubleVar(master)
        self.cena.trace("w", self.nastavi_ceno)

        okence_cena = Label(self.frame, text = "Cena v evrih:")
        okence_cena.grid(row=3, column = 2, sticky = E)

        cena = Entry(self.frame, textvariable = self.cena)
        cena.grid(row=3, column =3, sticky = E)

        prazna2 = Label(self.frame, text = "")
        prazna2.grid(row=4, column=0, columnspan = 8)

        #aplikacija ima dve okenci za vpis zneska: mesecni in tedenski budget

        self.tedenski = DoubleVar(master)
        self.tedenski.trace("w", self.doloci_budget)
        self.tedenski.trace("w", self.nastavi_denar)
        self.mesecni = DoubleVar(master)
        self.mesecni.trace("w", self.doloci_budget)
        self.mesecni.trace("w", self.nastavi_denar)


        okence_tedenski = Label(self.frame, text = "Tedenski budget:")
        okence_tedenski.grid(row = 0, column = 0, sticky = W)
        okence_mesecni = Label(self.frame, text = "Mesecni budget:")
        okence_mesecni.grid(row=1, column = 0)

        tedenski = Entry(self.frame, textvariable = self.tedenski)
        tedenski.grid(row = 0, column = 1)
        mesecni = Entry(self.frame, textvariable = self.mesecni)
        mesecni.grid(row = 1, column = 1)
        
        self.denar_teden = DoubleVar(master)
        self.denar_mesec = DoubleVar(master)
        
        okence_denar_tedenski = Label(self.frame, text = "Ta teden lahko zapravim še:")
        okence_denar_tedenski.grid(row = 0, column = 2)

        denar_tedenski = Label(self.frame, textvariable = self.denar_teden)
        denar_tedenski.grid(row = 0, column = 3)
        
        okence_denar_mesecni = Label(self.frame, text = "Ta mesec lahko zapravim še:")
        okence_denar_mesecni.grid(row=1, column = 2)

        denar_mesecni = Label(self.frame, textvariable = self.denar_mesec)
        denar_mesecni.grid(row = 1, column = 3)
        
        



        #ustvarim gumbke:

        kdaj_rabim = Label(self.frame, text = "Ta izdelek rabim:")
        kdaj_rabim.grid(row=5, column = 0, columnspan = 1)

        gumb_ta_teden = Button(self.frame, text = "Ta teden", command = self.ta_teden)
        gumb_ta_teden.grid(row = 5, column = 1, sticky = W)

        gumb_ta_mesec = Button (self.frame, text = "Ta mesec", command = self.ta_mesec)
        gumb_ta_mesec.grid(row = 5, column = 2, sticky = W)

        gumb_odstrani = Button (self.frame, text = "Že kupljeno ta teden", command = self.odstrani_teden)
        gumb_odstrani.grid(row = 6, column = 8, sticky = N + S + E)

        gumb_odstrani2 = Button (self.frame, text = "Že kupljeno ta mesec", command = self.odstrani_mesec)
        gumb_odstrani2.grid(row = 10, column = 8, sticky = N + S + E)

        #aplikacija ima dve okenci: seznam tedenskih in mesecnih potrebscin

        tedenski_listek = LabelFrame(self.frame, text ="Ta teden moram kupiti:")
        tedenski_listek.grid(row = 6, column = 0, columnspan = 6, rowspan = 3, sticky = W + E + N + S)
        tedenski_listek.columnconfigure(0, weight = 1)

        self.tedenski_listek = Listbox(tedenski_listek)
        self.tedenski_listek.grid(sticky = E + W + N + S)

        mesecni_listek = LabelFrame(self.frame, text = "Ta mesec moram kupiti:")
        mesecni_listek.grid(row = 10, column = 0, columnspan = 6, rowspan = 3, sticky = N + W + E + S)
        mesecni_listek.columnconfigure(0, weight = 1)

        self.mesecni_listek = Listbox(mesecni_listek)
        self.mesecni_listek.grid(sticky = E + W + N + S)

        menu = Menu(master)
        master.config(menu=menu)
        file_menu= Menu(menu)
        menu.add_cascade(label = "File", menu=file_menu)

        file_menu.add_command(label = "Odpri", command = self.odpri)
        file_menu.add_command(label = "Shrani", command = self.shrani)
        

        




    def doloci_budget(self, name, index, mode):
        try:
            self.tedenski.set(self.tedenski.get())
            self.mesecni.set(self.mesecni.get())
        except ValueError:
            return None

    def nastavi_denar(self, name, index, mode):
        try:
            self.denar_teden.set(self.tedenski.get())
            self.denar_mesec.set(self.mesecni.get())
        except ValueError:
            return None
            

    def nastavi_ceno(self, name, index, mode):
        try:
            self.cena.set(self.cena.get())
        except ValueError:
            return None
    



    def ta_teden(self):
        
        if self.izdelek.get() == "":
            return None
        izdelek = self.izdelek.get()
        cena = self.cena.get()

        if self.izdelek.get() == "svet":
            toplevel = Toplevel()
            okence = Label(toplevel, text = "Sveta pa že ne moreš kupiti!", height = 5, width = 50, bg ="light blue")
            okence.pack()
        
        elif (self.denar_teden.get() - self.cena.get()) >=0 and (self.denar_mesec.get() - self.cena.get()) >=0:
            self.denar_teden.set(self.denar_teden.get() - self.cena.get())
            self.denar_mesec.set(self.denar_mesec.get() - self.cena.get())
            self.tedenski_listek.insert(END, izdelek)
        
            

        else:
            toplevel = Toplevel()
            okence = Label(toplevel, text = "Cena tega izdelka presega znesek, ki ga imate na voljo. Izberite drug izdelek. ", height = 5,
                           width = 75, bg="light coral" )
            okence.pack()

        

    def ta_mesec(self):
        
        if self.izdelek.get() == "":
            return None
        izdelek = self.izdelek.get()
        cena = self.cena.get()

        if self.izdelek.get() == "svet":
            toplevel = Toplevel()
            okence = Label(toplevel, text = "Sveta pa že ne moreš kupiti!", height = 5, width = 50, bg ="light blue")
            okence.pack()
        
        
        elif (self.denar_mesec.get() - self.cena.get()) >=0:
            self.denar_mesec.set(self.denar_mesec.get() - self.cena.get())
            self.mesecni_listek.insert(END, izdelek)
            
        else:
            toplevel = Toplevel()
            okence = Label(toplevel, text = "Cena tega izdelka presega znesek, ki ga imate na voljo. Izberite drug izdelek. ", height = 5,
                           width = 75, bg="light coral" )
            okence.pack()


    def odstrani_teden(self):
        izbira = self.tedenski_listek.curselection()
        self.tedenski_listek.delete(izbira[0])

    def odstrani_mesec(self):
        izbira = self.mesecni_listek.curselection()
        self.mesecni_listek.delete(izbira[0])

    def shrani(self):
        ime = filedialog.asksaveasfilename()
        
        f = open(ime, "wt", encoding = "utf8")
        f.write(str(self.tedenski.get()))
        f.write("\n")
        f.write(str(self.mesecni.get()))
        f.write("\n")
        f.write(str(self.denar_teden.get()))
        f.write("\n")
        f.write(str(self.denar_mesec.get()))

        f.write("\n")


        temp_list = list(self.tedenski_listek.get(0,END))
        if len(temp_list) == 0:
            f.write("\n")
        else:
            temp_list = [i + "\n" for i in temp_list]
            f.writelines(temp_list)

        f.write("svet")
        f.write("\n")
        
        temp_list_2 = list(self.mesecni_listek.get(0,END))
        if len(temp_list_2) == 0:
            f.write("\n")
        else:
            temp_list_2 = [i + "\n" for i in temp_list_2]
            f.writelines(temp_list_2)

        f.close()

    def odpri(self):
        ime = filedialog.askopenfilename()
        f = open(ime, "r", encoding = "utf8")
        vrstice = f.readlines()
        self.tedenski.set(float(vrstice[0]))
        self.mesecni.set(float(vrstice[1]))
        self.denar_teden.set(float(vrstice[2]))
        self.denar_mesec.set(float(vrstice[3]))

        zgornja_meja = int(vrstice.index("svet\n"))

        for i in range(4, zgornja_meja):
            self.tedenski_listek.insert(END, vrstice[i])
        for i in range(zgornja_meja + 1, int(len(vrstice))):
            self.mesecni_listek.insert(END, vrstice[i])

        f.close()
        

root = Tk()
aplikacija = Aplikacija(root)
root.mainloop()
