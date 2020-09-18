from pydantic import BaseModel


class ContactModel(BaseModel):
	full_name:str
	phone_number :str



class UserModel(BaseModel):
	full_name:str 
	age:int
	phone_number : str
	contact: int