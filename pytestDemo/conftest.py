import pytest


@pytest.fixture(scope="class")
def setup():
    print("Setup initialization")
    yield
    print("Tear down steps")



@pytest.fixture(scope="class")
def dataLoad():
    print("user profile data is being created")
    return ["Suraj","Khopkar","suraj@mail.com"]



@pytest.fixture(params=["chrome","firefox","ie"])
def crossBrowser(request):
    return request.param