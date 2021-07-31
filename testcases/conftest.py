"""
==================
Author:Chloeee
Time:2021/7/27 13:44
Contact:403505960@qq.com
==================
"""


import pytest
from api.externalcontact.corp_tag import CorpTag

@pytest.fixture(scope="class")
def init_corp_tag():
    ct = CorpTag()
    ct.initial_tag()


