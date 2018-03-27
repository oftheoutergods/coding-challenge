Feature: presentation
    Scenario Outline: present a number
        Given a <number>
        When I present
        Then the result should be <result>

    Examples:
        | number | result          |
        |    -26 | DIFERENCA = -26 |
        |    -56 | DIFERENCA = -56 |
        |     86 | DIFERENCA = 86  |
