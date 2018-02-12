Feature: sum_two_numbers
    Scenario Outline: Add any two numbers
        Given I have entered <number1>
        And I have also entered <number2>
        When I sum
        Then the sum should be <result>

    Examples:
        | number1 | number2 | result |
        |      10 |       9 |     19 |
        |     -10 |       4 |     -6 |
        |      15 |      -7 |      8 |

