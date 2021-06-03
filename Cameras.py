#gerekli sınıfların tanımlanması
import numpy as np
import cv2 as cv
import face_recognition

class CreateCamera:
    face_classifier = ""
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    def TakePhoto(self,image):
        cv.imwrite('images/visitor.jpg',image)
        print("Resim çekme işlemi başarılı.")

    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")

            #Ziyaretçiye ait verinin alındığı kısım
            if(cv.waitKey(1)==ord('t')):
                if(len(faces_rects)==1):
                    self.TakePhoto(gray)
                else:
                    print("Lütfen resim çekerken ekranda tek bir yüz bulunsun.")

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                break
        #kameranın kapatıldığı kısım
        cap.release()
        cv.destroyAllWindows()

class CameraA:
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        print("Kamera A Aktifleştiriliyor.!")
        
    def TakePhoto(self,image):
        cv.imwrite('images/visitor.jpg',image)
        print("Resim çekme işlemi başarılı.")

    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        read_face = False
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")

            #Ziyaretçiye ait verinin alındığı kısım
            if(cv.waitKey(1)==ord('t')):
                if(len(faces_rects)==1):
                    self.TakePhoto(gray)
                    read_face = True
                else:
                    print("Lütfen resim çekerken ekranda tek bir yüz bulunsun.")

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                break
        #kameranın kapatıldığı kısım
        cap.release()
        cv.destroyAllWindows()
        return read_face

class CameraB:
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        print("Kamera B Aktifleştiriliyor.!")
        
    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")
            if(len(faces_rects)==1):
                #Ziyaretçi Görüldü mü?
                #ziyaretçinin kayıt edilen resminin kodlanması
                picture_of_visitor = face_recognition.load_image_file("images/visitor.jpg")
                visitor_encoding = face_recognition.face_encodings(picture_of_visitor)[0]

                #geçici resmin kayıt edilmesi
                cv.imwrite('images/temp.jpg',gray)

                #ziyaretçinin kamerada aranan resminin kodlanması
                unknown = face_recognition.load_image_file("images/temp.jpg")
                unknown_encoding = face_recognition.face_encodings(unknown)[0]

                results = face_recognition.compare_faces([visitor_encoding], unknown_encoding)

                if(results[0]==True):
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False

class CameraC:
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        print("Kamera C Aktifleştiriliyor.!")
        
    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")
            if(len(faces_rects)==1):
                #Ziyaretçi Görüldü mü?
                #ziyaretçinin kayıt edilen resminin kodlanması
                picture_of_visitor = face_recognition.load_image_file("images/visitor.jpg")
                visitor_encoding = face_recognition.face_encodings(picture_of_visitor)[0]

                #geçici resmin kayıt edilmesi
                cv.imwrite('images/temp.jpg',gray)

                #ziyaretçinin kamerada aranan resminin kodlanması
                unknown = face_recognition.load_image_file("images/temp.jpg")
                unknown_encoding = face_recognition.face_encodings(unknown)[0]

                results = face_recognition.compare_faces([visitor_encoding], unknown_encoding)

                if(results[0]==True):
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False
class CameraD:
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        print("Kamera D Aktifleştiriliyor.!")
        
    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")
            if(len(faces_rects)==1):
                #Ziyaretçi Görüldü mü?
                #ziyaretçinin kayıt edilen resminin kodlanması
                picture_of_visitor = face_recognition.load_image_file("images/visitor.jpg")
                visitor_encoding = face_recognition.face_encodings(picture_of_visitor)[0]

                #geçici resmin kayıt edilmesi
                cv.imwrite('images/temp.jpg',gray)

                #ziyaretçinin kamerada aranan resminin kodlanması
                unknown = face_recognition.load_image_file("images/temp.jpg")
                unknown_encoding = face_recognition.face_encodings(unknown)[0]

                results = face_recognition.compare_faces([visitor_encoding], unknown_encoding)

                if(results[0]==True):
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False
class CameraE:
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        print("Kamera E Aktifleştiriliyor.!")
        
    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")
            if(len(faces_rects)==1):
                #Ziyaretçi Görüldü mü?
                #ziyaretçinin kayıt edilen resminin kodlanması
                picture_of_visitor = face_recognition.load_image_file("images/visitor.jpg")
                visitor_encoding = face_recognition.face_encodings(picture_of_visitor)[0]

                #geçici resmin kayıt edilmesi
                cv.imwrite('images/temp.jpg',gray)

                #ziyaretçinin kamerada aranan resminin kodlanması
                unknown = face_recognition.load_image_file("images/temp.jpg")
                unknown_encoding = face_recognition.face_encodings(unknown)[0]

                results = face_recognition.compare_faces([visitor_encoding], unknown_encoding)

                if(results[0]==True):
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False
class CameraF:
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        print("Kamera F Aktifleştiriliyor.!")
        
    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")
            if(len(faces_rects)==1):
                #Ziyaretçi Görüldü mü?
                #ziyaretçinin kayıt edilen resminin kodlanması
                picture_of_visitor = face_recognition.load_image_file("images/visitor.jpg")
                visitor_encoding = face_recognition.face_encodings(picture_of_visitor)[0]

                #geçici resmin kayıt edilmesi
                cv.imwrite('images/temp.jpg',gray)

                #ziyaretçinin kamerada aranan resminin kodlanması
                unknown = face_recognition.load_image_file("images/temp.jpg")
                unknown_encoding = face_recognition.face_encodings(unknown)[0]

                results = face_recognition.compare_faces([visitor_encoding], unknown_encoding)

                if(results[0]==True):
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False
class CameraG:
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        print("Kamera G Aktifleştiriliyor.!")
        
    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")
            if(len(faces_rects)==1):
                #Ziyaretçi Görüldü mü?
                #ziyaretçinin kayıt edilen resminin kodlanması
                picture_of_visitor = face_recognition.load_image_file("images/visitor.jpg")
                visitor_encoding = face_recognition.face_encodings(picture_of_visitor)[0]

                #geçici resmin kayıt edilmesi
                cv.imwrite('images/temp.jpg',gray)

                #ziyaretçinin kamerada aranan resminin kodlanması
                unknown = face_recognition.load_image_file("images/temp.jpg")
                unknown_encoding = face_recognition.face_encodings(unknown)[0]

                results = face_recognition.compare_faces([visitor_encoding], unknown_encoding)

                if(results[0]==True):
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False
class CameraH:
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')
        print("Kamera H Aktifleştiriliyor.!")
        
    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Kameraya erişilemedi.!")
            exit()
        while True:
            #kameraya istek gönderilir
            ret, frame = cap.read()
            #kamera açılabildi mi
            if not ret:
                print("Kameradan düzgün veri alınamadı çıkış yapılıyor.!")
                break
            
            #görüntünün gri hali elde edilir
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            #algılanan yüz sayısı
            print(str(len(faces_rects))+" Adet yüz algılandı.")
            if(len(faces_rects)==1):
                #Ziyaretçi Görüldü mü?
                #ziyaretçinin kayıt edilen resminin kodlanması
                picture_of_visitor = face_recognition.load_image_file("images/visitor.jpg")
                visitor_encoding = face_recognition.face_encodings(picture_of_visitor)[0]

                #geçici resmin kayıt edilmesi
                cv.imwrite('images/temp.jpg',gray)

                #ziyaretçinin kamerada aranan resminin kodlanması
                unknown = face_recognition.load_image_file("images/temp.jpg")
                unknown_encoding = face_recognition.face_encodings(unknown)[0]

                results = face_recognition.compare_faces([visitor_encoding], unknown_encoding)

                if(results[0]==True):
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False
