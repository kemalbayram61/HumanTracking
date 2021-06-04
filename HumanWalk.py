class HumanWalk:
    def __init__(self):
        pass

    def Start(self,visitor):
        visitor_name = visitor.GetName()
        target_road = visitor.GetTargetRoad()
        cameras = target_road.GetCameras()
        face_found = False
        is_any_face_fount = False

        #Yol üzerindeki bütün kameraları adım adım bulma işlemi
        for camera in cameras:
            #Yol üzerindeki bütün kameralarda yüz kontrollerinin yapılması
            face_found = camera.ReadFace()
            #Uyarı mesajı verilecek olan kısım
            if(face_found):
                print(str(visitor_name)+" adlı ziyaretçi " + camera.GetName() + " adlı kamerada görüntülendi.")
                is_any_face_fount =True
            else:
                print(str(visitor_name)+" adlı ziyaretçi " + camera.GetName() + " adlı kamerada görülmedi.!")
                is_any_face_fount = False

        target_road.SetDone(is_any_face_fount)
        return target_road.GetDone()

