from flask import Flask
app = Flask(__name__)

@app.route('/')
def main():
    return "Future portfolio page"

if __name__ == '__main__':
    app.run()