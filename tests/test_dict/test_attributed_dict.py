import pytest

from assistypes.dict import AttributedDict


def test_dict_behavior():
    person = AttributedDict({"name": "John", "surname": "Smith"})
    assert person["name"] == "John"
    assert person["surname"] == "Smith"

    person["name"] = "Calvin"
    assert person == AttributedDict({"name": "Calvin", "surname": "Smith"})

    person.pop("name")
    assert person == AttributedDict({"surname": "Smith"})


def test_correct_attributes():
    person = AttributedDict({"name": "Jay-Jay", "surname": "Okocha"})
    assert person.name == "Jay-Jay"
    assert person.surname == "Okocha"

    person.name = "Alex"
    assert person == AttributedDict({"name": "Alex", "surname": "Okocha"})

    del person.name
    assert person == AttributedDict({"surname": "Okocha"})


def test_convert_child_dict_to_attributed():
    order = AttributedDict({
        "id": 123,
        "customer_id": 456,
        "products": {
            "bread": {"cost": 50},
            "milk": {"cost": 100},
        }
    })

    assert isinstance(order.products, AttributedDict)
