from pytest_bdd import given, when, then, parsers,step
from Pages.signup_login_page import SignupLogin
from Pages.home_page import Homepage


@given("I navigate to Signup_Login Page")
def navigate_to_signup(signup_page: SignupLogin):
    signup_page.navigate_to_signup()

@then(parsers.parse('I verify that "Logged in as {username}" is visible'))
def verify_loggedin_user(signup_page: SignupLogin, username):
    signup_page.loggedin_user_shown(name=username)

@then("I click Delete Account button and verify account is deleted")
def delete_account(signup_page: SignupLogin):
    signup_page.delete_account()


@given("I Verify text as SUBSCRIPTION text is visible")
def subscription_title_visible(homepage: Homepage):
    homepage.subscription_title_visible()


@when(parsers.parse("I Enter '{email}' address in input and click arrow button"))
def enter_subscription_details(homepage: Homepage,email):
    homepage.enter_subscription_details(email=email)

@then("I Verify success message is visible")
def subscription_success_message(homepage: Homepage):
    homepage.subscription_success_message()