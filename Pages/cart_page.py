from playwright.sync_api import Page, expect
import time


class Cartpage:

    def __init__(self, page: Page):
        self.page = page

    def subscription_title_visible(self,) -> None:
        expect(self.page.locator("//h2[text()='Subscription']")).to_be_visible

    def enter_subscription_details(self,email) -> None:
        self.page.locator("//input[@id='susbscribe_email']").fill(email)
        self.page.locator("//button[@id='subscribe']").click()

    def subscription_success_message(self) -> None:   
        expect(self.page.locator('#success-subscribe .alert-success')).to_be_visible()



