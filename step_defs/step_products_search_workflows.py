from pytest_bdd import given, when, then, parsers
from Pages.products_page import Search_Products


@given('I navigate to Products Page & Verify I navigated successfully')
def navigate_to_Products(products_page: Search_Products):
    products_page.navigate_to_Products()

@when('I verify products list is visible')
def all_products_visible(products_page: Search_Products):
    products_page.all_products_visible()

@then('I Click on View Product of first product')
def clickon_first_product(products_page: Search_Products):
    products_page.clickon_first_product()

@then('I verify User is landed on product details page and verify product details are shown')
def verify_all_product_details_visible(products_page: Search_Products):
    products_page.verify_all_product_details_visible()

@then(parsers.parse('I enter "{searched_product_name}" in search input and click search button'))
def search_products(products_page: Search_Products,searched_product_name):
    products_page.search_products(searched_product_name=searched_product_name)

@then('I Verify SEARCHED PRODUCTS is visible')
def searched_products_title_visible(products_page: Search_Products):
    products_page.searched_products_title_visible()

@then(parsers.parse('I Verify all the products related to "{searched_product_name}" are visible'))
def searched_products_contains_prodname(products_page: Search_Products,searched_product_name):
    products_page.searched_products_contains_prodname(searched_product_name=searched_product_name)