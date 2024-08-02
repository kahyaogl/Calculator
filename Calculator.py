#kutuphane eklendi
from tkinter import *

#yazdırma fonksiyonu oluşturuldu
def yaz(x):
    #her butona dokunuldugunda string yeniden hesaplanıp s degerine atanır
    s = len(giris.get())
    giris.insert(s,str(x))
    print(x)
 #işlem yapma fonksiyonu oluşturuldu
hesap = 5 
s1 = 0

def islemler(x):
    global hesap
    hesap = x
    global s1
    s1 = float(giris.get())
    print(hesap)
    print(s1)
    #text alanındaki yazı silindi
    giris.delete(0,'end')
    
    
    
#ikinci sayı alınarak hesaplama işlemleri gerceklestirildi    
    
s2=0
def hesapla():
    global s2
    s2 = float(giris.get())
    print(s2)
    global hesap
    sonuc=0
    if(hesap==0):
        sonuc = s1 +s2
    elif(hesap==1):
        sonuc = s1 -s2
    elif(hesap==2):
        sonuc = s1 *s2
    elif(hesap==3):
        sonuc = s1/s2
    giris.delete(0,'end')
    giris.insert(0,str(sonuc))
    

 #pencere olusturuldu
pencere = Tk() 
pencere.geometry("350x400")
 
#text alanı oluşturuludu
#justtify hizalama işlemi
giris = Entry(font="Verdana 14 bold" ,width=15,justify=RIGHT)

#ekrana yerleştirildi
giris.place(x=20,y=20)

 #butonları tutması için boş dizi oluşturuldu
b = [] 

#butonlar oluşturuldu
for i in range(1,10):
    b.append(Button(text=str(i),font="Verdana 14 bold",command=lambda x=i:yaz(x)))

sayac=0

#butonlar yerleştirildi
for i in range(0,3):
    for j in range(0,3):
        #ilk buton yerlesimi yapıldı
        b[sayac].place(x=20+j*50,y=50+i*50)
        sayac += 1
        
#işlemler olusturuldu ve yerlestiridi

#işlemleri tutmak için boş dizi olusturuldu
islem = []

#işlem butonu olusturuldu ve yerlestiridi

for i in range(0,4):
    islem.append(Button(font="Verdana 14 bold",width=2,command=lambda x=i:islemler(x)))
    
    
islem[0]['text'] = "+"
islem[1]['text'] = "-"
islem[2]['text'] = "*"
islem[3]['text'] = "/"


for i in range(0,4):
    islem[i].place(x=170,y=50+50*i)
    
#sıfır butonu oluşturuldu ve yerlestirildi
sb = Button(text="0",font="Verdana 14 bold",command=lambda x=0:yaz(x))
sb.place(x=20,y=200)

#nokta butonu oluşturuldu ve yerlestirildi
nb = Button(text=".",font="Verdan 14 bold",width=2,command=lambda x=".":yaz(x))
nb.place(x=70,y=200)

#esittir butonu olusturuldu ve yerlestirildi
eb = Button(text="=",fg="RED",font="Verdan 14 bold",width=2,command=hesapla)
eb.place(x=120,y=200)




pencere.mainloop()
