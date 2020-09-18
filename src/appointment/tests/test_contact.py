import uuid
import json
import pytest

def test_contact(client):
    full_name = "Dilshod"
    phone_number = "+998998323249"
    response = client.post("/create/contact/", json=dict(full_name=full_name, phone_number=phone_number))

    response.raise_for_status()
    
    url = f"/contact/{response.json()['id']}"
    assert client.get(url).json()['full_name'] == full_name


    url = f"/contact/{response.json()['id']}/delete/"
    client.delete(url).raise_for_status()
    assert client.delete(url).status_code == 404