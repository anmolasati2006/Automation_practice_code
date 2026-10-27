from Pages.contact_us_page import Contact_us
from pytest_bdd import given, parsers, step, then, when


@given("I navigate to Contact Us Page")
def navigate_to_contactus_page(contact_us: Contact_us):
    contact_us.navigate_to_contactus_page()


@when("I can see contact us page is visible")
def contactus_page_shown(contact_us: Contact_us):
    contact_us.contactus_page_shown()


@then(parsers.parse('I enter "{name}" "{email}" "{subject}" "{message}"'))
def enter_contact_details(
    contact_us: Contact_us, name: str, email: str, subject: str, message: str
):
    contact_us.enter_contact_details(
        name=name, email=email, subject=subject, message=message
    )


@then("I Upload a file from provided path")
def upload_file(contact_us: Contact_us):
    contact_us.upload_file()


@then("I click on submit button")
def click_submit_button(contact_us: Contact_us):
    contact_us.click_submit_button()


@then("I verify the success message")
def verify_success_message(contact_us: Contact_us):
    contact_us.verify_success_message()


@then("I navigate to hompage and verify it is visible")
def navigate_to_homepage(contact_us: Contact_us):
    contact_us.navigate_to_homepage()