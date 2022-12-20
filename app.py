from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/users', methods=['GET'])
def get_users():
    # Tạo một danh sách người dùng mẫu
    users = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
    return jsonify(users)

if __name__ == '__main__':
    app.run()