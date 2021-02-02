import uuid


class Utils:
    # generate a string w/ random characters in a fixed length of 20
    @staticmethod
    def generate_random_string():
        return uuid.uuid4().hex[:20]
