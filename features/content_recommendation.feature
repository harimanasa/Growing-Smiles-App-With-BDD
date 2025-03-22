
Feature: Generate recommendations across multiple content types

  Scenario: Recommend video and article formats
    Given the user interacts with "Generative AI for Developers"
    When the user requests multi-format content
    Then the system should return both videos and articles matching the interest topic

  Scenario: Filter recommendations by preferred content type
    Given the user prefers "video" content
    When a recommendation is generated
    Then only video content links should be included
