

import cv2
import numpy as np
import time

kamera = cv2.VideoCapture(1)
print("Sırasıyla 1,2,3,4,5,6,7,8,9 ve o tuşlarına basılı tutarak resminizi küçük çerçeveli kısmın içine yerleştirin q  tuşuna basılı tutarak çıkabilirsiniz ONUR ATAKAN ULUSOY")


while True:
    ret,kare = kamera.read()
    
    gri_kare = cv2.cvtColor(kare,cv2.COLOR_BGR2GRAY)
    kayıt_kare = kare[150:300,238:373]
    cv2.imshow("Kayıt",kayıt_kare)
    cv2.imshow("Onur Atakan ULUSOY",kare)

    
    
        
        
    if cv2.waitKey(25) & 0xFF == ord('1'):
            cv2.imwrite('yuz1.jpg',kayıt_kare)     
    if cv2.waitKey(25) & 0xFF == ord('2'):
            cv2.imwrite('yuz2.jpg',kayıt_kare)
    if cv2.waitKey(25) & 0xFF == ord('3'):
            cv2.imwrite('yuz3.jpg',kayıt_kare)
    if cv2.waitKey(25) & 0xFF == ord('4'):
            cv2.imwrite('yuz4.jpg',kayıt_kare)     
    if cv2.waitKey(25) & 0xFF == ord('5'):
            cv2.imwrite('yuz5.jpg',kayıt_kare)
    if cv2.waitKey(25) & 0xFF == ord('6'):
            cv2.imwrite('yuz6.jpg',kayıt_kare)
    if cv2.waitKey(25) & 0xFF == ord('7'):
            cv2.imwrite('yuz7.jpg',kayıt_kare)   
    if cv2.waitKey(25) & 0xFF == ord('8'):
            cv2.imwrite('yuz8.jpg',kayıt_kare)
    if cv2.waitKey(25) & 0xFF == ord('9'):
            cv2.imwrite('yuz9.jpg',kayıt_kare)
    if cv2.waitKey(25) & 0xFF == ord('o'):
            cv2.imwrite('yuz10.jpg',kayıt_kare)          


            
    if cv2.waitKey(25) & 0xFF == ord('q'):
            break

        
kamera.release()
cv2.destroyAllWindows()
