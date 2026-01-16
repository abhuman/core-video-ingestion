from core.validators.validator import Validator
from core.contracts.metadata_contract import REQUIRED_FIELDS
from core.domain.errors import MetadataError

class MetadataValidator(Validator):
    def validate(self, metadata):
        for field, dtype in REQUIRED_FIELDS.items():
            if field not in metadata:
                raise MetadataError(f"Missing field: {field}")
            if not isinstance(metadata[field], dtype):
                raise MetadataError(f"Invalid type: {field}")
