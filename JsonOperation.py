import json

class JsonOperation:
    def __init__(self):
        f = open('data/users.json',)
        self.json_file = json.load(f)
        f.close()

    def GetUser(self,user_name,user_password):
        users = self.json_file["users"]
        for user in users:
            if(user["name"]==user_name and user["password"]==user_password):
                return user
        return False

    def GetUserForC(self,user_name):
        users = self.json_file["users"]
        for user in users:
            if(user["name"]==user_name):
                return user
        return False
    

    def ChangeCameras(self,user_id, new_values):
        f = open('data/users.json','w')
        users = self.json_file["users"]
        for user in users:
            if(user["_id"]==user_id):
                user["cameras"]=new_values
                json.dump(self.json_file,f)
                f.close()
                return True
        f.close()
        return False
