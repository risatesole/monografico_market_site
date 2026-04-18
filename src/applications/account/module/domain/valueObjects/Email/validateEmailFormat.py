from .......error import EmailShouldHaveAtSymbolError , InvalidEmailError

def validateEmailFormat(email: str) -> None:
    if "@" not in email:
        raise EmailShouldHaveAtSymbolError("Email must contain '@'")
    if email.count("@") != 1:
        raise InvalidEmailError("Email must contain only one '@'")
    local, domain = email.split("@")
    if not local or not domain:
        raise InvalidEmailError("Email must have local and domain parts")
    if "." not in domain:
        raise InvalidEmailError("Domain must contain '.'")
