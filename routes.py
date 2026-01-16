import uuid
from flask import request, jsonify
from adapters.json_adapter import parse_json
from adapters.xml_adapter import parse_xml
from core.domain.ingestion import Ingestion
from core.pipeline.ingestion_pipeline import IngestionPipeline
from core.pipeline.worker_pool import WorkerPool
from core.storage.ingestion_store import IngestionStore

store = IngestionStore()
pipeline = IngestionPipeline(store)
workers = WorkerPool()

def ingest():
    if "file" not in request.files:
        return jsonify({"error": "File missing"}), 400

    file_type = request.args.get("type", "json")
    file = request.files["file"]

    metadata = parse_json(file) if file_type == "json" else parse_xml(file)

    ingestion = Ingestion(
        ingestion_id=str(uuid.uuid4()),
        partner_id=metadata["partner_id"]
    )

    store.save(ingestion)
    workers.submit(pipeline.execute, ingestion, metadata)

    return jsonify({"ingestion_id": ingestion.ingestion_id}), 202


def status(ingestion_id):
    record = store.get(ingestion_id)
    if not record:
        return jsonify({"error": "Not found"}), 404
    return jsonify(record)
