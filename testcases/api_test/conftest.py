import pytest
from small_FrontalGate.testcases.conftest import api_data


@pytest.fixture(scope="function")
def testcase_data(request):
    testcase_name = request.function.__name__
    return api_data.get(testcase_name)