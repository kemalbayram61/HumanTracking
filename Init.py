import Road,Cameras
class Init:
    def __init__(self):
        pass

        #yol nesnelerinin içeriklerinin doldurulması
    def Road1(self,camera_labels):
        road_1 = Road.Road("Ahmet")         #Ahmet kullanıcısına ait yol nesnesini tutar

        camera_b = Cameras.CameraB(camera_labels[0])    #Koridor 1 kamera nesnelerinden birisidir
        camera_e = Cameras.CameraE(camera_labels[1])    #Koridor 2 kamera nesnelerinden birisidir
        camera_f = Cameras.CameraF(camera_labels[2])    #Koridor 2 kamera nesnelerinden birisidir

        #Ahmet kullanıcısına ait yol nesnesinin doldurulması
        road_1.AddCamera(camera_b)
        road_1.AddCamera(camera_e)
        road_1.AddCamera(camera_f)
        return road_1

    def Road2(self,camera_labels):
        road_2 = Road.Road("Mehmet")        #Mehmet kullanıcısına ait yol nesnesini tutar

        camera_b = Cameras.CameraB(camera_labels[0])    #Koridor 1 kamera nesnelerinden birisidir
        camera_c = Cameras.CameraC(camera_labels[1])    #Koridor 1 kamera nesnelerinden birisidir
        camera_g = Cameras.CameraG(camera_labels[2])    #Koridor 3 kamera nesnelerinden birisidir
        camera_h = Cameras.CameraH(camera_labels[3])    #Koridor 3 kamera nesnelerinden birisidir

        #Mehmet kullanıcısına ait yol nesnesinin doldurulması
        road_2.AddCamera(camera_b)
        road_2.AddCamera(camera_c)
        road_2.AddCamera(camera_g)
        road_2.AddCamera(camera_h)
        return road_2

    def Road3(self,camera_labels):
        road_3 = Road.Road("Hasan")         #Hasan kullanıcısına ait yol nesnesini tutar

        camera_b = Cameras.CameraB(camera_labels[0])    #Koridor 1 kamera nesnelerinden birisidir
        camera_c = Cameras.CameraC(camera_labels[1])    #Koridor 1 kamera nesnelerinden birisidir
        camera_d = Cameras.CameraD(camera_labels[2])    #Koridor 1 kamera nesnelerinden birisidir

        #Hasan kullanıcısına ait yol nesnesinin doldurulması
        road_3.AddCamera(camera_b)
        road_3.AddCamera(camera_c)
        road_3.AddCamera(camera_d)
        return road_3
    