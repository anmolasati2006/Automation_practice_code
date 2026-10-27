from playwright.sync_api import Page, expect


class Testcase:
    """Page Object Model for Test Cases workflows."""

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_testcase(self) -> None:
        """Clicks the Test Cases header link and asserts page header visibility."""
        self.page.get_by_role("link", name="Test Cases").click()
        expect(self.page.locator('h2.title:has-text("Test Cases")')).to_be_visible()