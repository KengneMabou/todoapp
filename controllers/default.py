from core.app_init import app
from models.todo import Todo
from flask import Flask, render_template, request, redirect, url_for
from models.sqlalchemy_init import db
from flask import abort, jsonify
import sys


@app.route('/todos/<todo_id>/delete', methods=['DELETE'])
def delete_todo(todo_id):
    error = False
    resp_data = {}
    try:
        # description = request.form.get('description', '')
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
        resp_data['id'] = todo_id
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if error:
            abort(400)
        else:
            return jsonify(resp_data)
            # return redirect(url_for('index'))

@app.route('/todos/<todo_id>/set-completed', methods=['POST'])
def todo_set_completed(todo_id):
    error = False
    resp_data = {}
    try:
        # description = request.form.get('description', '')
        completed = request.get_json()['completed']
        todo = Todo.query.get(todo_id)
        todo.completed = completed
        db.session.commit()
        resp_data['id'] = todo.id
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if error:
            abort(400)
        else:
            # return jsonify(resp_data)
            return redirect(url_for('index'))

@app.route('/todos/create', methods=['POST'])
def create_todo():
    error = False
    resp_data = {}
    try:
        # description = request.form.get('description', '')
        description = request.get_json()['description']
        todo = Todo(description=description,completed=False, list_id=1)
        db.session.add(todo)
        db.session.commit()
        resp_data['description'] = todo.description
    except:
        error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
        if error:
            abort(400)
        else:
            return jsonify(resp_data)
            # return redirect(url_for('index'))

@app.route('/')
def index():
    return render_template('index.html', data=Todo.query.order_by('id').all())