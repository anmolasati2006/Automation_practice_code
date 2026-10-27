from pytest_bdd import given, when, then, parsers, step
from Pages.signup_login_page import SignupLogin



@then(parsers.parse('I enter email "{email}" and password "{password}" and click on Login button'))
def enter_login_details(signup_page: SignupLogin, email, password):
    signup_page.enter_login_details(login_email=email, login_password=password)



@then(parsers.parse('I verify error "{error_msg}" is visible'))
def verify_invalid_user_warning(signup_page: SignupLogin):
    # Note: Using your existing class method (arguments passed are available if needed)
    signup_page.invalid_user_warning()

@then("I click on logout button")
def logout_user(signup_page: SignupLogin):
    signup_page.logout_user()

@step("I verify Login to your account is visible")
def loginpage_title_shown(signup_page: SignupLogin):
    signup_page.loginpage_title_shown()
