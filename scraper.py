import os
os.system("cls")   # Windows
from bs4 import BeautifulSoup
import requests
import pandas as pd
liste = []
a= 0

for sayfa in range (1,50):


    response = requests.get(f"https://www.emlakjet.com/kiralik-konut/antalya?sayfa={sayfa}")
    soup = BeautifulSoup(response.content,"lxml")
    # print(soup)
    k1 = soup.find("div",class_="styles_wrapper__K8w6q")
    # print(len(k1))
    k2 = k1.find_all("div",class_="styles_listingWrapper__gVjYi")
    # print(len(k2))
    b = 0  
    for i1 in k2 :
        ara = i1.find("a",class_="styles_wrapper__587DT")
        ara_linkler = ara.get("href")
        bilgiler = ara.find("div",class_="styles_contentWrapper___jenb")
        ilan_ismi = bilgiler.find("div",class_="styles_titleWrapper__mwToX").text
        konum_ismi = bilgiler.find("div",class_="styles_locationWrapper__ZbFif").text
        daire_özellik = bilgiler.find("div",class_="styles_quickinfoWrapper__Vsnk5").text
        fiyat = bilgiler.find("div",class_="styles_priceContent__AtYE7").text
        # print(f"1 : {ilan_ismi}\n")
        # print(f"2 : {konum_ismi}\n")
        # print(f"3 : {daire_özellik}\n")
        # print(f"4 : {fiyat}\n ")
        yeni_ilan = "https://www.emlakjet.com" + ara_linkler
        
        response1 = requests.get(yeni_ilan)
        # print(response1)
        soup1 = BeautifulSoup(response1.content,"lxml")


        l1 = soup1.find("div",class_="styles_inner__qKPCB")
        l2 = l1.find_all("span",class_="styles_value__xmNV3")
        if l2[1]:
            l2[1].text
        else :
            print("none")

        if l2[8]:
            l2[8].text
        else :
            print("none")
        
        if l2[9]:
            l2[9].text
        else :
            print("none")
        
        if l2[10]:
            l2[10].text
        else :
            print("none")


        basliklar = soup1.find_all("span", class_="styles_infoTitle__uBgQ2")
        degerler = soup1.find_all("p", class_="styles_infoDescription__cXpIW")
        ort_kira = degerler[0].text.strip() if len(degerler) > 0 else ""
        ort_satis = degerler[1].text.strip() if len(degerler) > 1 else ""

            
        liste_img = []    

        resimler = soup1.find_all("img")
        del resimler[3]
        # print("Toplam img sayisi:", len(resimler))
        
        for im in resimler:
            im.get("src")
            im1 = im.get("src")
            liste_img.append(im1)


        liste.append([ilan_ismi,konum_ismi,daire_özellik,fiyat,l2[1].text,l2[8].text,l2[9].text,l2[10].text,ort_kira,ort_satis,[liste_img]])
        b = b + 1
        print(b) 
    a = a + 1
    print(f"--------------------------------------------{a}\n")
    
df = pd.DataFrame(liste)
df.columns = ["İsim","Konum","Özellik","Fiyat","Yayinlanma_Tarihi","Kat_sayisi","Bulundugu_kat","Bina_yasi","Ort_kira","Ort_satis","Görseller"]
print(df)
df.to_excel("listing.xlsx",index=False)