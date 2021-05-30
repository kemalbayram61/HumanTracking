class Road:
    camera_list = []
    road_name = ""
    done_case = False
    def __init__(self,road_name):
        self.road_name = road_name

    def AddCamera(self, camera):
        self.camera_list.append(camera)

    def GetCameras(self):
        return self.camera_list

    def SetDone(self, value):
        self.done_case = value

    def GetDone(self):
        return self.done_case