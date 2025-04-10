class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        status = "Выполнено" if self.completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def show_pending_tasks(self):
        pending_tasks = [task for task in self.tasks if not task.completed]
        if pending_tasks:
            for task in pending_tasks:
                print(task)
        else:
            print("Нет невыполненных задач.")

    def mark_task_completed(self, description):
        for task in self.tasks:
            if task.description == description:
                task.mark_completed()
                print(f"Задача '{description}' отмечена как выполненная.")
                return
        print(f"Задача '{description}' не найдена.")

# Пример работы с задачами
manager = TaskManager()
manager.add_task(Task("Купить продукты", "2025-02-10"))
manager.add_task(Task("Сдать проект", "2025-02-15"))
manager.show_pending_tasks()
manager.mark_task_completed("Купить продукты")
manager.show_pending_tasks()


