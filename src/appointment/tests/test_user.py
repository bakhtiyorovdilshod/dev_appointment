import uuid
import json
import pytest
from ..models.users import  User, Contact

def test_user(client):
	full_name = "Dilshod"
	phone_number = "+998998323249"
	age = 22
	contact = Contact.create(full_name=full_name, phone_number=phone_number)
	contact_id = contact.pk
	response = client.post("/create/user/", json=dict(full_name=full_name, age=age, phone_number=phone_number, contact=contact_id))
	response.raise_for_status()