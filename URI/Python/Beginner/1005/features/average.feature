Feature: average
    Scenario Outline: calculates the average
        Given a <number1>
        And a another <number2>
        When I calculate
        Then the average should be <result>

    Examples:
        | number1 | number2 |   result |
        |     5.0 |     7.1 |  6.43182 |
        |     0.0 |     7.1 |  4.84091 |
        |    10.0 |    10.0 | 10.00000 |
