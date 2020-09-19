import pytest
import allure
import sys
print(sys.path)

from operation.user import login_user
from testcases.conftest import api_data
from common.logger import logger


@allure.step("步骤1 ==>> 登录用户")
def step_1(username):
    logger.info("步骤1 ==>> 登录用户：{}".format(username))


@allure.feature("用户登录模块")
class TestUserLogin():

    @allure.story("用例--登录用户")
    @pytest.mark.single
    @pytest.mark.parametrize("username, password, except_result, except_code, except_msg",
                             api_data["test_login_user"])
    def test_login_user(self, username, password, except_result, except_code, except_msg):
        logger.info("*************** 开始执行用例 ***************")
        result = login_user(username, password)
        step_1(username)
        assert result.success == except_result, result.error
        assert result.response.status_code == 200
        assert result.success == except_result, result.error
        logger.info("code ==>> 期望结果：{}， 实际结果：【 {} 】".format(except_code, result.response.json().get("code")))
        assert result.response.json().get("code") == except_code
        assert except_msg in result.msg
        logger.info("*************** 结束执行用例 ***************")


if __name__ == '__main__':
    pytest.main(["-q", "-s", "test_03_login.py"])
