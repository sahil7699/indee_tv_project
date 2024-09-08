Feature: Book a hotel on Expedia

  Scenario: User books a single-day stay in Bangalore
    Given the user opens the Expedia website
    When the user selects "Hotels" and searches for hotels in "Bangalore"
    And picks the 2nd hotel from the search results
    And extracts the room types and stores the room types in a JSON file