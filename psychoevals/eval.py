import uuid

class Eval:
    def __init__(self, prompt, meta):
        self._id = str(uuid.uuid4())
        self.prompt = prompt
        self.meta = meta

    def __str__(self):
        return f"ID: {self._id}\nPrompt: {self.prompt}\nMeta: {self.meta}"

    def __repr__(self):
        return f"Eval(_id='{self._id}', prompt='{self.prompt}', meta='{self.meta}')"
