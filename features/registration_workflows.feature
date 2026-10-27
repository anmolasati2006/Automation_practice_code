Feature: Registration Workflows

  Scenario Outline: Register the user and then delete the account
    Given I navigate to Signup_Login Page 
    When I enter "<name>" and "<email>" and click on Signup button 
    Then I enter "<password>" and then enter "<date>" and "<month>" and "<year>" as DOB 
    And I verify "<name>" and "<email>" are prefilled as entered in signup Page 
    And I select checkbox for signup 
    And I fill address details for "<first_name>" "<last_name>" "<company>" "<address1>" "<address2>" "<country>" "<state>" "<city>" "<zipcode>" and "<mobile>" 
    And I verify Account created is shown 
    Then I verify that "Logged in as <username>" is visible 
    And I click Delete Account button and verify account is deleted 


    Examples:
      | name      | email                   | password         | date | month | year | username  | first_name | last_name | company | address1    | address2 | country | state      | city     | zipcode | mobile     |
      | Test User | iamking0012345678@gmail.com | YourPassword123! | 20   | 6     | 1999 | Test User | John       | Doe       | QA Corp | 123 Main St | Suite 4  | India     | California | New York | 10001   | 1234567890 |


  Scenario Outline: Register the user with already valid account
    Given I navigate to Signup_Login Page 
    When I enter "<name>" and "<email>" and click on Signup button 
    Then I verify email already exist message is shown

    Examples:
      | name      | email                   |
      | Test User | test1234test1234@gmail.com |