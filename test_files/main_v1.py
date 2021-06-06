from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QCoreApplication
from DesignPythonv1 import Ui_MainWindow
import sys
import Init,Cameras,HumanWalk,Humans

class Design(QMainWindow):
   def __init__(self):
      super().__init__()
      self.ui =Ui_MainWindow()
      self.ui.setupUi(self)
      self.ui.btn_kamera.clicked.connect(self.buttonClick)
      self.ui.btn_calisanlar.clicked.connect(self.buttonClick)
      self.ui.btn_izlenme.clicked.connect(self.buttonClick)
      self.ui.btn_raporlar.clicked.connect(self.buttonClick)
      self.ui.btn_ziyaretci.clicked.connect(self.buttonClick)
      self.ui.btn_exit.clicked.connect(self.buttonClick)

   def buttonClick(self):
      # GET BUTTON CLICKED
      btn = self.sender()
      btnName = btn.objectName()

      # SHOW HOME PAGE
      if btnName == "btn_kamera":         
         self.ui.stackedWidget.setCurrentWidget(self.ui.kameralar_sayfasi)
         
      # SHOW CALISANLAR PAGE
      if btnName == "btn_calisanlar":
         self.ui.stackedWidget.setCurrentWidget(self.ui.calisanlar_sayfasi)

       # SHOW HOME PAGE
      if btnName == "btn_ziyaretci":         
         self.ui.stackedWidget.setCurrentWidget(self.ui.ziyaretci_sayfasi)

      # SHOW self.ui PAGE
      if btnName == "btn_izlenme":
         self.ui.stackedWidget.setCurrentWidget(self.ui.izleme_sayfasi)
      
      # SHOW self.ui PAGE
      if btnName == "btn_raporlar":
         self.ui.stackedWidget.setCurrentWidget(self.ui.raporlar_sayfasi)

      # SHOW self.ui PAGE
      if btnName == "btn_exit":
         QCoreApplication.instance().quit()

            

app = None

if __name__ == "__main__":   
   app = QApplication(sys.argv)
   windows = Design()
   windows.show()
   app.exec_()
