class Stoplight(object):
    def __int__(self, code):
        self.inputs = []
        self.code = code

    def push(self, val):
        self.inputs.append(val)

    def get(self):
        return ''.join(self.inputs)

    def validate(self):
        calculated = self.get()
        return calculated == self.code

    def reset(self):
        self.inputs = []
