"""
==================
Author:Chloeee
Time:2021/7/27 15:12
Contact:403505960@qq.com
==================
"""

from api.baseapi import BaseApi

class UserBase(BaseApi):
    api_url = r'user/'
    corpsecret = 'innRabibJwosRxYsEBCcatdvTZTi544R_ftQ3hR7EEk'

    def usr_requests(self,method,path,**kwargs):
        api_url = self.api_url + path
        response_json = self.requests_by_access_token(self.corpsecret,method,api_url,**kwargs)
        return response_json



