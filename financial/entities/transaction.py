import uuid
from datetime import datetime


class Transaction:
    def __init__(self, from_account: str, to_account: str, amount: float):
        self.transaction_id = str(uuid.uuid4())[:12]
        self.from_account = from_account
        self.to_account = to_account
        self.amount = amount
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"Transaction({self.transaction_id}, From={self.from_account}, To={self.to_account}, Amount={self.amount}, Date={self.timestamp})"
