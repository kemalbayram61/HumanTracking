import json
from os import nice
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
from design_python import Ui_MainWindow
from JsonOperation import JsonOperation
from Humans import User, Visitor
from HumanWalk import HumanWalk
from Init import Init
import Cameras
import cv2
import sys
from datetime import datetime

class Design(QMainWindow):
   def __init__(self):
      self.read_face = False
      super().__init__()
      self.ui =Ui_MainWindow()
      self.ui.setupUi(self)
      self.ui.btn_giris.clicked.connect(self.buttonClick)
      self.ui.btn_girisekrani.clicked.connect(self.buttonClick)
      self.ui.btn_calisanlar.clicked.connect(self.buttonClick)
      self.ui.btn_gonder.clicked.connect(self.buttonClick)
      self.ui.btn_raporlar.clicked.connect(self.buttonClick)
      self.ui.btn_ziyaretci.clicked.connect(self.buttonClick)
      self.ui.btn_exit.clicked.connect(self.buttonClick)
      self.ui.btn_guncelle.clicked.connect(self.buttonClick)
      self.ui.btn_resimcek.clicked.connect(self.buttonClick)
      self.init = Init()
      self.human_walk = HumanWalk()
      self.report_text = ""

      #fonksiyonel sınıfların tanımlanması
      self.json_operation = JsonOperation()
      self.user = User()

   def ChangeCameras(self):
      cameras = self.user.user_cameras.split(",")
      for camera in cameras:
         if(camera=="A"):
            self.ui.lbl_kameraA.show()
         elif(camera=="B"):
            self.ui.lbl_kameraB.show()
         elif(camera=="C"):
            self.ui.lbl_kameraC.show()
         elif(camera=="D"):
            self.ui.lbl_kameraD.show()
         elif(camera=="E"):
            self.ui.lbl_kameraE.show()
         elif(camera=="F"):
            self.ui.lbl_kameraF.show()
         elif(camera=="G"):
            self.ui.lbl_kameraG.show()
         elif(camera=="H"):
            self.ui.lbl_kameraH.show()



   def CheckUser(self):
      json_user = self.json_operation.GetUser(self.ui.txt_kullaniciadi.text(),self.ui.txt_sifre.text())
      
      if(json_user!=False):
         self.user.Setuser(json_user)
         self.ui.btn_ziyaretci.setEnabled(True)
         if(self.user.user_authority=="1"):
            self.ui.btn_calisanlar.setEnabled(True)
         self.ui.btn_raporlar.setEnabled(True)
         self.ui.btn_giris.setEnabled(False)
         self.ui.btn_giris.setText("Giriş başarılı...")
         now = datetime.now()
         current_time = now.strftime("%H:%M:%S")
         self.report_text = self.report_text + "\n" + self.user.user_name + " başarı ile giriş yaptı." + current_time
         self.ChangeCameras()
      else:
         now = datetime.now()
         current_time = now.strftime("%H:%M:%S")
         self.report_text = self.report_text + "\n Hatalı giriş denemesi yapıldı." + current_time
      self.ui.txt_rapor.setText(self.report_text)

   def UpdateUserCameras(self):
      json_user = self.json_operation.GetUserForC(self.ui.txt_kullaniciadi_calisan.text())
      change_user = User()
      change_user.Setuser(json_user)
      if(len(change_user.user_name)>0):
         self.json_operation.ChangeCameras(change_user.user_id,self.ui.txt_atanacak.text())
         self.ui.btn_guncelle.setEnabled(False)
         self.ui.btn_guncelle.setText("Güncelleme başarılı...")
      else:
         print("Güncellenecek kullanıcı bulunamadı.")

   def buttonClick(self):
      # GET BUTTON CLICKED
      btn = self.sender()
      btnName = btn.objectName()
      print(btnName)


      # user login
      if btnName == "btn_resimcek":
         now = datetime.now()
         current_time = now.strftime("%H:%M:%S")
         self.report_text = self.report_text + "\n Resim çekme isteğinde bulunuldu." + current_time
         self.ui.txt_rapor.setText(self.report_text)
         main_camera = Cameras.CameraA()
         self.read_face = main_camera.ReadFace()
         
         if(self.read_face):
            img = cv2.imread('images/visitor.jpg', cv2.IMREAD_UNCHANGED)

            scale_percent = 40 # percent of original size
            width = int(img.shape[1] * scale_percent / 100)
            height = int(img.shape[0] * scale_percent / 100)
            dim = (width, height)
            
            # resize image
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite("images/visitor_temp.jpg",resized)

            self.ui.ziyareci_kamera.setStyleSheet("background-image : url(images/visitor_temp.jpg); border : 2px solid blue")
            self.ui.ziyareci_kamera.setText("")

      # user login
      if btnName == "btn_giris":
         self.CheckUser()

      # update camera
      if btnName == "btn_guncelle":
         self.UpdateUserCameras()
         now = datetime.now()
         current_time = now.strftime("%H:%M:%S")
         self.report_text = self.report_text + "\n Kullanıcı güncelleme işlemi yapıldı." +current_time
         self.ui.txt_rapor.setText(self.report_text)

      # SHOW HOME PAGE
      if btnName == "btn_girisekrani":
         self.ui.stackedWidget.setCurrentWidget(self.ui.giris_sayfasi)
         
      # SHOW CALISANLAR PAGE
      if btnName == "btn_calisanlar":
         self.ui.stackedWidget.setCurrentWidget(self.ui.calisanlar_sayfasi)

       # SHOW HOME PAGE
      if btnName == "btn_ziyaretci":         
         self.ui.stackedWidget.setCurrentWidget(self.ui.ziyaretci_sayfasi)

      # SHOW self.ui PAGE
      if btnName == "btn_gonder":
         if(self.read_face):
            road = ""
            is_start = False
            target_name = self.ui.cmb_adres.currentText()
            if(target_name == "ahmet"):
               is_start=True
               camera_labesl = [self.ui.lbl_kameraB,self.ui.lbl_kameraE,self.ui.lbl_kameraF]
               road = self.init.Road1(camera_labesl)

            elif(target_name=="mehmet"):
               camera_labesl = [self.ui.lbl_kameraB,self.ui.lbl_kameraC,self.ui.lbl_kameraG,self.ui.lbl_kameraH]
               road = self.init.Road2(camera_labesl)
               is_start = True
            elif(target_name=="hasan"):
               camera_labesl = [self.ui.lbl_kameraB,self.ui.lbl_kameraC,self.ui.lbl_kameraD]
               road = self.init.Road3(camera_labesl)
               is_start = True
            else:
               print("Gerekli bilgiler girilmedi.")
            if(is_start):
               now = datetime.now()
               current_time = now.strftime("%H:%M:%S")
               self.report_text = self.report_text + "\n" + self.ui.txt_adi.text() + " adlı ziyaretçi " + self.ui.cmb_adres.currentText() +" adlı kişiye yönlendirildi."+current_time
               self.ui.txt_rapor.setText(self.report_text)
               img = cv2.imread('images/visitor.jpg', cv2.IMREAD_UNCHANGED)
               scale_percent = 30 # percent of original size
               width = int(img.shape[1] * scale_percent / 100)
               height = int(img.shape[0] * scale_percent / 100)
               dim = (width, height)
               
               # resize image
               resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
               cv2.imwrite("images/visitor_temp_a.jpg",resized)

               self.ui.lbl_kameraA.setStyleSheet("background-image : url(images/visitor_temp_a.jpg); border : 2px solid blue")
               self.ui.lbl_kameraA.setText("")

               self.ui.stackedWidget.setCurrentWidget(self.ui.izleme_sayfasi)
               visitor = Visitor(self.ui.txt_adi,road)
               if(self.human_walk.Start(visitor)):
                  self.ui.label.show()
                  now = datetime.now()
                  current_time = now.strftime("%H:%M:%S")
                  self.report_text = self.report_text + "\n" + self.ui.txt_adi.text() + " adlı ziyaretçi " + self.ui.cmb_adres.currentText() +" adlı kişiye ulaştı."+current_time
                  self.ui.txt_rapor.setText(self.report_text)
               else:
                  self.ui.label_2.show()
                  now = datetime.now()
                  current_time = now.strftime("%H:%M:%S")
                  self.report_text = self.report_text + "\n" + self.ui.txt_adi.text() + " adlı ziyaretçi " + self.ui.cmb_adres.currentText() +" adlı kişiye ulaşamadı."+current_time
                  self.ui.txt_rapor.setText(self.report_text)
      
      # SHOW self.ui PAGE
      if btnName == "btn_raporlar":
         self.ui.stackedWidget.setCurrentWidget(self.ui.raporlar_sayfasi)

      # SHOW self.ui PAGE
      if btnName == "btn_exit":
         file_object = open('report.txt', 'a')
         file_object.write(self.report_text)
         file_object.close()
         QCoreApplication.instance().quit()

            

app = None

if __name__ == "__main__":   
   app = QApplication(sys.argv)
   windows = Design()
   windows.show()
   app.exec_()

