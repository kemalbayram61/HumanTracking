class User:
    user_id = ""
    def __init__(self,user_id):
        self.user_id = user_id


class Visitor:
    visitor_name = ""
    target_road = ""
    visitor_face = ""
    def __init__(self,visitor_name,target_road,visitor_face):
        self.visitor_name = visitor_name
        self.target_road = target_road
        self.visitor_face = visitor_face

    def GetTargetRoad(self):
        return self.target_road
    
    def GetVisitorFace(self):
        return self.visitor_face

    def GetName(self):
        return self.visitor_name