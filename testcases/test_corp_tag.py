"""
==================
Author:Chloeee
Time:2021/7/26 13:20
Contact:403505960@qq.com
==================
"""
import allure
import pytest
from api.externalcontact.corp_tag import CorpTag
from utils.yaml_controller import yaml_data


@allure.epic("企业微信web")
@pytest.mark.usefixtures("init_corp_tag")
@allure.feature("管理企业标签")
class TestCorpTag:

    @allure.title("管理企业标签全流程冒烟测试")
    @pytest.mark.run(order=1)
    def test_smoke_success(self):
        """
        冒烟测试：管理企业标签全流程
        1、获取现存tag
        2、添加tag（数字+中英文）及顺带添加组（数字+中英文+字符）
        3、在添加的组下再次添加tag,order=3
        4、编辑tag,更改为（中+字符）
        5、删除1个tag
        6、再删除1个tag使得group被删除
        """
        datas = yaml_data['smoke']
        ct = CorpTag()

        with allure.step("步骤一：获取当前所有tag,默认存在组客户等级，以及tag名一般"):
            search_result_01 = ct.search_tag()
            assert datas['testsearch']['groupname'] in ct.get_groups_name(search_result_01)
            assert datas['testsearch']['tagsname'] in ct.get_tags_name(search_result_01)


        with allure.step("步骤二：添加tag：冒烟tag1，组名：冒烟组GROUP2!"):
            ct.add_tag([{"name":datas['testadd']['tagname']}],group_name=datas['testadd']['groupname'])
            search_result_02 = ct.search_tag()
            assert datas['testadd']['tagname'] in ct.get_tags_name(search_result_02)
            assert datas['testadd']['groupname'] in ct.get_groups_name(search_result_02)
            # 获取tag后续用
            tag_01_id = ct.get_tags_id_by_name(search_result_02,datas['testadd']['tagname'])[0]
            group_id = ct.get_groups_tag_id_by_name(search_result_02,datas['testadd']['groupname'])[0]


        with allure.step("步骤三： 在添加的组下再次添加tag,order=3"):
            ct.add_tag([{"name":datas['testaddorder']['tagname'],"order":datas['testaddorder']['order']}],
                       group_id=group_id)
            search_result_03 = ct.search_tag()
            assert datas['testaddorder']['tagname'] in ct.get_tags_name(search_result_03)
            assert datas['testaddorder']['order'] == ct.get_orders_by_name(search_result_03,datas['testaddorder']['tagname'])[0]
            tag_02_id = ct.get_tags_id_by_name(search_result_03,datas['testaddorder']['tagname'])[0]


        with allure.step("步骤四：编辑tag,更改为（中+字符）"):
            ct.edit_tag(id=tag_02_id,name=datas['testedit']['tagname'])
            search_result_04 = ct.search_tag()
            assert datas['testedit']['tagname'] in ct.get_tags_name(search_result_04)


        with allure.step("步骤五：删除1个tag，group仍存在"):
            ct.delete_tag([tag_01_id])
            search_result_05 = ct.search_tag()
            assert tag_01_id not in ct.get_tags_id(search_result_05)
            assert "冒烟组GROUP2!" in ct.get_groups_name(search_result_05)


        with allure.step("步骤六：再删除1个tag使得group被删除"):
            ct.delete_tag([tag_02_id])
            search_result_06 = ct.search_tag()
            assert tag_02_id not in ct.get_tags_id(search_result_06)
            assert "冒烟组GROUP2!" not in ct.get_groups_name(search_result_06)

    @allure.title("测试增加标签-未实现")
    @pytest.mark.run(order=2)
    def test_add_tag(self):
        pass


    @allure.title("测试编辑标签-未实现")
    @pytest.mark.run(order=3)
    def test_edit_tag(self):
        pass

    @allure.title("测试删除标签-未实现")
    @pytest.mark.run(order=4)
    def test_delete_tag(self):
        pass







