from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "hellp world"

@app.route("/test")
def test():
    return "test page"

if __name__ == "__main__":
    app.run()

def hello():
    print("hello")
