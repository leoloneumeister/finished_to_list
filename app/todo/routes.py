from flask import Blueprint, render_template, redirect
from .models import Todo

blueprint = Blueprint('todo', __name__)


@blueprint.route('/todo-list')
def show_todos():
    all_todo = Todo.query.all()
    return render_template('tasks.html', todos=all_todo)
