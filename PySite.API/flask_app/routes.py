from flask_app import app
from flask import jsonify, request

# Add initial User
current_id = 0
users = {str(current_id): {"name": "Diana"}}


@app.route("/api/users", methods=["GET", "POST"])
def handle_users():
    global current_id
    if request.method == "GET":
        return jsonify({"users": users})

    elif request.method == "POST":
        # Recieved new request to add a user
        try:
            data = request.get_json()
            print("printing the data recieved from frontend", data)
            current_id += 1
            users[str(current_id)] = data

            return jsonify({"message": "Users updated successfully"})
        except Exception as e:
            print("Error occured: ", e)
            return jsonify({"message": "could not update users"}), 500


@app.route("/api/users/<user_id>", methods=["GET", "PUT", "DELETE"])
def handle_user(user_id):
    global users
    # To update user
    if request.method == "PUT":
        try:
            data = request.get_json()
            users[str(user_id)] = (data)
            return jsonify({"message": "User updated successfully"})
        except Exception as e:
            print("Error occurred: ", e)
            return jsonify({"message": "Could not update user"}), 500
        # To delete user
    elif request.method == "DELETE":
        try:
            del users[str(user_id)]
            return jsonify({"message": "User deleted successfully"})
        except Exception as e:
            print("Error occurred: ", e)
            return jsonify({"message": "Could not delete user"}), 500

    if user_id in users:
        if request.method == "GET":
            return jsonify(users[user_id])
    else:
        return jsonify({"message": "User not found"}), 404
