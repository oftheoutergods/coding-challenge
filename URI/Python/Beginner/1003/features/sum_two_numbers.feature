Feature: sum_two_numbers
    Scenario Outline: Add any two numbers
        Given I have entered <number1>
        And I have also entered <number2>
        When I sum
        Then the sum should be <result>

    Examples:
        | number1 | number2 | result |
        |      30 |      10 |     40 |
        |     -30 |      10 |    -20 |
        |       0 |       0 |      0 |

