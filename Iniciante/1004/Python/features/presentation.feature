Feature: presentation
    Scenario Outline: Presents a number
    Given I have entered a <number>
    When I present
    Then the present should be <result>

    Examples:
        | number | result      |
        |     27 | PROD = 27   |
        |   -300 | PROD = -300 |
        |      0 | PROD = 0    |
