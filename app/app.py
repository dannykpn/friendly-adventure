from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return '<h2>Hello from Techbase DSO</h2>'


if __name__ == "__main__":
    app.run(debug=True)