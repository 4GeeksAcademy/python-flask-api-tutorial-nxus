from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Global variable holding the list of todos
todos = [
    {"label": "My first task", "done": False},
    {"label": "My second task", "done": False}
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify(todos)

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body:", request_body)

    if not request_body or 'label' not in request_body:
        abort(400)  # Bad request if label is missing

    new_todo = {
        'label': request_body['label'],
        'done': request_body.get('done', False)  # Default to False if not provided
    }
    todos.append(new_todo)

    return jsonify(todos), 200  # Return updated todos with status code 201

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    
    if position < 0 or position >= len(todos):
        abort(404)  # Not found if position is invalid
    
    todos.pop(position)  # Remove the todo at the specified position
    return jsonify(todos)  # Return updated list of todos

if __name__ == '__main__':
    app.run(debug=True)
