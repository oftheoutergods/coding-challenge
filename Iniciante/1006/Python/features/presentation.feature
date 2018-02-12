Feature: presentation
    Scenario Outline: present a number
        Given a <number>
        When I present
        Then the result should be <result>

    Examples:
        | number | result      |
        |    6.3 | MEDIA = 6.3 |
        |    9.0 | MEDIA = 9.0 |
        |    7.5 | MEDIA = 7.5 |
