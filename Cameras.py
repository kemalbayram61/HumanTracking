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
            #print(str(len(faces_rects))+" Adet yüz algılandı.")

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
            #print(str(len(faces_rects))+" Adet yüz algılandı.")

            #Ziyaretçiye ait verinin alındığı kısım
            if(cv.waitKey(1)==ord('t')):
                if(len(faces_rects)==1):
                    self.TakePhoto(gray)
                    read_face = True
                else:
                    print("Lütfen resim çekerken ekranda tek bir yüz bulunsun.")

            #video ekranından çıkma işlemi
            #self.show_element.setStyleSheet("background-image : url(image.png); border : 2px solid blue")
            cv.imshow("frame",gray)

            if cv.waitKey(1) == ord('q'):
                break
        #kameranın kapatıldığı kısım
        cap.release()
        cv.destroyAllWindows()
        return read_face

    def GetName(self):
        return "Camera A"

class CameraB:
    def __init__(self,camera_label):
        self.camera_labes = camera_label
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
            #print(str(len(faces_rects))+" Adet yüz algılandı.")
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
                    img = cv.imread('images/temp.jpg', cv.IMREAD_UNCHANGED)
                    scale_percent = 30 # percent of original size
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    
                    # resize image
                    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
                    cv.imwrite("images/visitor_temp_b.jpg",resized)

                    self.camera_labes.setStyleSheet("background-image : url(images/visitor_temp_b.jpg); border : 2px solid blue")
                    self.camera_labes.setText("")
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False
    def GetName(self):
        return "Camera B"


class CameraC:
    def __init__(self,camera_label):
        self.camera_labes = camera_label
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
            #print(str(len(faces_rects))+" Adet yüz algılandı.")
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
                    img = cv.imread('images/temp.jpg', cv.IMREAD_UNCHANGED)
                    scale_percent = 30 # percent of original size
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    
                    # resize image
                    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
                    cv.imwrite("images/visitor_temp_c.jpg",resized)

                    self.camera_labes.setStyleSheet("background-image : url(images/visitor_temp_c.jpg); border : 2px solid blue")
                    self.camera_labes.setText("")
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False

    def GetName(self):
        return "Camera C"

class CameraD:
    def __init__(self,camera_label):
        self.camera_labes = camera_label
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
            #print(str(len(faces_rects))+" Adet yüz algılandı.")
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
                    img = cv.imread('images/temp.jpg', cv.IMREAD_UNCHANGED)
                    scale_percent = 30 # percent of original size
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    
                    # resize image
                    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
                    cv.imwrite("images/visitor_temp_d.jpg",resized)

                    self.camera_labes.setStyleSheet("background-image : url(images/visitor_temp_d.jpg); border : 2px solid blue")
                    self.camera_labes.setText("")
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False

    def GetName(self):
        return "Camera D"

class CameraE:
    def __init__(self,camera_label):
        self.camera_labes = camera_label
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
            #print(str(len(faces_rects))+" Adet yüz algılandı.")
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
                    img = cv.imread('images/temp.jpg', cv.IMREAD_UNCHANGED)
                    scale_percent = 30 # percent of original size
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    
                    # resize image
                    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
                    cv.imwrite("images/visitor_temp_e.jpg",resized)

                    self.camera_labes.setStyleSheet("background-image : url(images/visitor_temp_e.jpg); border : 2px solid blue")
                    self.camera_labes.setText("")
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False

    def GetName(self):
        return "Camera E"

class CameraF:
    def __init__(self,camera_label):
        self.camera_labes = camera_label
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
            #print(str(len(faces_rects))+" Adet yüz algılandı.")
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
                    img = cv.imread('images/temp.jpg', cv.IMREAD_UNCHANGED)
                    scale_percent = 30 # percent of original size
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    
                    # resize image
                    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
                    cv.imwrite("images/visitor_temp_f.jpg",resized)

                    self.camera_labes.setStyleSheet("background-image : url(images/visitor_temp_f.jpg); border : 2px solid blue")
                    self.camera_labes.setText("")
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False

    def GetName(self):
        return "Camera F"

class CameraG:
    def __init__(self,camera_label):
        self.camera_labes = camera_label
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
            #print(str(len(faces_rects))+" Adet yüz algılandı.")
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
                    img = cv.imread('images/temp.jpg', cv.IMREAD_UNCHANGED)
                    scale_percent = 30 # percent of original size
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    
                    # resize image
                    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
                    cv.imwrite("images/visitor_temp_g.jpg",resized)

                    self.camera_labes.setStyleSheet("background-image : url(images/visitor_temp_g.jpg); border : 2px solid blue")
                    self.camera_labes.setText("")
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False

    def GetName(self):
        return "Camera G"

class CameraH:
    def __init__(self,camera_label):
        self.camera_labes = camera_label
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
            ##print(str(len(faces_rects))+" Adet yüz algılandı.")
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
                    img = cv.imread('images/temp.jpg', cv.IMREAD_UNCHANGED)
                    scale_percent = 30 # percent of original size
                    width = int(img.shape[1] * scale_percent / 100)
                    height = int(img.shape[0] * scale_percent / 100)
                    dim = (width, height)
                    
                    # resize image
                    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
                    cv.imwrite("images/visitor_temp_h.jpg",resized)

                    self.camera_labes.setStyleSheet("background-image : url(images/visitor_temp_h.jpg); border : 2px solid blue")
                    self.camera_labes.setText("")
                    cap.release()
                    cv.destroyAllWindows()
                    return True

            #video ekranından çıkma işlemi
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                cap.release()
                cv.destroyAllWindows()
                return False
    def GetName(self):
        return "Camera H"