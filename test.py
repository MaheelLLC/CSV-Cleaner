from main import clean_contact

contact = {
    "id": "1",
    "name": "  fatima  ",
    "email": " FATIMA@example.com ",
    "age": "19",
    "city": ""
}

result = clean_contact(contact)

assert result["name"] == "Fatima"
assert result["city"] == "Unknown"
assert result["age"] == 19

contact = {
    "id": "2",
    "name": "",
    "email": "test@example.com",
    "age": "25",
    "city": "Riyadh"
}

assert clean_contact(contact) is None