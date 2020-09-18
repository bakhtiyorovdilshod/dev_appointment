from fastapi import APIRouter
from pydantic import BaseModel

from ..models.users import User, Contact
from ..models.pydantic_model import ContactModel,UserModel

router = APIRouter()


@router.post("/create/contact/")
async def create_contact(contact: ContactModel):
    contact = await Contact.create(full_name=contact.full_name, phone_number=contact.phone_number)
    return contact.to_dict()


@router.get("/contact/{uid}/")
async def get_contact(uid:int):
    contact = await Contact.get_or_404(uid)
    return contact.to_dict()


@router.delete("/contact/{uid}/delete/")
async def delete_contact(uid: int):
    contact = await Contact.get_or_404(uid)
    await contact.delete()
    return dict(id=uid)


@router.post("/create/user/")
async def create_user(user:UserModel):
    contact_id = user.contact
    get_contact = await Contact.select('id').where(Contact.id == contact_id).gino.scalar()
    user = await User.create(full_name=user.full_name, age=user.age, phone_number=user.phone_number, contact=get_contact)
    return user.to_dict()


@router.get("/user/{uid}/")
async def get_user(uid:int):
    user = await User.get_or_404(uid)
    return user.to_dict()

@router.delete("/user/{uid}/delete/")
async def delete_user(uid:int):
    user = await User.get_or_404(uid)
    await user.delete()
    return dict(id=uid)



def init_app(app):
    app.include_router(router)