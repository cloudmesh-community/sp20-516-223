from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/student/rahul')
def rahul_information():
    data = {
        'firstname': 'Rahul',
        'lastname': 'D',
        'university': 'IUy',
        'email': 'rahd@example.com'
        }
    return jsonify(**data)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)
