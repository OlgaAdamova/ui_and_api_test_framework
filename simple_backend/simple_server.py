import re
import sqlite3

from flask import Flask, request
from flask_restx import Api, Resource, fields


app = Flask(__name__)
api = Api(app, version='1.0', title='User API', description='Simple User API', )

# SQLite database setup
conn = sqlite3.connect('users.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        email TEXT NOT NULL
    )
''')
conn.commit()
conn.close()


# Validate email format
def is_valid_email(email):
    email_regex = re.compile(r"[^@]+@[^@]+\.[^@]+")
    return bool(re.match(email_regex, email))


# Namespace
ns = api.namespace('users', description='User operations')

# User Model
user_model = api.model('User', {
    'id': fields.Integer(readonly=True, description='The user ID'),
    'first_name': fields.String(required=True, description='The first name of the user'),
    'last_name': fields.String(required=True, description='The last name of the user'),
    'email': fields.String(required=True, description='The email of the user')
})


# User Resource
@ns.route('/<int:user_id>')
@ns.response(404, 'User not found')
@ns.param('user_id', 'The user identifier')
class UserResource(Resource):
    @ns.doc('get_user')
    @ns.marshal_with(user_model)
    def get(self, user_id):
        """
        Get a user by ID
        """
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE id = ?', (user_id,))
        user = cursor.fetchone()
        conn.close()

        if user:
            user_data = {
                'id': user[0],
                'first_name': user[1],
                'last_name': user[2],
                'email': user[3]
            }
            return user_data
        else:
            api.abort(404, 'User not found')


# Create user endpoint
@ns.route('/')
class CreateUserResource(Resource):
    @ns.doc('create_user')
    @ns.expect(user_model)
    @ns.marshal_with(user_model, code=201)
    def post(self):
        """
        Create a new user
        """
        data = request.json

        # Check if all required fields are present
        if 'first_name' not in data or 'last_name' not in data or 'email' not in data:
            api.abort(400, 'All fields (first_name, last_name, email) are required.')

        first_name = data['first_name']
        last_name = data['last_name']
        email = data['email']

        # Validate email format
        if not is_valid_email(email):
            api.abort(400, 'Invalid email format.')

        # Insert user into the database
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (first_name, last_name, email) VALUES (?, ?, ?)',
                       (first_name, last_name, email))
        user_id = cursor.lastrowid
        conn.commit()
        conn.close()

        user_data = {
            'id': user_id,
            'first_name': first_name,
            'last_name': last_name,
            'email': email
        }

        return user_data, 201


if __name__ == '__main__':
    app.run(debug=True)
