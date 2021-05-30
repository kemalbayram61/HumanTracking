class HumanWalk:
    def __init__(self):
        pass

    def Start(self,visitor):
        visitor_name = visitor.GetName()
        target_road = visitor.GetTargetRoad()
        cameras = target_road.GetCameras()
        face = visitor.GetFace()
        face_found = False

        #Yol üzerindeki bütün kameraları adım adım bulma işlemi
        for camera in cameras:
            #Yol üzerindeki bütün kameralarda yüz kontrollerinin yapılması
            face_found = camera.ReadFace(face)
            #Uyarı mesajı verilecek olan kısım
            if(face_found):
                print(str(visitor_name)+" adlı ziyaretçi kamerada görüntülendi.")

        target_road.Set_Done(True)
        return target_road.GetDone()

