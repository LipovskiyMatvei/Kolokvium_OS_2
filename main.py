from flask import Flask, jsonify, request


app = Flask(__name__)
tasks = [
    {
        "id": 1,
        "title": "Текстовая задача",
        "description": "Проверить, что работает",
        "status": "todo"
    }
]

current_id = 1


@app.route('/tasks', methods = ['POST'])
def create_task():
    global current_id
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Запрос пустой или не является JSON"}), 400




    if 'title' not in data:
        return jsonify({"error": "Отсутствует обязательное поле 'title'"}), 400

    if not isinstance(data['title'], str):
        return jsonify({"error": "Поле 'title' должно быть строкой"}), 400

    if not data['title'].strip():
        return jsonify({"error": "Поле 'title' не может быть пустым"}), 400


    new_task = {
        "id": current_id + 1,
        "title": data['title'],
        "description": data.get('description', ""),
        "status": "todo"
    }

    tasks.append(new_task)
    current_id += 1

    return jsonify(new_task), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():

    return jsonify(tasks)

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            return jsonify(task)

    return jsonify({"error": "Not found"}), 404


@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    for task in tasks:
        if task['id'] == task_id:
            tasks.remove(task)
            return jsonify({"result": True}), 200
    return jsonify({"error": "Not found"}), 404

@app.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "No data"}), 400

    if 'title' in data:
        if not isinstance(data['title'], str) or not data['title'].strip():
            return jsonify({"error": "Tittle is requiered"}), 400

    if 'status' in data:
        allowed_status = ["to do", "done", "is_requiered"]
        if data['status'] not in allowed_status:
            return jsonify({"error": f"Status should be one of {allowed_status}"}), 400

    for task in tasks:

        if task['id'] == task_id:

            task['title'] = data.get('title', task['title'])
            task['description'] = data.get('description', task['description'])
            task['status'] = data.get('status', task['status'])
            return jsonify(task), 200
    return jsonify({"error": "Not found"}), 404


if __name__ == '__main__':
    app.run(debug=True)
