from flask import Flask, request, jsonify
import sqlite3

app = Flask(__name__)
DATABASE = 'users.db'

# Helper function to get a database connection
def get_db_connection():
    try:
        conn = sqlite3.connect(DATABASE)
        conn.row_factory = sqlite3.Row
        return conn
    except sqlite3.Error as e:
        return None

# Initialize the database
def init_db():
    with app.app_context():
        conn = get_db_connection()
        if conn is not None:
            try:
                conn.execute('''
                    CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        email TEXT NOT NULL
                    )
                ''')
                conn.commit()
            except sqlite3.Error as e:
                print(f"Database error: {e}")
            finally:
                conn.close()
        else:
            print("Failed to connect to the database.")

# Error handler for 400 Bad Request
@app.errorhandler(400)
def bad_request(error):
    return jsonify({"error": "Bad Request", "message": "Invalid input or missing data"}), 400

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Not Found", "message": "Resource not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_server_error(error):
    return jsonify({"error": "Internal Server Error", "message": "Something went wrong on the server"}), 500

# Create a new user
@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()

    # Check if the request contains valid JSON
    if not data:
        return jsonify({"error": "Bad Request", "message": "No data provided"}), 400

    # Check if required fields are present
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"error": "Bad Request", "message": "Missing name or email"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Internal Server Error", "message": "Failed to connect to the database"}), 500

    try:
        conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
        conn.commit()
        return jsonify({"message": "User created successfully"}), 201
    except sqlite3.Error as e:
        return jsonify({"error": "Database Error", "message": str(e)}), 500
    finally:
        conn.close()

# Retrieve all users
@app.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Internal Server Error", "message": "Failed to connect to the database"}), 500

    try:
        users = conn.execute('SELECT * FROM users').fetchall()
        return jsonify([dict(user) for user in users])
    except sqlite3.Error as e:
        return jsonify({"error": "Database Error", "message": str(e)}), 500
    finally:
        conn.close()

# Retrieve a single user by ID
@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Internal Server Error", "message": "Failed to connect to the database"}), 500

    try:
        user = conn.execute('SELECT * FROM users WHERE id = ?', (id,)).fetchone()
        if user is None:
            return jsonify({"error": "Not Found", "message": "User not found"}), 404
        return jsonify(dict(user))
    except sqlite3.Error as e:
        return jsonify({"error": "Database Error", "message": str(e)}), 500
    finally:
        conn.close()

# Update a user's name or email
@app.route('/users/<int:id>', methods=['PUT'])
def update_user(id):
    data = request.get_json()

    # Check if the request contains valid JSON
    if not data:
        return jsonify({"error": "Bad Request", "message": "No data provided"}), 400

    # Check if required fields are present
    name = data.get('name')
    email = data.get('email')
    if not name or not email:
        return jsonify({"error": "Bad Request", "message": "Missing name or email"}), 400

    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Internal Server Error", "message": "Failed to connect to the database"}), 500

    try:
        conn.execute('UPDATE users SET name = ?, email = ? WHERE id = ?', (name, email, id))
        conn.commit()
        return jsonify({"message": "User updated successfully"})
    except sqlite3.Error as e:
        return jsonify({"error": "Database Error", "message": str(e)}), 500
    finally:
        conn.close()

# Delete a user
@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    conn = get_db_connection()
    if conn is None:
        return jsonify({"error": "Internal Server Error", "message": "Failed to connect to the database"}), 500

    try:
        conn.execute('DELETE FROM users WHERE id = ?', (id,))
        conn.commit()
        return jsonify({"message": "User deleted successfully"})
    except sqlite3.Error as e:
        return jsonify({"error": "Database Error", "message": str(e)}), 500
    finally:
        conn.close()

if __name__ == '__main__':
    init_db()
    app.run(debug=True)