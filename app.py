from flask import Flask
from admin import admin_console

app = Flask(__name__)

app.register_blueprint(admin_console)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)