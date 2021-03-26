from flask import Flask

app = Flask(__name__)

print("on start")

@app.route('/')
def hello():
    print("request received")
    return 'Hello'

if __name__ == '__main__':
    app.run(port=5001)