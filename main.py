from flask import Flask
import os

app = Flask(__name__)

port = int(os.environ.get('PORT', 9999))
print (port)


@app.route("/")
def hello_world():
    return "<p>Hello, Cats!</p>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)