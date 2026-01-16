from core.domain.states import IngestionState

class Ingestion:
    def __init__(self, ingestion_id, partner_id):
        self.ingestion_id = ingestion_id
        self.partner_id = partner_id
        self.state = IngestionState.RECEIVED
        self.reason = None

    def transition(self, state):
        self.state = state

    def fail(self, reason):
        self.state = IngestionState.FAILED
        self.reason = reason
