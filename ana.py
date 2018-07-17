# -*- coding:utf-8 -*-
import siteler
import tkinter as tk
from tkinter import *


pencere=tk.Tk()
pencere.geometry('700x500')
pencere.title("Deha Pazarlama *** Pazar Yerleri ***")
img = tk.PhotoImage(file = r'C:\Users\pc\Desktop\deha\image\DP.png')
pencere.tk.call('wm', 'iconphoto', pencere._w, img)
pencere.resizable(width=FALSE, height=FALSE)





frame=Frame(pencere)
frame.pack(fill=Y,side=LEFT)



class tuslar():
    def gitt_islem():
        yazi21 = tk.Label(frame, text="GittiGidiyor \n\nİşlemler")
        yazi21.pack(fill=Y, pady=15, padx=1, side=TOP)
        dugme21 = tk.Button(frame, text='Siparişler', command=siteler.gitti.siparisler)
        dugme21.pack(fill=BOTH, pady=1, padx=1, side=TOP)
        dugme22 = tk.Button(frame, text='Gönderilenler', command=siteler.gitti.gonderilenler)
        dugme22.pack(fill=X, pady=1, padx=1, side=TOP)
        dugme23 = tk.Button(frame, text='İadeler',command=siteler.gitti.iadeler)
        dugme23.pack(fill=X, pady=1, padx=1, side=TOP)
        dugme24 = tk.Button(frame, text='Mesajlar', command=siteler.gitti.mesajlar)
        dugme24.pack(fill=BOTH, pady=1, padx=1, side=TOP)
        dugme25 = tk.Button(frame, text='Ürünler', command=siteler.gitti.urunler)
        dugme25.pack(fill=BOTH, pady=1, padx=1, side=TOP)

    def hb_islem():
        yazi21 = tk.Label(frame, text="HepsiBurada \n\nİşlemler")
        yazi21.pack(fill=Y, pady=15, padx=1, side=TOP)
        dugme21 = tk.Button(frame, text='Siparişler', command=siteler.hb.siparisler)
        dugme21.pack(fill=BOTH, pady=1, padx=1, side=TOP)
        dugme22 = tk.Button(frame, text='Gönderilenler', command=siteler.hb.gonderilenler)
        dugme22.pack(fill=X, pady=1, padx=1, side=TOP)
        dugme23 = tk.Button(frame, text='İadeler', command=siteler.hb.iadeler)
        dugme23.pack(fill=X, pady=1, padx=1, side=TOP)
        dugme24 = tk.Button(frame, text='Mesajlar', command=siteler.hb.mesajlar)
        dugme24.pack(fill=BOTH, pady=1, padx=1, side=TOP)
        dugme25 = tk.Button(frame, text='Ürünler', command=siteler.hb.urunler)
        dugme25.pack(fill=BOTH, pady=1, padx=1, side=TOP)

    def n11_1_islem():
        yazi21 = tk.Label(frame, text="n11 \n1. Mağaza \nİşlemler")
        yazi21.pack(fill=Y, pady=15, padx=1, side=TOP)
        dugme21 = tk.Button(frame, text='Siparişler', command=siteler.n11_magaza1.siparisler)
        dugme21.pack(fill=BOTH, pady=1, padx=1, side=TOP)
        dugme22 = tk.Button(frame, text='Gönderilenler', command=siteler.n11_magaza1.gonderilenler)
        dugme22.pack(fill=X, pady=1, padx=1, side=TOP)
        dugme23 = tk.Button(frame, text='İadeler', command=siteler.n11_magaza1.iadeler)
        dugme23.pack(fill=X, pady=1, padx=1, side=TOP)
        dugme24 = tk.Button(frame, text='Mesajlar', command=siteler.n11_magaza1.mesajlar)
        dugme24.pack(fill=BOTH, pady=1, padx=1, side=TOP)
        dugme25 = tk.Button(frame, text='Ürünler', command=siteler.n11_magaza1.urunler)
        dugme25.pack(fill=BOTH, pady=1, padx=1, side=TOP)

    def n11_2_islem():
        yazi21 = tk.Label(frame, text="n11 \n2. Mağaza \nİşlemler")
        yazi21.pack(fill=Y, pady=15, padx=1, side=TOP)
        dugme21 = tk.Button(frame, text='Siparişler', command=siteler.n11_magaza2.siparisler)
        dugme21.pack(fill=BOTH, pady=1, padx=1, side=TOP)
        dugme22 = tk.Button(frame, text='Gönderilenler', command=siteler.n11_magaza2.gonderilenler)
        dugme22.pack(fill=X, pady=1, padx=1, side=TOP)
        dugme23 = tk.Button(frame, text='İadeler', command=siteler.n11_magaza2.iadeler)
        dugme23.pack(fill=X, pady=1, padx=1, side=TOP)
        dugme24 = tk.Button(frame, text='Mesajlar', command=siteler.n11_magaza2.mesajlar)
        dugme24.pack(fill=BOTH, pady=1, padx=1, side=TOP)
        dugme25 = tk.Button(frame, text='Ürünler', command=siteler.n11_magaza2.urunler)
        dugme25.pack(fill=BOTH, pady=1, padx=1, side=TOP)

yazi=tk.Label(frame,text="Siteler")
yazi.pack(fill=X,pady=15,padx=1,side=TOP)
dugme11 = tk.Button(frame,text='GittiGidiyor',command=tuslar.gitt_islem)
dugme11.pack(fill=BOTH,pady=1,padx=1,side=TOP)
dugme12 = tk.Button(frame,text='N11 Magaza 1',command=tuslar.n11_1_islem)
dugme12.pack(fill=X,pady=1,padx=1,side=TOP)
dugme13 = tk.Button(frame,text='N11 Magaza 2',command=tuslar.n11_2_islem)
dugme13.pack(fill=X,pady=1,padx=1,side=TOP)
dugme14 = tk.Button(frame,text='Hepsiburada',command=tuslar.hb_islem)
dugme14.pack(fill=BOTH,pady=1,padx=1,side=TOP)

pencere.mainloop()