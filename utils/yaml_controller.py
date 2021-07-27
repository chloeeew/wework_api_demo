"""
==================
Author:Chloeee
Time:2021/4/14 20:19
Contact:403505960@qq.com
==================
"""

import yaml
from config.path import corp_tag_data_yaml_path,config_yaml_path



def read_yaml(fpath):
    """
    :param fpath: yaml路径
    :return: yaml里的数据
    """
    with open(fpath, encoding="utf-8") as f:
        data = yaml.load(f, yaml.FullLoader)
        return data



yaml_data = read_yaml(corp_tag_data_yaml_path)
yaml_config = read_yaml(config_yaml_path)




