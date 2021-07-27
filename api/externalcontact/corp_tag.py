"""
==================
Author:Chloeee
Time:2021/7/26 13:19
Contact:403505960@qq.com
==================
"""

from api.externalcontact.external_contact_base import ExternalContactBase

class CorpTag(ExternalContactBase):



    def search_tag(self, tag_id: list = None, group: list = None) -> dict:
        """
        若tag_id和group_id均为空，则返回所有标签。
        同时传递tag_id和group_id时，忽略tag_id，仅以group_id作为过滤条件。
        """
        path = 'get_corp_tag_list'
        data = {"tag_id":tag_id,"group_id":group}
        response_json = self.ec_requests("post",path,json=data)
        return response_json

    def add_tag(self,tag_dict:list,group_id:str = None, group_name:str = None,group_order:int = None,agentid:int = None
                ):
        """
        如果要向指定的标签组下添加标签，需要填写group_id参数；如果要创建一个全新的标签组以及标签，则需要通过group_name参数指定新标
        签组名称，如果填写的groupname已经存在，则会在此标签组下新建标签。如果填写了group_id参数，则group_name和标签组的order参数
        会被忽略。不支持创建空标签组。标签组内的标签不可同名，如果传入多个同名标签，则只会创建一个。
        tag_dict参考：[{
            "name": "TAG_NAME_1",
            "order": 1
        },
        {
            "name": "TAG_NAME_2",
            "order": 2
        }]
        """
        path = 'add_corp_tag'
        data = {"group_id": group_id, "group_name": group_name,"order": group_order,
                "tag": tag_dict,"agentid" : agentid
                }
        response_json = self.ec_requests("post", path, json=data)
        return response_json


    def edit_tag(self,id:str,name:str,order:int=None,agentid:int = None):
        path = 'edit_corp_tag'
        data = {"id": id,"name": name,"order": order,"agentid": agentid}
        response_json = self.ec_requests("post", path, json=data)
        return response_json


    def delete_tag(self,tag_id:list = None,group_id:list = None,agentid:int = None):
        """
        tag_id和group_id不可同时为空。
        如果一个标签组下所有的标签均被删除，则标签组会被自动删除。
        tag_id例子："tag_id": [
        "TAG_ID_1",
        "TAG_ID_2"
        ]
        """
        path = 'del_corp_tag'
        data ={"tag_id":tag_id,"group_id": group_id,"agentid" : agentid}
        response_json = self.ec_requests("post", path, json=data)
        return response_json


    def get_tags_id_by_name(self,response_dict,name):
        expression = f'$..tag[?(@.name=="{name}")].id'
        # tag_01_id = jsonpath.jsonpath(search_result_02,'$..tag[?(@.name=="冒烟tag1")].id')
        return self.get_attributes_by_jsonpath(response_dict, expression)

    def get_tags_id(self,response_dict):
        expression = '$..id'
        return self.get_attributes_by_jsonpath(response_dict, expression)


    def get_groups_tag_id_by_name(self,response_dict,name):
        expression = f'$..tag_group[?(@.group_name=="{name}")].group_id'
        # jsonpath.jsonpath(search_result_02,'$..tag_group[?(@.group_name=="冒烟组GROUP2!")].group_id')
        return self.get_attributes_by_jsonpath(response_dict, expression)

    def get_tags_name(self,response_dict):
        expression = "$..name"
        return self.get_attributes_by_jsonpath(response_dict,expression)

    def get_groups_name(self,response_dic):
        expression = "$..group_name"
        return self.get_attributes_by_jsonpath(response_dic,expression)


    def get_orders_by_name(self,response_dict,name):
        expression = f'$..tag[?(@.name=="{name}")].order'
        return self.get_attributes_by_jsonpath(response_dict,expression)


    def initial_tag(self):
        """清理和初始化的工作,删除所有的tag，初始化一组3个tag"""
        # 删除所有的tag
        tags_id_list = self.get_tags_id(self.search_tag())
        self.delete_tag(tag_id=tags_id_list)
        # 初始化3个tag
        initial_tags = [{"name":"一般"},{"name":"重要"},{"name":"非常重要"}]
        self.add_tag(tag_dict=initial_tags,group_name="客户等级")






