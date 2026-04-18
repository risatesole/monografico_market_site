from .......utils import normalizeStringToLowerCase, validateStringIsNotEmpty 
from .validateEmailFormat import validateEmailFormat

class EmailValueObject:
    """
    Value Object representing a validated email address.
    """
    def __init__(self, email: str):
        validateStringIsNotEmpty(email) # type: ignore
        normalizedEmail = normalizeStringToLowerCase(email)
        validateEmailFormat(normalizedEmail)
        self._value = normalizedEmail

    def get_value(self) -> str:
        return self._value
