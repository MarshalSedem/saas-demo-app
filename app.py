from flask import Flask
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return f"""
    <h1>Innovartus SaaS Demo</h1>
    <p>Status: Running</p>
    <p>Server time: {datetime.datetime.now()}</p>
    """

@app.route("/health")
def health():
    return {"status": "ok"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)