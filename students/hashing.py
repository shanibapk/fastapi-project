# from passlib.context import CryptContext



# pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# class Hash:
#     @staticmethod
#     def bcrypt(password: str):
#         return pwd_context.hash(password)

#     @staticmethod
#     def verify( hashed_password,plain_password):
#         return pwd_context.verify(plain_password, hashed_password)

from passlib.context import CryptContext

pwd_context=CryptContext(schemes=["bcrypt"],deprecated="auto")

class Hash():
    def bcrypt(password:str):
         return pwd_context.hash(password)
    
    def verify(hashed_password,plainpassword):
        return pwd_context.verify(plainpassword,hashed_password)   


