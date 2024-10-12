from flask import Flask, request, jsonify 

app = Flask(__name__)

# Diccionario de usuarios para propositos de ejemplos 
users = {
    "Admin": "password123", 
    "User1": "abc123",
    "user2":"password456"
}


@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    
    if username in users and users[username] == password:
        return jsonify({"status":"success", "message":"Login successful"})
    else:
        return jsonify({"status":"fail", "message":"Inalid username and/or password"})

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port=5000)