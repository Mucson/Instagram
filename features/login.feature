# Created by Vladimir at 28.12.2018
Feature: Login
  Validate user can login with username and password

  Background:
    Given I open login page

  Scenario: Valid login
    When I log in
    When I click now button
    When I enter text in search field
    Then I assert data

  Scenario Outline: Invalid login
    When I type "<username>" in username field
    When I type "<password>" in password field
    When I click login button
    Then I see element with text "Введенное вами имя пользователя не принадлежит аккаунту. Проверьте свое имя пользователя и повторите попытку."

    Examples:
      | username | password |
      | 1234qwrs | 0129412e |
      | hello-12 | zk@0da21 |
      | fidor1mq | d0d@;d42 |


  Scenario: one step
    Then I see validation for message "Введенное вами имя пользователя не принадлежит аккаунту. Проверьте свое имя пользователя и повторите попытку."
      | username | password |
      | 1234qwrs | 0129412e |
      | hello-12 | zk@0da21 |
      | fidor1mq | d0d@;d42 |
    When I type " " in password field