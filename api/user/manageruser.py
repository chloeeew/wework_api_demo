"""
==================
Author:Chloeee
Time:2021/7/27 15:11
Contact:403505960@qq.com
==================
"""


from api.user.user_base import UserBase

class ManagerUser(UserBase):
    def create_user(self,user_id:str ,name:str,department:dict,**kwargs):
        path = 'create'
        data = {
                "userid": user_id,
                "name": name,
                "department": department
            }
        data.update(kwargs)
        return self.usr_requests("post",path,json=data)

    def get_user(self,user_id):
        path = 'get'
        data = {'userid':user_id}
        return self.usr_requests("get",path,params=data)

