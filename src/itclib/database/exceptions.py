class NullsDataframe(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class FormatPointlist(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class EmptyPointlist(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)

class CustomError(Exception):
    def __init__(self, message: str):
        self.message = message
        super().__init__(self.message)