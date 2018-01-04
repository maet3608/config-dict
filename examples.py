"""
Usage examples for the config dictionary
"""

from config import Config

contact = Config({"address": {"street": "Baker St", "number": 221}})

print(contact.address.street)
print(contact.address.number)

contact.address.number = 111
print(contact.address)

contact.address = Config({"street": "Downing", "number": 12})
print(contact.address)

contact.save('contactdata.json')
contact = Config.load('contactdata.json')
print(contact)