class Task:
    def __init__(self, title, description, due_date, priority):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def update_task(self, title=None, description=None, due_date=None, priority=None):
        if title:
            self.title = title
        if description:
            self.description = description
        if due_date:
            self.due_date = due_date
        if priority:
            self.priority = priority

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"Task: {self.title}, Due: {self.due_date}, Priority: {self.priority}, Status: {status}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, due_date, priority):
        task = Task(title, description, due_date, priority)
        self.tasks.append(task)

    def list_tasks(self):
        if not self.tasks:
            return []
        return [str(task) for task in self.tasks]

    def mark_task_completed(self, title):
        for task in self.tasks:
            if task.title == title:
                task.mark_completed()
                return f"Task '{title}' marked as completed."
        return f"Task '{title}' not found."

    def clear_all_tasks(self):
        self.tasks.clear()
        return "All tasks have been cleared."

    def update_task(self, title, new_title=None, description=None, due_date=None, priority=None):
        for task in self.tasks:
            if task.title == title:
                task.update_task(new_title, description, due_date, priority)
                return f"Task '{title}' updated."
        return f"Task '{title}' not found."

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                return f"Task '{title}' deleted."
        return f"Task '{title}' not found."