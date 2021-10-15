from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["POST"])
def hello_world():
    return {'test': 'test'}

if __name__ == '__main__':
    app.run(port=5000)
