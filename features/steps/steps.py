from behave import given, when, then
from todo_list import TodoList, Task

todo_list = TodoList()

@given('the to-do list is empty')
def step_impl(context):
    global todo_list
    todo_list = TodoList()

@when('the user adds a task "{title}" with description "{description}", due date "{due_date}", and priority "{priority}"')
def step_impl(context, title, description, due_date, priority):
    todo_list.add_task(title, description, due_date, priority)

@then('the to-do list should contain "{title}"')
def step_impl(context, title):
    tasks = todo_list.list_tasks()
    assert any(title in task for task in tasks), f'Task "{title}" not found in the to-do list'

@given('the to-do list has a task "{title}"')
def step_impl(context, title):
    todo_list.add_task(title, "Sample description", "2025-07-10", "Medium") 

@given('the to-do list has tasks')
def step_impl(context):
    todo_list.add_task("Buy groceries", "Buy milk and bread", "2025-07-10", "High")
    todo_list.add_task("Do laundry", "Wash and fold clothes", "2025-07-11", "Medium")
    todo_list.add_task("Read book", "Read 50 pages", "2025-07-12", "Low")

@when('the user lists all tasks')
def step_impl(context):
    context.tasks = todo_list.list_tasks()

@then('the task "{title}" should be listed')
def step_impl(context, title):
    assert any(title in task for task in context.tasks), f'Task "{title}" not listed'

@when('the user marks the task "{title}" as completed')
def step_impl(context, title):
    result = todo_list.mark_task_completed(title)
    context.result = result

@then('the task "{title}" should be marked as completed')
def step_impl(context, title):
    tasks = todo_list.list_tasks()
    task = next((task for task in tasks if title in task), None)
    assert task and "Completed" in task, f'Task "{title}" not marked as completed'

@when('the user clears the to-do list')
def step_impl(context):
    context.message = todo_list.clear_all_tasks()

@then('the to-do list should be empty')
def step_impl(context):
    assert not todo_list.list_tasks(), "The to-do list is not empty"

@when('the user updates the task "{title}" with new title "{new_title}", new description "{description}", new due date "{due_date}", and new priority "{priority}"')
def step_impl(context, title, new_title, description, due_date, priority):
    todo_list.update_task(title, new_title, description, due_date, priority)

@when('the user deletes the task "{title}"')
def step_impl(context, title):
    result = todo_list.delete_task(title)
    context.result = result

@then('the to-do list should not contain "{title}"')
def step_impl(context, title):
    task_titles = [t.title if isinstance(t, Task) else t.split(',')[0].replace('Task: ', '').strip() for t in todo_list.tasks]
    assert title not in task_titles, f'Task "{title}" should not be in the to-do list'
