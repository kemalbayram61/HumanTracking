class User:
    user_id        = ""
    user_name      = ""
    user_password  = ""
    user_authority = ""
    user_cameras   = ""
    def __init__(self):
        pass

    def Setuser(self, json_user):
        self.user_id        = json_user["_id"]
        self.user_name      = json_user["name"]
        self.user_password  = json_user["password"]
        self.user_authority = json_user["authority"]
        self.user_cameras   = json_user["cameras"]


class Visitor:
    visitor_name = ""
    target_road = ""
    def __init__(self,visitor_name,target_road):
        self.visitor_name = visitor_name
        self.target_road = target_road

    def GetTargetRoad(self):
        return self.target_road

    def GetName(self):
        return self.visitor_name