# TODO implement + test
from anonymizers.anonymizer import AnonymizerAbstract


class Replace(AnonymizerAbstract):
    def __init__(self, new_text: str):
        self.new_text = new_text

    def anonymize(self):
        pass
