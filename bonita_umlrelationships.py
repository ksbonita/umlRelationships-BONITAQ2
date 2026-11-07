from abc import ABC, abstractmethod
from enum import Enum


# inheritance (is-a)
class Vehicle:
    def __init__(self, brand: str):
        self.brand = brand


# car inherits from vehicle
class Car(Vehicle):
    def honk(self):
        return f"{self.brand} car says Beep!"


def demo_inheritance():
    print("=== Inheritance (Is-a) ===")
    my_car = Car("Toyota")
    print(my_car.honk())


# realization / impl (implements)
class Notifier(ABC):
    @abstractmethod
    def send(self, message: str) -> bool:
        pass


# emailnotifier realizes notifier
class EmailNotifier(Notifier):
    def send(self, message: str) -> bool:
        print(f"Sending email: {message}")
        return True


def demo_realization():
    print("\n=== Realization (Implements) ===")
    notifier = EmailNotifier()
    status = notifier.send("Meeting at 3 PM")
    print(f"Send Status: {status}")


# composition (strong has-a)
class Lesson:
    def __init__(self, topic: str):
        self.topic = topic


class Course:
    def __init__(self, title: str):
        self.title = title
        # course makes and owns these lessons
        self.lessons = [Lesson("Variables"), Lesson("Loops"), Lesson("Functions")]


def demo_composition():
    print("\n=== Composition (Strong Has-a) ===")
    python_course = Course("Intro to Python")
    for lesson in python_course.lessons:
        print(f"Lesson created: {lesson.topic}")
    # if course is deleted, lessons go too


# aggregation (weak has-a)
class Player:
    def __init__(self, name: str):
        self.name = name

    def __del__(self):
        print(f"Player object destroyed: '{self.name}'")


class Team:
    def __init__(self, players: list[Player] = None):
        # team takes players that already exist
        self.players = players if players else []

    def __del__(self):
        print("Team object destroyed.")


def demo_aggregation():
    print("\n=== Aggregation (Weak Has-a) ===")
    # players made outside first, so they exist w/o a team
    player1 = Player("Messi")
    player2 = Player("Ronaldo")

    # passed into the team
    my_team = Team([player1, player2])
    print(f"Team roster: {[p.name for p in my_team.players]}")

    print("\nExecuting: del my_team")
    del my_team

    print("\nChecking variable accessibility after container deletion:")
    print(f"Still active in memory -> player1: {player1.name}")
    print(f"Still active in memory -> player2: {player2.name}")
    # my_team is gone but players live on


# association (knows-a)
class Author:
    def __init__(self, name: str):
        self.name = name
        self.articles = []  # tracks articles


class Article:
    def __init__(self, article_id: int, author: Author):
        self.article_id = article_id
        self.author = author  # ref back to the author
        author.articles.append(self)


def demo_association():
    print("\n=== Association (Knows-a) ===")
    bob = Author("Bob")

    article_1 = Article(1, bob)
    article_2 = Article(2, bob)

    print(f"Author Profile: {bob.name}")
    print("Linked articles tracked inside Author list:")
    for a in bob.articles:
        print(f"  - Article ID: {a.article_id}")

    print(f"\nArticle #1 lookup -> Written by: {article_1.author.name}")


# dependency (uses-a)
class Oven:
    def heat(self, dish: str):
        print(f"Baking: {dish}")


class Chef:
    def __init__(self, name: str):
        self.name = name

    # chef needs an oven only during this call
    def cook(self, dish: str, oven: Oven):
        oven.heat(dish)


def demo_dependency():
    print("\n=== Dependency (Uses-a) ===")
    kitchen_oven = Oven()
    chef = Chef("Gordon")

    chef.cook("Lasagna", kitchen_oven)


# combined: enum + interface + abs class
class TaskStatus(Enum):
    TODO = 1
    DOING = 2
    DONE = 3


class Remindable(ABC):
    @abstractmethod
    def set_reminder(self):
        pass


class Task(ABC):
    def __init__(self, title: str):
        self.title = title
        self.status = TaskStatus.TODO  # enum as attr type

    def show_details(self):
        print(self.title, self.status.name)

    @abstractmethod
    def perform_task(self):
        pass


# extends task, implements remindable
class Homework(Task, Remindable):
    def perform_task(self):
        print("Solving homework problems.")

    def set_reminder(self):
        print(f"{self.title} reminder set.")


def demo_combined():
    print("\n=== Combined: Enum + Interface + Abstract Class ===")
    task = Homework("Math Homework")
    task.show_details()
    task.perform_task()
    task.set_reminder()


# run
if __name__ == "__main__":
    demo_inheritance()
    demo_realization()
    demo_composition()
    demo_aggregation()
    demo_association()
    demo_dependency()
    demo_combined()
