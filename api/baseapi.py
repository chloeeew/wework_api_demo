"""
==================
Author:Chloeee
Time:2021/7/26 22:01
Contact:403505960@qq.com
==================
"""

import jsonpath
from utils.requests_manager import RequestsManager

class BaseApi:
    host = r'https://qyapi.weixin.qq.com/cgi-bin/'
    corp_id = 'ww653fc9506e7deb09'

    def __init__(self):
        self.rm = RequestsManager()

    def __get_access_token(self,corpsecret):
        url = self.host + 'gettoken'
        access_token_params = {'corpid':'ww653fc9506e7deb09','corpsecret':corpsecret}
        response_json = self.rm.send_requests('get',url,params=access_token_params)
        # todo:logger===print(json.dumps(response_json,indent=2,ensure_ascii=False))
        return jsonpath.jsonpath(response_json,"$..access_token")[0]

    def requests_by_access_token(self,corpsecret,method,api_path,**kwargs) -> dict:
        access_token = self.__get_access_token(corpsecret)
        param_data = {"access_token":access_token}
        if kwargs.get("params"):
            param_data.update(kwargs.get('params'))
        response_json = self.rm.send_requests(method,self.host+api_path,params=param_data,**kwargs)
        return response_json


    def get_attributes_by_jsonpath(self, response_dict, expression):
        return jsonpath.jsonpath(response_dict,expression)





#
# if __name__ == '__main__':
    # BaseApi().__get_access_token('7vqhu8H3IsbEDhCV4wSnO0mtl0oW1xnGan5FdvBGCvI')
