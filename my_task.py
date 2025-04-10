class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_done = False

    def mark_done(self):
        self.is_done = True

    def __str__(self):
        status = "✅ Выполнено" if self.is_done else "❌ Не выполнено"
        return f"{self.description} (до {self.deadline}) - {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, description, deadline):
        task = Task(description, deadline)
        self.tasks.append(task)

    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
        else:
            print("Неверный номер задачи.")

    def show_pending_tasks(self):
        print("\n📋 Невыполненные задачи:")
        for i, task in enumerate(self.tasks):
            if not task.is_done:
                print(f"{i + 1}. {task}")

    def show_all_tasks(self):
        print("\n📚 Все задачи:")
        for i, task in enumerate(self.tasks):
            print(f"{i + 1}. {task}")


# === Интерфейс ===

manager = TaskManager()

while True:
    print("\nВыберите действие:")
    print("1 - Добавить задачу")
    print("2 - Отметить задачу выполненной")
    print("3 - Показать невыполненные задачи")
    print("4 - Показать все задачи")
    print("5 - Выйти")

    choice = input("Ваш выбор: ")

    if choice == '1':
        desc = input("Описание задачи: ")
        deadline = input("Срок выполнения (например, 2025-04-15): ")
        manager.add_task(desc, deadline)

    elif choice == '2':
        manager.show_all_tasks()
        number = int(input("Введите номер задачи, которую вы выполнили: "))
        manager.mark_task_done(number - 1)

    elif choice == '3':
        manager.show_pending_tasks()

    elif choice == '4':
        manager.show_all_tasks()

    elif choice == '5':
        print("Завершение работы.")
        break

    else:
        print("Неверный ввод. Повторите попытку.")
