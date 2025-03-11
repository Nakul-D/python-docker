from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "This is a simple Python application running on Docker in an EC2 instance"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
