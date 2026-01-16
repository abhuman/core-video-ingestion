import json
import os

DB_PATH = "data/ingestion_db.json"

class IngestionStore:
    def _load(self):
        if not os.path.exists(DB_PATH):
            return {}
        with open(DB_PATH) as f:
            return json.load(f)

    def save(self, ingestion):
        db = self._load()
        db[ingestion.ingestion_id] = {
            "partner_id": ingestion.partner_id,
            "state": ingestion.state.value,
            "reason": ingestion.reason
        }
        with open(DB_PATH, "w") as f:
            json.dump(db, f, indent=4)

    def get(self, ingestion_id):
        return self._load().get(ingestion_id)
