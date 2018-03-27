Feature: circle_area
    Scenario Outline: determines the area of circle
        Given a <number>
        When I computes the area
        Then the area should be <result>

    Examples:
        | number |     result |
        |   2.00 |    12.5664 |
        | 100.64 | 31819.3103 |
        | 150.00 | 70685.7750 |
