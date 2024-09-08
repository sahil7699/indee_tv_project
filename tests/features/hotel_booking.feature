Feature: Book a hotel on Expedia

  Scenario: User books a single-day stay in Bangalore
    Given the user opens the Expedia website
    When the user selects "Hotels" and searches for hotels in "Bangalore"
    And selects check-in date as "3 days from today" and check-out as "4 days from today"
    And picks the 2nd hotel from the search results
    Then extracts the room types and stores the room types in a JSON file
