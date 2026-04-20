from ....interfaces.signupInterface import signup_interface

def signup_view(request): 
    return signup_interface(request)
