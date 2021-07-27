"""
==================
Author:Chloeee
Time:2021/7/26 21:27
Contact:403505960@qq.com
==================
"""
import json
import requests
from utils.logger_handler import logger


class RequestsManager:


    def send_requests(self,method,url,**kwargs):
        try:
            response = requests.request(method, url=url, **kwargs)
        except ConnectionError as ce:
            logger.error("链接失败，请检查")
            raise ce
        else:
            # 用json格式返回响应体
            response_json = response.json()
            logger.info(f"请求成功，返回数据：{json.dumps(response_json,indent=2,ensure_ascii=False)}")
            return response_json





