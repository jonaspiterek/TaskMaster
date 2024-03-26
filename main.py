from abc import ABC, abstractmethod


class Task(ABC):
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

        @abstractmethod
        def display_detes(self):
            pass

        def complete_task(self):
            self.completed = True


class Observer(ABC):
    @abstractmethod
    def update(self, task):
        pass


class NormalTask(Task):
    def display_detes(self):
        status = "Completed" if self.completed else "Pending"
        print(f"Title: {self.title}\nDescription: {self.description}\nStatus: {status}")


class HighPrioTask(Task):
    def display_detes(self):
        status = "Completed" if self.completed else "Pending"
        print(
            f"This is a high priority task!\nTitle: {self.title}\nDescription: {self.description}\nStatus: {status}"
        )


class TaskObserver(Observer):
    def update(self, task):
        print(f"Task {task.title} has been updated!")


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.observers = []

    def create_task(self):
        title = input("Title: ")
        description = input("Description: ")
        isHighPrio = input("Does this new task has hight priority? (y/N): ")

        if (
            isHighPrio == "Y"
            or isHighPrio == "y"
            or isHighPrio == "Yes"
            or isHighPrio == "yes"
        ):
            newHighPrioTask = HighPrioTask(title=title, description=description)
            self.tasks.append(newHighPrioTask)
            self.notify_observers(newNormalTask)
        elif (
            isHighPrio == "N"
            or isHighPrio == "n"
            or isHighPrio == "No"
            or isHighPrio == "no"
        ):
            newNormalTask = NormalTask(title=title, description=description)
            self.tasks.append(newNormalTask)
            self.notify_observers(newNormalTask)

    def list_tasks(self):
        print("----- Tasks -----")
        if len(self.tasks) > 0:
            for task in self.tasks:
                task.display_detes()
        else:
            print("There are no tasks.")

    def complete_task(self, task):
        taskToComplete = int(input("Enter task to complete: "))

        for task in self.tasks:
            if task == taskToComplete:
                taskToComplete.completed

            else:
                print("")

    def attach_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, task):
        for observer in self.observers:
            observer.update(task)


class main:
    task_manager = TaskManager()

    task_observer = TaskObserver()
    task_manager.attach_observer(task_observer)

    while True:
        print("1. Create Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                task_manager.create_task()

            case 2:
                task_manager.list_tasks()

            case 3:
                pass

            case 4:
                break

            case _:
                print("Your Input is not a valid option! Try again.")


main()
