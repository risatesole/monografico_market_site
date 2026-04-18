from ..error import EmptyStringError

def validateStringIsNotEmpty(text):
    if not text:
        raise EmptyStringError("Value Should not be empty")
