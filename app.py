from flask import Flask
from api.routes import ingest, status

app = Flask(__name__)

app.add_url_rule("/ingest", "ingest", ingest, methods=["POST"])
app.add_url_rule("/status/<ingestion_id>", "status", status, methods=["GET"])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
