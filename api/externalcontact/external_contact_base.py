"""
==================
Author:Chloeee
Time:2021/7/26 21:53
Contact:403505960@qq.com
==================
"""

from api.baseapi import BaseApi

class ExternalContactBase(BaseApi):
    api_url = r'externalcontact/'
    corpsecret = '7vqhu8H3IsbEDhCV4wSnO0mtl0oW1xnGan5FdvBGCvI'

    def ec_requests(self,method,path,**kwargs):
        api_url = self.api_url + path
        return self.requests_by_access_token(self.corpsecret,method,api_url,**kwargs)









# if __name__ == '__main__':
#     ExternalContactBase().get_access_token()
