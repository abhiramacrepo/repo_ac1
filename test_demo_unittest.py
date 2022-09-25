import pytest

@pytest.yield_fixture() #for both setup and teardown
#@pytest.fixture() for only setup
def setUp(): #method name need not be setup ,method name can be anything it can be anything
    #it can be any name abhi, or m2 anything
    print("setup method")#just using yield keyword will start teardown to differentiate setup and teardown
    #above yield is called setup activitiy
    yield
    print("Teardown")
    #only teardown needed just put yield, no need of setup no setup activity required
    #pass the func name to test methods
#test method naming convention - method name should start with test_
def test_methodA(setUp):
    print("Demo method 1")
#test methods have to be assigned with setupmethod - associate setup method with test method
def test_methodB(setUp):
    print("Demo method 2")
#associate setup to test method i.e pass setup in test method
def test_methodC(setUp):
    print("Demo method 3")

print("test cleared")

#py.test will test all test within current working directory

# -s will print the statment output displayed to the console
# -v verbose output

#how to implement setup method in pytest by using some decorator
#@pytest.fixture() - this is the decorator to use - implement setup

#how to implement teardown in pytest
#decorator to be used for teardown is @pytest.yield_fixture

#@pytest.yield_fixture() #both setup and teardown