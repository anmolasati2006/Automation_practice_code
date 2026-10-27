Feature: Verify Products Search Workflows


  Scenario Outline: Verify All Products and product detail page
    Given I navigate to Products Page & Verify I navigated successfully 
    When I verify products list is visible
    Then I Click on View Product of first product
    Then I verify User is landed on product details page and verify product details are shown

  Scenario Outline: Search Products
    Given I navigate to Products Page & Verify I navigated successfully 
    When I verify products list is visible
    Then I enter "<searched_product_name>" in search input and click search button
    Then I Verify SEARCHED PRODUCTS is visible
    Then I Verify all the products related to "<searched_product_name>" are visible

    Examples:
    | searched_product_name |
    | top |
