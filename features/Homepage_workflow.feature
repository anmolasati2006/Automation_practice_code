Feature: Home Page Workflows

  Scenario Outline: Verify Subscription in home page 
    Given I Verify text as SUBSCRIPTION text is visible
    When I Enter '<email>' address in input and click arrow button
    Then I Verify success message is visible

    Examples:
   | email                       | 
   | iamking0012345678@gmail.com |