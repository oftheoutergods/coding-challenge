Feature: presentation
    Scenario Outline: presents the area of circle
        Given a <number>
        When I present
        Then the presentation should be <result>

    Examples:
        |     number | result       |
        |    12.5664 | A=12.5664    |
        | 31819.3103 | A=31819.3103 |
        | 70685.7750 | A=70685.7750 |
