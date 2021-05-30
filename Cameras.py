#gerekli sınıfların tanımlanması
import numpy as np
import cv2 as cv

class CreateCamera:
    face_classifier = ""
    def __init__(self):
        self.face_classifier = cv.CascadeClassifier('data/haarcascade_frontalface_default.xml')

    #Kamerada istenilen yüzü arayan fonksiyondur
    def ReadFace(self):
        cap = cv.VideoCapture(0)
        if not cap.isOpened():
            print("Cannot open camera")
            exit()
        while True:
            # Capture frame-by-frame
            ret, frame = cap.read()
            # if frame is read correctly ret is True
            if not ret:
                print("Can't receive frame (stream end?). Exiting ...")
                break
            # Our operations on the frame come here
            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            faces_rects = self.face_classifier.detectMultiScale(gray, scaleFactor = 1.2, minNeighbors = 5)
            print(faces_rects)
            # Display the resulting frame
            cv.imshow('frame', gray)
            if cv.waitKey(1) == ord('q'):
                break
        # When everything done, release the capture
        cap.release()
        cv.destroyAllWindows()

class CameraA:
    def __init__(self):
        pass
        
    def ReadFace(self, human_face):
        pass

    def RecFace(self):
        pass

class CameraB:
    def __init__(self):
        pass
        
    def ReadFace(self, human_face):
        pass

class CameraC:
    def __init__(self):
        pass
        
    def ReadFace(self, human_face):
        pass

class CameraD:
    def __init__(self):
        pass
        
    def ReadFace(self, human_face):
        pass

class CameraE:
    def __init__(self):
        pass
        
    def ReadFace(self, human_face):
        pass

class CameraF:
    def __init__(self):
        pass
        
    def ReadFace(self, human_face):
        pass

class CameraG:
    def __init__(self):
        pass
        
    def ReadFace(self, human_face):
        pass

class CameraH:
    def __init__(self):
        pass
        
    def ReadFace(self, human_face):
        pass



