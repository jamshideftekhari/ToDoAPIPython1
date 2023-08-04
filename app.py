from flask import Flask

print("hello world")
app = Flask(__name__)

@app.route('/')
def index():
    return "Hello task ! i am her"


if __name__ == '__main__':
    app.run(debug=True, host='localhost', port=5000)
