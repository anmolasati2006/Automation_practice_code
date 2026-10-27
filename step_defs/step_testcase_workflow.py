from pytest_bdd import given, when, then, parsers
from Pages.testcase_page import Testcase




@given('I navigate to Test case Page')
def navigate_to_testcase(testcase_page: Testcase):
    testcase_page.navigate_to_testcase()
