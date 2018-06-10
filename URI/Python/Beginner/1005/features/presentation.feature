Feature: presentation
    Scenario Outline: present a number
        Given a <number>
        When I present
        Then the result should be <result>

    Examples:
        |   number | result           |
        |  6.43182 | MEDIA = 6.43182  |
        |  4.84091 | MEDIA = 4.84091  |
        | 10.00000 | MEDIA = 10.00000 |
