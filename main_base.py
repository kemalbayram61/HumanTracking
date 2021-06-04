import Init,Cameras,HumanWalk,Humans,Road

#nesnelerin tanımlanması
init = Init.Init()
main_camera = Cameras.CameraA()
human_walk = HumanWalk.HumanWalk()

#nesne değerlerinin atanması
target = init.Road1()
print(str(len(target.GetCameras()))+" Adet kameradan geçmesi bekleniliyor.")

visitor = Humans.Visitor("Kemal",target)

#Ziyaretcinin görüntüsünün alınması
if(main_camera.ReadFace()==True):

    #Yüz tanıtma işleminin ardından ziyaretçiyi gönderme işlemi başlatılıyor
    if(human_walk.Start(visitor)==True):
        print("Ziyaretçi hedefine güvenle ulaştı.!")
    else:
        print("Ziyaretçi kameraların bazılarında görülemedi.!!!")

