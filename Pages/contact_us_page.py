import os
from playwright.sync_api import Page, expect


class Contact_us:
    """Page Object Model for Contact Us workflows."""

    file_path = (
        r"C:\Users\anmol\Downloads\Automation_practice_Login\test_doc.txt"
    )

    def __init__(self, page: Page):
        self.page = page

    def navigate_to_contactus_page(self) -> None:
        expect(self.page.get_by_role("link", name="Contact us")).to_be_visible()
        self.page.get_by_role("link", name="Contact us").click()

    def contactus_page_shown(self) -> None:
        expect(self.page.locator('//h2[text()="Get In Touch"]')).to_be_visible()

    def enter_contact_details(
        self, name: str, email: str, subject: str, message: str
    ) -> None:
        self.page.locator('[data-qa="name"]').fill(name)
        self.page.locator('[data-qa="email"]').fill(email)
        self.page.locator('[data-qa="subject"]').fill(subject)
        self.page.locator('[data-qa="message"]').fill(message)

    def upload_file(self, file_path: str = None) -> None:
        """Uploads file using provided file_path or defaults to self.file_path."""
        target_path = file_path if file_path else self.file_path
        clean_path = target_path.strip('"\'')
        normalized_path = os.path.normpath(clean_path)

        if not os.path.exists(normalized_path):
            raise FileNotFoundError(
                f"File not found at target path: {normalized_path}"
            )

        file_upload_input = self.page.locator('input[name="upload_file"]')
        file_upload_input.set_input_files(normalized_path)

    def click_submit_button(self) -> None:
        """Listens for JS dialog, clicks submit, and waits for submission to complete."""
        # Use on() to handle dialog even if multiple popups/alerts fire
        self.page.on("dialog", lambda dialog: dialog.accept())

        submit_btn = self.page.locator('[data-qa="submit-button"]')
        submit_btn.scroll_into_view_if_needed()
        submit_btn.click()

        # Wait for submit network request/page reload
        self.page.wait_for_load_state("domcontentloaded")

    def verify_success_message(self) -> None:
        """Verifies success message container is visible post-submission."""
        success_elem = self.page.locator(".status.alert-success")
        expect(success_elem).to_be_visible(timeout=10000)

    def navigate_to_homepage(self) -> None:
        self.page.get_by_role("link", name="Home").click()
        expect(self.page.get_by_role("link", name="Home")).to_be_visible()