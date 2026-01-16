class IngestionError(Exception):
    pass

class MetadataError(IngestionError):
    pass

class VideoValidationError(IngestionError):
    pass
