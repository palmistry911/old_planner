import os

class Task:
    def __init__(self, description):
        self.description = description
        self.completed = False

    def __str__(self):
        if self.completed:
            return f"~~{self.description}~~"
        else:
            return f"**{self.description}**"


class TaskPlanner:
    def __init__(self):
        self.tasks = []

    def add_task(self, description):
        if len(description) < 2:
            print("Ошибка: задача должна содержать не менее двух символов.")
            return False
        self.tasks.append(Task(description))
        return True

    def view_tasks(self):
        if not self.tasks:
            print("Здесь будет отображаться список ваших задач.")
        else:
            for index, task in enumerate(self.tasks, 1):
                print(f"{index}. {task}")

    def mark_task_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            if self.tasks[task_index].completed:
                print("Эта задача уже выполнена.")
            else:
                self.tasks[task_index].completed = True
                print("Задача помечена как выполненная.")
        else:
            print("Ошибка: неверный индекс задачи.")

    def remove_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            del self.tasks[task_index]
            print("Задача удалена.")
        else:
            print("Ошибка: неверный индекс задачи.")

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as file:
            for task in self.tasks:
                file.write(f"{task.description} | {'completed' if task.completed else 'not completed'}\n")
        print(f"Задачи сохранены в файл {filename}.")


def main():
    planner = TaskPlanner()
    print("\n Добро пожаловать в простой текстовый планировщик задач!")

    while True:
        print("\n1. Добавить задачу")
        print("2. Просмотреть задачи")
        print("3. Отметить задачу как выполненную")
        print("4. Удалить задачу")
        print("5. Сохранить задачи в файл")
        print("6. Выйти")
        choice = input("Выберите номер действия: ")

        if choice == '1':
            task_description = input("Введите описание задачи: ")
            if not planner.add_task(task_description):
                continue
        elif choice == '2':
            planner.view_tasks()
        elif choice == '3':
            try:
                task_index = int(input("Введите номер задачи для отметки как выполненной: ")) - 1
                planner.mark_task_completed(task_index)
            except ValueError:
                print("Ошибка: введите число.")
        elif choice == '4':
            try:
                task_index = int(input("Введите номер задачи для удаления: ")) - 1
                planner.remove_task(task_index)
            except ValueError:
                print("Ошибка: введите число.")
        elif choice == '5':
            planner.save_to_file()
        elif choice == '6':
            print("Завершаем программу. Сохраненные задачи будут автоматически записаны файл")
            break
        else:
            print("Ошибка: неверный выбор. Пожалуйста, выберите из предложенных вариантов.")

if __name__ == "__main__":
    main()
