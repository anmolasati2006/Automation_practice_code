from pytest_bdd import given, when, then, parsers
from Pages.signup_login_page import SignupLogin




@when(parsers.parse('I enter "{name}" and "{email}" and click on Signup button'))
def submit_initial_signup_details(signup_page: SignupLogin, name: str, email: str):
    signup_page.submit_initial_signup_details(name=name, email=email)

@then(parsers.parse('I enter "{password}" and then enter "{date}" and "{month}" and "{year}" as DOB'))
def enter_info(signup_page: SignupLogin,password,date,month,year):
    signup_page.enter_info(password=password, date=date, month=month, year=year)


@then(parsers.parse('I verify "{name}" and "{email}" are prefilled as entered in signup Page'))
def verify_prefilled_user_details(signup_page: SignupLogin, name,email):
    signup_page.verify_prefilled_user_details(name=name,email=email)


@then(('I select checkbox for signup'))
def select_newsletter_and_offers(signup_page: SignupLogin):
    signup_page.select_newsletter_and_offers()


@then(('I verify Account created is shown'))
def check_account_created(signup_page: SignupLogin):
    signup_page.check_account_created()

@then(parsers.parse('I verify error "{error_msg}" is visible'))
def verify_invalid_user_warning(signup_page: SignupLogin):
    # Note: Using your existing class method (arguments passed are available if needed)
    signup_page.invalid_user_warning()

@then(parsers.parse('I fill address details for "{first_name}" "{last_name}" "{company}" "{address1}" "{address2}" "{country}" "{state}" "{city}" "{zipcode}" and "{mobile}"'))
def fill_address_information(signup_page: SignupLogin,first_name,last_name,company,address1,address2,country,state,city,zipcode,mobile,):
    signup_page.fill_address_information(fname=first_name,lname=last_name,company=company,address1=address1,address2=address2,country=country,state=state,city=city,zipcode=zipcode,mobile_no=mobile)


@then('I verify email already exist message is shown')
def email_already_exist(signup_page: SignupLogin):
    signup_page.email_already_exist()