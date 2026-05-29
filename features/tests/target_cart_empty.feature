# Created by monalimodi at 5/29/26
Feature: Test case for Empty Cart on Target

  Scenario: User can see cart empty msg
    Given Open Target main page
    When Click on Cart icon
    Then Verify 'Your cart is empty' message is shown