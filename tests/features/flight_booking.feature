Feature: Book a flight on Expedia

  Scenario: User books a one-way flight from Bangalore to Delhi
    Given the user opens the Expedia website
    When the user selects "Flights" and chooses a one-way trip from "Bangalore" to "Delhi"
    And sorts the results by "Duration (shortest)"
    And selects the cheapest flight available
    Then the user proceeds to checkout
    And enters the following details: "sahil", "kumar", "sahil@test.com", "1111111111", "downtown", "metrocity", "111111", "AAAAA0000A"
    And verifies the error message for missing credit card details
    And captures the error text
