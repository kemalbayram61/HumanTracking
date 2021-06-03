class User:
    user_id = ""
    def __init__(self,user_id):
        self.user_id = user_id


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