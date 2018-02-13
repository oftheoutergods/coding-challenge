Feature: difference
    Scenario Outline: calculate difference
        Given a first <number1>
        And a second <number2>
        And a third <number3>
        And a fourth <number4>
        When I calculate
        Then the result should be <result>

    Examples:
        | number1 | number2 | number3 | number4 | result |
        | 5       | 6       | 7       | 8       | -26    |
        | 0       | 0       | 7       | 8       | -56    |
        | 5       | 6       | -7      | 8       | 86     |
