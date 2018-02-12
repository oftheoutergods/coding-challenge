Feature: presentation
    Scenario Outline: Presents a number
    Given I have entered a <number>
    When I present
    Then the present should be <result>

    Examples:
        | number | result |
        |     19 | X = 19 |
        |     -6 | X = -6 |
        |     8  | X = 8  |