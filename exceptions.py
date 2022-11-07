class CustomException(Exception):
    def __init__(self, message: str) -> None:
        self.base_message = message

    def __str__(self) -> str:
        return self.base_message
    

class WrongGridSizeException(CustomException):
    def __init__(self, message='') -> None:
        self.message = 'Row and column count must be the same. '
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()

class MissingGridSizeException(CustomException):
    def __init__(self, message='') -> None:
        self.message = 'Missing or wrong dimensions of the grid. '
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()

class WrongRowInputException(CustomException):
    def __init__(self, message='') -> None:
        self.message = 'Missing or wrong input in row. '
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()

class CannotMapToIntegerException(CustomException):
    def __init__(self, message='') -> None:
        self.message = 'Cannot map to number. '
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()

class NoEmptySpaceFoundException(CustomException):
    def __init__(self, message='') -> None:
        self.message = "Didn't find empty space in given numbers."
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()

class NumbersOutOfRangeException(CustomException):
    def __init__(self, message='') -> None:
        self.message = "Numbers out of range. "
        self.base_message = self.message if not message else self.message + str(message)

    def __str__(self) -> str:
        return super().__str__()