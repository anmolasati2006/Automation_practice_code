Feature: Contact Us Workflows

  Scenario Outline: User is able to fill contact us form and submit successfully
    Given I navigate to Contact Us Page 
    When I can see contact us page is visible 
    Then I enter "<name>" "<email>" "<subject>" "<message>" 
    And I Upload a file from provided path
    And I click on submit button 
    And I verify the success message 
    Then I navigate to hompage and verify it is visible

    Examples:
      | name      | email                       | subject | message   |
      | Test User | iamking0012345678@gmail.com | Testing | I am king |