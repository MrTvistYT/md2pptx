class UndefinedFormat(Exception):
    def __init__(self, message):
        self.message = "Undefined slide format: "
        super().__init__(self.message)
