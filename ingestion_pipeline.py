from core.domain.states import IngestionState
from core.validators.metadata_validator import MetadataValidator
from core.validators.video_validator import VideoValidator

class IngestionPipeline:
    def __init__(self, store):
        self.store = store
        self.metadata_validator = MetadataValidator()
        self.video_validator = VideoValidator()

    def execute(self, ingestion, metadata):
        try:
            ingestion.transition(IngestionState.VALIDATING_METADATA)
            self.store.save(ingestion)

            self.metadata_validator.validate(metadata)

            ingestion.transition(IngestionState.VALIDATING_VIDEO)
            self.store.save(ingestion)

            self.video_validator.validate(metadata["video_path"])

            ingestion.transition(IngestionState.PASSED)

        except Exception as e:
            ingestion.fail(str(e))

        self.store.save(ingestion)
