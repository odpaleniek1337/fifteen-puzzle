class CustomException(Exception):
    def __init__(self, message: str) -> None:
        self.base_message = message

    def __str__(self) -> str:
        return self.base_message
    

class WrongGridSize(CustomException):
    def __init__(self, message='') -> None:
        self.message = 'Row and column count must be the same. '
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()

class MissingGridSize(CustomException):
    def __init__(self, message='') -> None:
        self.message = 'Missing or wrong dimensions of the grid. '
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()

class WrongRowInput(CustomException):
    def __init__(self, message='') -> None:
        self.message = 'Missing or wrong input in row. '
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()