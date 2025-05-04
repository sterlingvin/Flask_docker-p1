from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []  # simple in-memory task list

@app.route('/')
def home():
    return "📝 ToDo List is Ready!"

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos), 200

@app.route('/todos', methods=['POST'])
def add_todo():
    data = request.get_json()
    todo = {
        "id": len(todos) + 1,
        "task": data.get("task", ""),
        "done": False
    }
    todos.append(todo)
    return jsonify(todo), 201