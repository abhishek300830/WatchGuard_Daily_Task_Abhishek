import pytest


@pytest.fixture(scope='module')
def setup():
    print("---setup---")
    yield setup
    print("--teardown--")


# def setup_module(module):
#     print("---Setup-----")
#
#
# def teardown_module(module):
#     print("----tearDown-----")


def test1(setup):
    print("Test 1")
    assert True


def test2(setup):
    print("Test 2")
    assert True


@pytest.mark.usefixtures('setup')
def test3():
    print("test 3")
    assert True

