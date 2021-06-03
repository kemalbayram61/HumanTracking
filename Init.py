import Road,Cameras
class Init:
    road_1 = ""
    road_2 = ""
    road_3 = ""

    def __init__(self):
        pass

    def Load(self):
        #boş nesnelerin tanımlanması
        self.road_1 = Road.Road("Ahmet")         #Ahmet kullanıcısına ait yol nesnesini tutar
        self.road_2 = Road.Road("Mehmet")        #Mehmet kullanıcısına ait yol nesnesini tutar
        self.road_3 = Road.Road("Hasan")         #Hasan kullanıcısına ait yol nesnesini tutar

        #kamera nesnelerinin tanımlanması
        camera_a = Cameras.CameraA()    #Danışmadaki kamera nesnesini tutar
        camera_b = Cameras.CameraB()    #Koridor 1 kamera nesnelerinden birisidir
        camera_c = Cameras.CameraC()    #Koridor 1 kamera nesnelerinden birisidir
        camera_d = Cameras.CameraD()    #Koridor 1 kamera nesnelerinden birisidir
        camera_e = Cameras.CameraE()    #Koridor 2 kamera nesnelerinden birisidir
        camera_f = Cameras.CameraF()    #Koridor 2 kamera nesnelerinden birisidir
        camera_g = Cameras.CameraG()    #Koridor 3 kamera nesnelerinden birisidir
        camera_h = Cameras.CameraH()    #Koridor 3 kamera nesnelerinden birisidir

        #yol nesnelerinin içeriklerinin doldurulması
        #Ahmet kullanıcısına ait yol nesnesinin doldurulması
        self.road_1.AddCamera(camera_b)
        self.road_1.AddCamera(camera_e)
        self.road_1.AddCamera(camera_f)
        #Mehmet kullanıcısına ait yol nesnesinin doldurulması
        self.road_2.AddCamera(camera_b)
        self.road_2.AddCamera(camera_c)
        self.road_2.AddCamera(camera_g)
        self.road_2.AddCamera(camera_h)
        #Hasan kullanıcısına ait yol nesnesinin doldurulması
        self.road_3.AddCamera(camera_b)
        self.road_3.AddCamera(camera_c)
        self.road_3.AddCamera(camera_d)
    