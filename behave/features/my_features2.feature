Feature: Calculator
    In order to avoid silly mistakes
    I want to be told the sum of two numbers

    Scenario: Add two numbers
        Given I have entered 5 into the calculator and I have entered 7 into the calculator
        When I press add
        Then the result should be 12 on the screen
