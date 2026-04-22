from ...models.model_user import User

class emailExistsError(Exception):
    pass


class UserService:
    def deactivateUser(self):
        raise NotImplementedError("This method is not implemented")
    
    def activateUser(self):
        raise NotImplementedError("This method is not implemented")
    
    def createCustomer(self,first_name,last_name,email,password):
        if User.objects.filter(email=email).exists():
            raise emailExistsError("This email is alrreddy in use")
        
        user = User.objects.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            role="customer",
            status="active"
        )
        return user


    def createEmployee(self):
        raise NotImplementedError("This method is not implemented")
    
    def createProvider(self):
        raise NotImplementedError("This method is not implemented")

    def setUserRoleCustomer(self,userid):
        raise NotImplementedError("This method is not implemented")

    
    def setUserRoleEmployee(self):
        raise NotImplementedError("This method is not implemented")
    
    def setUserRoleProvider(self):
        raise NotImplementedError("This method is not implemented")
    
    def getUserRole(self,userid):
        raise NotImplementedError("This method is not implemented")
    
    def isUserEmployee(self,userid):
        raise NotImplementedError("This method is not implemented")
    
    def isUserCustomer(self,userid):
        raise NotImplementedError("This method is not implemented")
    
    def isUserProvider(self,userid):
        raise NotImplementedError("This method is not implemented")
