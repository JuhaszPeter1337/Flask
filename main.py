from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Home page"

@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "John Doe",
        "age": 28,
        "email": "john.doe@example.com"
    }
    
    extra = request.args.get("extra")
    
    if extra:
        user_data["extra"] = extra
    
    return jsonify(user_data), 200

# curl -X POST http://127.0.0.1:5000/create-user/632 -H 'Content-Type: application/json' -d '{"name": "John Doe"}'
@app.route("/create-user/<user_id>", methods = ["POST"])
def create_user(user_id):
    id = user_id
    data = request.get_json()
    data["id"] = id
    
    return jsonify(data), 201

# curl -X GET http://127.0.0.1:5000/user
# curl -X POST http://127.0.0.1:5000/user
@app.route("/user", methods = ["POST", "GET"])
def user():
    if request.method == "GET":
        return "GET"
    else:
        return "POST"

if __name__ == "__main__":
    app.run(debug=True)
