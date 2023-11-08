from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World! This is a message displayed on the web application.'

if __name__ == '__main__':
    app.run(debug=True)
