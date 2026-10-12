from flask import Flask, jsonify
import requests

app = Flask(__name__)

servers = [
    "http://127.0.0.1:5001",
    "http://127.0.0.1:5002",
    "http://127.0.0.1:5003"
]

current = 0
request_count = 0

stats = {
    "Server 1": 0,
    "Server 2": 0,
    "Server 3": 0
}


@app.route("/")
def home():
    global current, request_count

    request_count += 1

    server = servers[current]

    stats[f"Server {current + 1}"] += 1

    print(f"Request {request_count} --> {server}")

    current = (current + 1) % len(servers)

    response = requests.get(server)

    return response.text


@app.route("/stats")
def statistics():
    return jsonify(stats)


if __name__ == "__main__":
    app.run(port=8000)