from flask import Flask, request, jsonify

app = Flask(__name__)

students = [
    {'id':1,'name': 'Silvia','grade': 'A' },
    {'id':2,'name': 'Daniel','grade': 'B' },
    {'id':3,'name': 'Alonso','grade': 'C' }
]

@app.route('/students', methods=['POST'])
def create_student():
    data = request.get_json()
    if 'name' not in data or 'grade' not in data:
        return jsonify({"missing data"}), 400
    
    student = {
        "id":len(students) + 1,
        "name":data['name'],
        "grade": data['grade']
    }
    students.append(student)
    return jsonify(student), 201

@app.route('/students', methods=['GET'])
def get_students():
    return jsonify(students)

@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is not None:
        return jsonify(student)
    return jsonify({"student not found"}), 404

@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = next((s for s in students if s['id'] == student_id), None)
    if student is not None:
        student['name'] = data.get(('name'), student['name'])
        student['grade'] = data.get(('grade'), student['grade'])
        return jsonify(student)
    return jsonify({"student not found"}), 404

@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = next((s for s in students if s['id'] == student_id), None)
    if student is not None:
        students.remove(student)
        return jsonify({"student deleted"})
    return jsonify({"student not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)