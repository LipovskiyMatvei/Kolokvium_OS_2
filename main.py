from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    status = db.Column(db.String(100), default="todo")

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "status": self.status
        }

with app.app_context():
    db.create_all()

@app.route('/tasks', methods = ['POST'])
def create_task():

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Запрос пустой или не является JSON"}), 400

    if 'title' not in data:
        return jsonify({"error": "Отсутствует обязательное поле 'title'"}), 400

    if not isinstance(data['title'], str):
        return jsonify({"error": "Поле 'title' должно быть строкой"}), 400

    if not data['title'].strip():
        return jsonify({"error": "Поле 'title' не может быть пустым"}), 400

    new_task = Task(
        title=data['title'],
        description=data.get('description', ""),
        status="todo"
    )
    db.session.add(new_task)
    db.session.commit()

    return jsonify(new_task.to_dict()), 201

@app.route('/tasks', methods=['GET'])
def get_tasks():
    all_tasks = Task.query.all()

    return jsonify([task.to_dict() for task in all_tasks])


@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({"error": "Not found"}), 404

    return jsonify(task.to_dict())

@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task is None:
        return jsonify({"error": "Not found"}), 404

    db.session.delete(task)
    db.session.commit()

    return jsonify({"result": True}), 200

@app.route('/tasks/<int:task_id>', methods=['PUT', 'PATCH'])
def update_task(task_id):

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "No data"}), 400

    task = Task.query.get(task_id)
    if task is None:
        return jsonify({"error": "Not found"}), 404


    if 'title' in data:
        if not isinstance(data['title'], str) or not data['title'].strip():
            return jsonify({"error": "Title is required"}), 400
        task.title = data['title']

    if 'status' in data:
        allowed_status = ["to do", "done", "is_requiered"]
        if data['status'] not in allowed_status:
            return jsonify({"error": f"Status should be one of {allowed_status}"}), 400
        task.status = data['status']

    if 'description' in data:
        task.description = data['description']


    db.session.commit()

    return jsonify(task.to_dict()), 200

if __name__ == '__main__':
    app.run(debug=True)
