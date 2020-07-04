class Transaction:
    def __init__(self, amount, sender, recipient):
        self.amount = amount
        self.sender = sender
        self.recipient = recipient
    def __repr__(self):
        return (
            "\n" +
            "\t{\n" +
            f"\tamount: {self.amount}\n" +
            f"\tsender: {self.sender}\n" +
            f"\trecipient: {self.recipient}\n" +
            "\t}"
        )
    def get(self):
        ret = {"amount": self.amount, "sender": self.sender, "recipient": self.recipient}
        return ret