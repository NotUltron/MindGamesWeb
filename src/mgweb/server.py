from flask import Flask, render_template, jsonify, request

# Structure
class Server:
    def __init__(self):
        self.flask = Flask(__name__)
        self.directories()
        self.requests()

    def directories(self):

        @self.flask.route('/')
        def index():
            return "Hello World"
    def requests(self):

        @self.flask.route('/api/')
        def ping():
            return jsonify({'status': 'ok'})
