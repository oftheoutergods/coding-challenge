Feature: average
    Scenario Outline: calculates the average
        Given a <number1>
        And a another <number2>
	And a third <number3>
        When I calculate
        Then the average should be <result>

    Examples:
        | number1 | number2 | number3 | result |
        |     5.0 |     6.0 |     7.0 |    6.3 |
        |     5.0 |    10.0 |    10.0 |    9.0 |
        |    10.0 |    10.0 |     5.0 |    7.5 |
