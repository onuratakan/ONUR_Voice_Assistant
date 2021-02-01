#Copyright © 2020 | Site adresimiz : onurias.com | Onur Atakan ULUSOY

print("Copyright © 2020 | Site adresimiz : onurias.com | Onur Atakan ULUSOY")



print("ONUR : Sistem başlatılıyor")
print(" ")
print(" ")
print(" ")
print(" ")


import webbrowser
import cv2
import numpy as np
from gtts import gTTS
import speech_recognition as sr
import time
from playsound import playsound
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tkinter import *






yuza = 0
c = 25
ses = 50
ana_döngü = 200
language = 'tr'

seslenme = 1
bilinmiyor = 0
          
sde = gTTS(text="Sizi dinliyorum efendim", lang=language, slow=False)
sde.save("dinliyorum.mp3")

print("ONUR : Yüz tanıma modülü başlatılıyor...")
print(" ")

yüz1 = cv2.imread("yuz1.jpg",0)
yüz2 = cv2.imread("yuz2.jpg",0)
yüz3 = cv2.imread("yuz3.jpg",0)
yüz4 = cv2.imread("yuz4.jpg",0)
yüz5 = cv2.imread("yuz5.jpg",0)
yüz6 = cv2.imread("yuz6.jpg",0)
yüz7 = cv2.imread("yuz7.jpg",0)
yüz8 = cv2.imread("yuz8.jpg",0)
yüz9 = cv2.imread("yuz9.jpg",0)
yüz10 = cv2.imread("yuz10.jpg",0)

w1,h1 = yüz1.shape

kamera = cv2.VideoCapture(1)

yuzde1 = 0.8

print("ONUR : Yüz tanıma modülü başlatıldı")


print(" ")
print(" ")
print(" ")
print(" ")
print("ONUR : Sistem başlatıldı")
print(" ")
print(" ")


while ana_döngü == 200:
 yuza = 0
 c = 25
 kamera = cv2.VideoCapture(1)
 _,kare = kamera.read()
 gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
 while c == 25:
   while c == 25:
    print("1")
    res1 = cv2.matchTemplate(gri_kare,yüz1,cv2.TM_CCOEFF_NORMED)
    loc1 = np.where(res1>yuzde1)
    for n in zip(*loc1[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("2")
    res2 = cv2.matchTemplate(gri_kare,yüz2,cv2.TM_CCOEFF_NORMED)
    loc2 = np.where(res2>yuzde1)
    for n in zip(*loc2[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("3")
    res3 = cv2.matchTemplate(gri_kare,yüz3,cv2.TM_CCOEFF_NORMED)
    loc3 = np.where(res3>yuzde1)
    for n in zip(*loc3[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("4")
    _,kare = kamera.read()
    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    res4 = cv2.matchTemplate(gri_kare,yüz4,cv2.TM_CCOEFF_NORMED)
    loc4 = np.where(res4>yuzde1)
    for n in zip(*loc4[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("5")
    res5 = cv2.matchTemplate(gri_kare,yüz5,cv2.TM_CCOEFF_NORMED)
    loc5 = np.where(res5>yuzde1)
    for n in zip(*loc5[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("6")
    res6 = cv2.matchTemplate(gri_kare,yüz6,cv2.TM_CCOEFF_NORMED)
    loc6 = np.where(res6>yuzde1)
    for n in zip(*loc3[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("7")
    res7 = cv2.matchTemplate(gri_kare,yüz7,cv2.TM_CCOEFF_NORMED)
    loc7 = np.where(res7>yuzde1)
    for n in zip(*loc3[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("8") 
    res8 = cv2.matchTemplate(gri_kare,yüz8,cv2.TM_CCOEFF_NORMED)
    loc8 = np.where(res3>yuzde1)
    for n in zip(*loc8[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("9")
    res9 = cv2.matchTemplate(gri_kare,yüz9,cv2.TM_CCOEFF_NORMED)
    loc9 = np.where(res9>yuzde1)
    for n in zip(*loc9[::-1]):
       yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break
   while c == 25:
    print("10")
    res10 = cv2.matchTemplate(gri_kare,yüz10,cv2.TM_CCOEFF_NORMED)
    loc10 = np.where(res3>yuzde1)
    for n in zip(*loc10[::-1]):
        yuza = 1
    if yuza == 1:
       ses =  50
       c = 20
       break
    else:
       break







 playsound('dinliyorum.mp3')
 while ses == 50:
    


        def kbb():
        

            
            seslenme = 1
            bilinmiyor = 1
            r = sr.Recognizer()
            with sr.Microphone() as source:
              print("ONUR : Dinliyorum efendim")
              audio = r.listen(source)
              data = ""
            try:
              data = r.recognize_google(audio, language='tr-tr')
              data = data.lower()
              print(data)


            
              
            except sr.UnknownValueError:
              bilinmiyor = 0


             

              
            
                
            if 'internette ara' in data:
               bilinmiyor = 0
               print("ONUR : Efendim şimdi sadece internette aramamı istediğiniz şeyi söyleyin")
               playsound('googleara.mp3')
               r = sr.Recognizer()
               with sr.Microphone() as source:
                  audio = r.listen(source)
                  data = ""
               try:
                  data = r.recognize_google(audio, language='tr-tr')
                  data = data.lower()
                  print(data)
                  webbrowser.open('https://www.google.com/search?q=' + data)
                  playsound('interara.mp3')
                  
               except sr.UnknownValueError:
                  print("ONUR : Anlaşılamadı")
            else:
                  pass
                 




            if 'araştır' in data:
                  bilinmiyor = 0
                  print("ONUR : Efendim şimdi sadece araştırmam gereken şeyi söyleyin")
                  playsound('nara.mp3')
                  r = sr.Recognizer()
                  with sr.Microphone() as source:
                   audio = r.listen(source)
                   data = ""
                  try:
                    data = r.recognize_google(audio, language='tr-tr')
                    data = data.lower()
                    print(data)
                    driver = webdriver.Chrome()
                    driver.get('https://www.google.com/search?q=' + data)
                    araştırmasonucu = driver.find_element_by_xpath('//*[@id="rhs_block"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/span[1]').text
                    print(araştırmasonucu)
                    arastırma = gTTS(text=araştırmasonucu, lang=language, slow=False)
                    arastırma.save("arastirma.mp3")
                    playsound('arastirma.mp3')
                    
                  except sr.UnknownValueError:
                    print("ONUR : Anlaşılamadı")
            else:
                    pass


                   
            if 'facebook' in data:
              bilinmiyor = 0  
              webbrowser.open('http://facebook.com')
              print("ONUR : Facebook'u açıldı efendim")
              playsound('faefendim.mp3')
              pass
            else:
              pass






        
            if 'youtube' in data:
               bilinmiyor = 0  
               webbrowser.open('http://youtube.com')
               print("ONUR : Youtube'u açıldı efendim")
               playsound('yaefendim.mp3')
               pass
            else:
               pass



            
            if 'yabancı müzik' in data:
              bilinmiyor = 0  
              webbrowser.open('https://www.youtube.com/watch?v=JDG2m5hN1vo')
              print("ONUR : Yabancı müziği youtube üzerinden açtım efendim dört buçuk dakika şarkı molası veriyorum")
              playsound('yabancimuzik.mp3')
              time.sleep(3)
              pass
            else:
              pass


            if 'yapımcın' in data:
              bilinmiyor = 0  
              print("ONUR : Benim yapımcım Onur Atakan ULUSOY'dur")
              playsound('ykim.mp3')
              pass
            else:
              pass
      
        
            if 'nasılsın' in data:
              bilinmiyor = 0  
              print("ONUR : Daha iyi olamazdım")
              playsound('iyimisin.mp3')
              
            else:
              pass

            if 'döngüden çık' in data:
              bilinmiyor = 0  
              print("ONUR : Döngüden çıkılıyor")
              return dc()
            else:
              pass

            if 'aferin' in data:
               bilinmiyor = 0  
               print("ONUR : Teşekkürler")
               playsound('tsk.mp3')
               pass
            else:
               pass
 


            if bilinmiyor == 1 :
                print("ONUR : Henüz buna cevap veremiyorum")
                playsound('cveremiyorum.mp3')
                return kbb()
            else :
                return kbb()
                pass


        def dc():
            print("ONUR : Döngüden çıkıldı")



        def kbb2():
        

            
            
            seslenme = 1
            bilinmiyor = 1
            r = sr.Recognizer()
            with sr.Microphone() as source:
              print("ONUR : Dinliyorum efendim")
              audio = r.listen(source)
              data = ""
            try:
              data = r.recognize_google(audio, language='tr-tr')
              data = data.lower()
              print(data)


            
              
            except sr.UnknownValueError:
              bilinmiyor = 0
              print("ONUR : Efendim ne dediğinizi anlayamadım")
              playsound('eanlayamadim.mp3')

             

              
            
                
            if 'internette ara' in data:
               bilinmiyor = 0
               print("ONUR : Efendim şimdi sadece internette aramamı istediğiniz şeyi söyleyin")
               playsound('googleara.mp3')
               r = sr.Recognizer()
               with sr.Microphone() as source:
                  audio = r.listen(source)
                  data = ""
               try:
                  data = r.recognize_google(audio, language='tr-tr')
                  data = data.lower()
                  print(data)
                  webbrowser.open('https://www.google.com/search?q=' + data)
                  playsound('interara.mp3')
                  
               except sr.UnknownValueError:
                  print("ONUR : Efendim ne dediğinizi anlayamadım")
                  playsound('eanlayamadim.mp3')
            else:
                  pass
                 




            if 'araştır' in data:
                  bilinmiyor = 0
                  print("ONUR : Efendim şimdi sadece araştırmam gereken şeyi söyleyin")
                  playsound('nara.mp3')
                  r = sr.Recognizer()
                  with sr.Microphone() as source:
                   audio = r.listen(source)
                   data = ""
                  try:
                    data = r.recognize_google(audio, language='tr-tr')
                    data = data.lower()
                    print(data)
                    driver = webdriver.Chrome()
                    driver.get('https://www.google.com/search?q=' + data)
                    araştırmasonucu = driver.find_element_by_xpath('//*[@id="rhs_block"]/div/div[1]/div/div[1]/div[2]/div[2]/div/div[1]/div/div/div/div/span[1]').text
                    print(araştırmasonucu)
                    arastırma = gTTS(text=araştırmasonucu, lang=language, slow=False)
                    arastırma.save("arastirma.mp3")
                    playsound('arastirma.mp3')
                    
                  except sr.UnknownValueError:
                    print("ONUR : Efendim ne dediğinizi anlayamadım")
                    playsound('eanlayamadim.mp3')
            else:
                    pass


                   
            if 'facebook' in data:
              bilinmiyor = 0  
              webbrowser.open('http://facebook.com')
              print("ONUR : Facebook'u açıldı efendim")
              playsound('faefendim.mp3')
              pass
            else:
              pass






        
            if 'youtube' in data:
               bilinmiyor = 0  
               webbrowser.open('http://youtube.com')
               print("ONUR : Youtube'u açıldı efendim")
               playsound('yaefendim.mp3')
               pass
            else:
               pass



            
            if 'yabancı müzik' in data:
              bilinmiyor = 0  
              webbrowser.open('https://www.youtube.com/watch?v=JDG2m5hN1vo')
              print("ONUR : Yabancı müziği youtube üzerinden açtım efendim dört buçuk dakika şarkı molası veriyorum")
              playsound('yabancimuzik.mp3')
              time.sleep(3)
              pass
            else:
              pass


            if 'yapımcın' in data:
              bilinmiyor = 0  
              print("ONUR : Benim yapımcım Onur Atakan ULUSOY'dur")
              playsound('ykim.mp3')
              pass
            else:
              pass
      
        
            if 'nasılsın' in data:
              bilinmiyor = 0  
              print("ONUR : Daha iyi olamazdım")
              playsound('iyimisin.mp3')
            else:
              pass



            if 'aferin' in data:
               bilinmiyor = 0  
               print("ONUR : Teşekkürler")
               playsound('tsk.mp3')
               pass
            else:
               pass
 
            if 'söz sende' in data:
               bilinmiyor = 0  
               print("ONUR : Beni dinlediğiniz için teşekkür ederim")
               playsound('btsk.mp3')
               playsound('btsk2.mp3')
               pass
            else:
               pass

            if bilinmiyor == 1 :
                print("ONUR : Henüz buna cevap veremiyorum")
                playsound('cveremiyorum.mp3')
                
            else :
                pass



        root = Tk()
        frame = Frame(root)
        root.title('ONUR - Sesli Asistan')
        yukari_yazisi = Label(frame, text="ONUR Emrinizdedir", bg="black", fg="white")
        yukari_yazisi.pack(fill=X,pady=0)

        root.configure(background='black')

        root.geometry("360x180")
        frame.pack()

        button = Button(frame, text="Konuşma\nButonu\n(Sürekli Dinleme)\nDöngüden çıkmak\nİçin\nDöngüden çık\nDiyin", command=kbb)
        button.config( height = 10, width = 10 )
        button.pack(side=RIGHT)


        button2 = Button(frame, text="Konuşma\nButonu\n(Bas Konuş)", command=kbb2)
        button2.config( height = 10, width = 10 )
        button2.pack(side=LEFT)

        
        root.mainloop()
    




