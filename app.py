from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world! welcome to my flask app"



if __name__ == "__main__":
    app.run(debug=True)