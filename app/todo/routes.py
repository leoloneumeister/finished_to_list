from flask import Blueprint, render_template, redirect, url_for, request, current_app
from .models import Todo

blueprint = Blueprint('todo', __name__)


@blueprint.route('/todo-list')
def show_todos():
    page_number = request.args.get('page', 1, type=int)
    all_todo = Todo.query.paginate(
            page=page_number,
            per_page=current_app.config['TODOS_PER_PAGE']
            )
    return render_template('tasks.html', todos=all_todo)


@blueprint.route('/create-todo-form')
def create_todo_form():
    return render_template('create_task.html')


@blueprint.post('/create-todo')
def create_todo():
    new_todo = Todo(
            title=request.form.get('title'),
            content=request.form.get('content')
            )
    new_todo.save()
    return redirect(url_for('todo.show_todos'))


@blueprint.post('/delete-todo')
def delete_todo():
    todo_id = request.form.get('id')
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.delete()
    return redirect(url_for('todo.show_todos'))


@blueprint.get('/edit-todo-form/<id>')
def edit_todo_form(id):
    todo = Todo.query.filter_by(id=id).first()
    return render_template('edit_todo.html', todo=todo)


@blueprint.post('/edit-todo')
def edit_todo():
    todo_id = request.form.get('id')
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.title = request.form.get('title')
    todo.content = request.form.get('content')
    todo.save()

    return redirect(url_for('todo.show_todos'))


@blueprint.route('/showtodo/<id>')
def show_todo(id):
    todo = Todo.query.filter_by(id=id).first()
    return render_template('show.html', todo=todo)
