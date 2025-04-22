from flask import Flask, request, jsonify
from .models import TodoModel

def create_app():
    app = Flask(__name__)
    todo_model = TodoModel()

    @app.route('/todos', methods=['GET'])
    def get_todos():
        todos = todo_model.get_all_todos()
        return jsonify(todos)

    @app.route('/todos', methods=['POST'])
    def create_todo():
        data = request.get_json()
        todo_id = todo_model.create_todo(
            data.get('title'),
            data.get('description')
        )
        return jsonify({'id': todo_id}), 201

    @app.route('/todos/<int:todo_id>', methods=['GET'])
    def get_todo(todo_id):
        todo = todo_model.get_todo(todo_id)
        if todo:
            return jsonify(todo)
        return jsonify({'error': 'Todo not found'}), 404

    @app.route('/todos/<int:todo_id>', methods=['PUT'])
    def update_todo(todo_id):
        data = request.get_json()
        todo = todo_model.update_todo(
            todo_id,
            data.get('title'),
            data.get('description'),
            data.get('completed', False)
        )
        if todo:
            return jsonify(todo)
        return jsonify({'error': 'Todo not found'}), 404

    @app.route('/todos/<int:todo_id>', methods=['DELETE'])
    def delete_todo(todo_id):
        todo_model.delete_todo(todo_id)
        return jsonify({'message': 'Todo deleted'})

    return app