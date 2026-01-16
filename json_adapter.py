import json
import tempfile

def parse_json(file):
    tmp = tempfile.NamedTemporaryFile(delete=False)
    file.save(tmp.name)
    with open(tmp.name) as f:
        return json.load(f)
