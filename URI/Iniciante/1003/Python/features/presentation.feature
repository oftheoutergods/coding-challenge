Feature: presentation
    Scenario Outline: Presents a number
    Given I have entered a <number>
    When I present
    Then the present should be <result>

    Examples:
        | number | result     |
        |     40 | SOMA = 40  |
        |    -20 | SOMA = -20 |
        |      0 | SOMA = 0   |
