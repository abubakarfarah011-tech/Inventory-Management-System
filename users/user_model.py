class User:
    def __init__(self,email,password):
        self.__email = email
        self.__password = password
        

    def get_email(self):
        return self.__email
 
 
    def get_password(self):
         return self.__password
    
    
    def set_password(self, new_password):
         self.__password = new_password
        
    def to_dict(self):
        return {
            "email": self.__email,
            "password": self.__password
        }