from app.todo.models import Todo
from app.app import create_app


if __name__ == '__main__':
    app = create_app()
    app.app_context().push()


test_todos = {
        "Laundry": "Do the laundry before 13 oclock",
        "Programming": "Finish the handin before the deadline",
        "Trash": "Take the trash out tonight",
        "Clean": "Tidy up the room and clean the bathroom",
        "Bed": "Make the bed"
        }


def seed_todos():
    for key, value in test_todos.items():
        new_todo = Todo(title=key, content=value)
        new_todo.save()

seed_todos()
