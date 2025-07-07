Feature: Manage the to-do list

  # Scenario 1: Adding a task
  # This scenario tests adding a task to the to-do list.
  # It ensures that after adding the task, it appears in the to-do list.
  Scenario: Adding a task
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with description "Buy milk and bread", due date "2025-07-10", and priority "High"
    Then the to-do list should contain "Buy groceries"

  # Scenario 2: Listing all tasks
  # This scenario tests listing all tasks in the to-do list.
  # It ensures that all tasks in the list are displayed correctly.
  Scenario: Listing all tasks in the to-do list
    Given the to-do list has a task "Buy groceries"
    When the user lists all tasks
    Then the task "Buy groceries" should be listed

  # Scenario 3: Marking a task as completed
  # This scenario tests marking a task as completed.
  # It ensures that a task can be marked correctly as completed.
  Scenario: Marking a task as completed
    Given the to-do list has a task "Buy groceries"
    When the user marks the task "Buy groceries" as completed
    Then the task "Buy groceries" should be marked as completed

  # Scenario 4: Clearing the entire to-do list
  # This scenario tests clearing all tasks in the to-do list.
  # It ensures that all tasks are removed when the list is cleared.
  Scenario: Clearing the entire to-do list
    Given the to-do list has tasks
    When the user clears the to-do list
    Then the to-do list should be empty
  
  # Scenario 5: Updating a task
  # This scenario tests updating a task in the to-do list.
  # It ensures that a task's title, description, due date, or priority can be updated successfully.
  Scenario: Updating a task
    Given the to-do list has a task "Buy groceries"
    When the user updates the task "Buy groceries" with new title "Buy groceries and veggies", new description "Buy milk, bread, and vegetables", new due date "2025-07-12", and new priority "Low"
    Then the to-do list should contain "Buy groceries and veggies"

  # Scenario 6: Deleting a task
  # This scenario tests deleting a task from the to-do list.
  # It ensures that a task can be removed from the list successfully.
  Scenario: Deleting a task
    Given the to-do list has a task "Buy groceries"
    When the user deletes the task "Buy groceries"
    Then the to-do list should not contain "Buy groceries"