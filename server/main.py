from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "OpenVault backend is alive!"

if __name__ == "__main__":
    app.run(debug=True, port=5000)
