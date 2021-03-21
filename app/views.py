from flask import jsonify
from app import app

data = ["task1", "task2", "task3", "task4", "task5", "task6", "task7", "task8"]


@app.route('/tasks', methods=['GET'])
def get_tasks():
    app.logger.info('get request from /tasks')
    return jsonify({"data": data})
