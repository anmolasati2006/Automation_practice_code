Feature: User Login Workflows

  Scenario Outline: Login to the account with valid user credentials and delete account
    Given I navigate to Signup_Login Page
    When I verify Login to your account is visible
    Then I enter email "<email>" and password "<password>" and click on Login button
    And I verify that "Logged in as <username>" is visible
    #And I click Delete Account button and verify account is deleted

    Examples:
      | email                      | password         | username  |
      | test1234test1234@gmail.com | YourPassword123! | Test User |


  Scenario Outline: Login to the account with incorrect user credentials
    Given I navigate to Signup_Login Page
    When I verify Login to your account is visible
    Then I enter email "<email>" and password "<password>" and click on Login button
    And I verify error "Your email or password is incorrect!" is visible

    Examples:
      | email                | password        |
      | invalid_user@abc.com | wrongpassword12 |

  Scenario Outline: Login to the account with valid user credentials and logout account
    Given I navigate to Signup_Login Page
    When I verify Login to your account is visible
    Then I enter email "<email>" and password "<password>" and click on Login button
    Then I verify that "Logged in as <username>" is visible
    And I click on logout button 
    And I verify Login to your account is visible

    Examples:
      | email                      | password         | username  |
      | test1234test1234@gmail.com | YourPassword123! | Test User |