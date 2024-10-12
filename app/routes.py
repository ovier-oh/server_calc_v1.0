from flask import Blueprint, request, jsonify, render_template 

main = Blueprint('main', __name__)

# Diccionario de usuarios 
users = {
    "Admin": {"password": "password123", "role":"admin"}, 
    "user1": {"password": "abc123", "role": "user"}, 
    "user2": {"password": "password123", "role": "user"}
}

@main.route('/')
def index():
    return render_template('admin.html')

@main.route('/users', methods=['GET'])
def get_user():
    return jsonify(users) 

@main.route('/add_user', methods=['POST'])
def add_user():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    role = data.get('role') 
    
    if username in users:
        return jsonify({"status": "fail", "message": "User already exists"})
    
    users[username] = {"password": password, "role": role}
    return jsonify({"status": "success", "message": "User add successfully"})

@main.route('/delete_user', methods=['POST'])
def delete_user():
    data = request.json
    username = data.get('username')
    
    if username in users:
        del users[username]
        return jsonify({"status": "success", "message": "User deleted successfully"})
    else:
        return jsonify({"status": "fail", "message": "User not found"})
    