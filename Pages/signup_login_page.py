from playwright.sync_api import Page, expect


class SignupLogin:
    """Page Object Model for Signup and Account Creation workflows."""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_signup(self) -> None:
        """Navigate to signup and submit initial user credentials."""
        # Click on 'Signup / Login' button
        self.page.get_by_role("link", name="Signup / Login").click()

    def submit_initial_signup_details(self,name,email) -> None:
        #Verify 'New User Signup!' is visible
        expect(self.page.get_by_role("heading", name="New User Signup!")).to_be_visible()
        #Enter name and email address
        self.page.get_by_placeholder("Name").fill(name)
        self.page.locator('input[data-qa="signup-email"]').fill(email)
        #Click 'Signup' button
        self.page.get_by_role("button", name="Signup").click()
        

    def enter_info(self,password,date,month,year) -> None:
        #Verify that 'ENTER ACCOUNT INFORMATION' is visible
        expect(self.page.get_by_role("heading", name="Enter Account Information")).to_be_visible()
        """Enter account details, personal address, and create account."""
        #Fill details: Title, Name, Email, Password, Date of birth
        self.page.get_by_label("Mr.").check()
        self.page.locator('input[data-qa="password"]').fill(password)
        self.page.locator('select[data-qa="days"]').select_option(date)
        self.page.locator('select[data-qa="months"]').select_option(month)  # June
        self.page.locator('select[data-qa="years"]').select_option(year)

    def verify_prefilled_user_details(self, name, email) -> None:
        #Verify user name is same as provided above and is editable
        expect(self.page.locator('input[data-qa="name"]')).to_have_value(name)
        expect(self.page.locator('input[data-qa="name"]')).to_be_editable()
        #Verify user email is same as provided above and is non-editable
        expect(self.page.locator('input[data-qa="email"]')).to_be_disabled()
        expect(self.page.locator('input[data-qa="email"]')).to_have_value(email)

    def select_newsletter_and_offers(self) -> None:
        #Select checkbox 'Sign up for our newsletter!'
        self.page.get_by_label("Sign up for our newsletter!").check()
        #Select checkbox 'Receive special offers from our partners!'
        self.page.get_by_label("Receive special offers from our partners!").check()

    def fill_address_information(self,fname,lname,company,address1,address2,country,state,city,zipcode,mobile_no) -> None:
        #Fill address details & submit
        self.page.get_by_label("First name *").fill(fname)
        self.page.get_by_label("Last name *").fill(lname)
        self.page.locator('input[data-qa="company"]').fill(company)
        self.page.get_by_label("Address *").fill(address1)
        self.page.get_by_label("Address 2").fill(address2)
        self.page.get_by_label("Country *").select_option(country)
        self.page.get_by_label("State *").fill(state)
        self.page.get_by_label("City *").fill(city)
        self.page.locator('input[data-qa="zipcode"]').fill(zipcode)
        self.page.get_by_label("Mobile Number *").fill(mobile_no)
        #Click Create Account
        self.page.get_by_role("button", name="Create Account").click()

    def check_account_created(self) -> None:
        expect(self.page.locator('h2[data-qa="account-created"]')).to_be_visible()
        self.page.locator('a[data-qa="continue-button"]').click()  

    def enter_login_details(self,login_email,login_password) -> None:
        self.page.locator('input[data-qa="login-email"]').fill(login_email)
        self.page.get_by_placeholder("Password").fill(login_password)  
        self.page.get_by_role('button',name="Login").click()  

    def loggedin_user_shown(self,name) -> None:
        expect(self.page.locator('a:has(i.fa-user)')).to_contain_text(name)

    def delete_account(self) -> None:
        self.page.locator('a[href="/delete_account"]').click()
        expect(self.page.locator('h2[data-qa="account-deleted"]')).to_be_visible()
        self.page.locator('a[data-qa="continue-button"]').click()

    def invalid_user_warning(self) -> None:
        expect(self.page.get_by_text("Your email or password is incorrect!")).to_be_visible()


    def logout_user(self) -> None:
        self.page.locator('a[href="/logout"]').click()

    def loginpage_title_shown(self) -> None:
        expect(self.page.locator('//h2[text()="Login to your account"]')).to_be_visible()

    def email_already_exist(self) -> None:
        expect(self.page.locator('//p[text()="Email Address already exist!"]')).to_be_visible()
