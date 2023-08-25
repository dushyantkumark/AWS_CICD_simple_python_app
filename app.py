from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This is AWS CICD Pipeline Automation'

if __name__ == '__main__':
    app.run()

