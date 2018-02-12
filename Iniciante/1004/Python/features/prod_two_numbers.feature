Feature: prod_two_numbers
    Scenario Outline: Prod any two numbers
        Given I have entered <number1>
        And I have also entered <number2>
        When I prod
        Then the prod should be <result>

    Examples:
        | number1 | number2 | result |
        |       3 |       9 |     27 |
        |     -30 |      10 |   -300 |
        |       0 |       9 |      0 |

