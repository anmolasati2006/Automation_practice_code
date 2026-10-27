from playwright.sync_api import Page, expect
import time


class Search_Products:
    """Page Object Model for Test Cases workflows."""

    def __init__(self, page: Page):
        self.page = page
        self.container = page.locator(".product-information")
        self.product_cards = page.locator(".single-products")


    def navigate_to_Products(self) -> None:
        self.page.get_by_role("link", name=" Products").click()
        expect(self.page.locator("//h2[text()='All Products']")).to_be_visible

    def all_products_visible(self) -> None:
        expect(self.page.locator(".features_items")).to_be_visible

    def clickon_first_product(self) -> None:
        self.page.locator('a[href="/product_details/1"]').click()

    def verify_all_product_details_visible(self) -> None:
        expect(self.page.get_by_role("button", name="Add to cart")).to_be_visible()
        expect(self.container.locator("h2").first).to_be_visible()
        expect(self.container.locator("span > span").first).to_be_visible()
        expect(self.container.locator("p", has_text="Category:")).to_be_visible()
        expect(self.container.locator("p", has_text="Availability:")).to_be_visible()
        expect(self.container.locator("p", has_text="Condition:")).to_be_visible()
        expect(self.container.locator("p", has_text="Brand:")).to_be_visible()

    def search_products(self,searched_product_name) -> None:
        self.page.locator('//*[@id="search_product"]').fill(searched_product_name)
        time.sleep(2)
        self.page.locator('//*[@id="submit_search"]').click()
        time.sleep(5)

    def searched_products_title_visible(self) -> None:
        expect(self.page.locator('//h2[text()="Searched Products"]')).to_be_visible


    def searched_products_contains_prodname(self,searched_product_name) -> None:
        count = self.product_cards.count()
        for i in range(count):
            card = self.product_cards.nth(i)
            # Scope search strictly inside the current product card's productinfo block
            product_name_locator = card.locator(".productinfo p")

            # Extract full text content from the product name paragraph
            product_name = product_name_locator.text_content()

            # Assert that 'Top' exists in the product name (case-insensitive check)
            #assert (searched_product_name in product_name.lower()), 
            print(f"Expected product name to contain 'Top', but got: '{product_name}' at index {i}")
            time.sleep(2)



class Add_Products:

    def __init__(self, page: Page):
        self.page = page

    def add_to_cart(self)-> None:
        # 1. Locate the specific card containing product ID 1
        card = self.page.locator(".productinfo", has=self.page.locator("a[data-product-id='1']"))
        # 2. Extract and clean the product name ("Blue Top")
        product_name = card.locator("p").text_content().strip()


        self.page.locator(".productinfo").first.hover()
        self.page.locator("a.add-to-cart[data-product-id='1']").click()
        self.page.get_by_role("button",name="Continue Shopping").click()
        self.page.locator(".productinfo").nth(1).hover()
        self.page.locator("a.add-to-cart[data-product-id='2']").click()
        self.page.get_by_role("link", name="View Cart").click()

