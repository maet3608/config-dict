"""
Configuration dictionary
"""

import json


class Config(dict):
    """
    Store configuration data in dictionary and access via dot notation.

    >>> contact = Config({"address": {"street": "Baker St", "number": 221}})

    >>> print(contact['address']['number'])  # the traditional way
    221

    >>> print(contact.address.number)  # much nicer
    221

    >>> print(contact.address)  # pretty printing of content
    {
      "number": 221,
      "street": "Baker St"
    }

    >>> contact.address.number = 111  # update of values
    >>> print(contact.address)
    {
      "number": 111,
      "street": "Baker St"
    }

    >>> contact.address = Config({"street": "Downing", "number": 12})
    >>> print(contact.address.street)
    Downing
    """

    def __init__(self, *args, **kwargs):
        """ Construct the same way a plain Python dict is created. """
        wrap = lambda v: Config(v) if type(v) is dict else v
        kvdict = {k: wrap(v) for k, v in dict(*args, **kwargs).items()}
        super(Config, self).__init__(kvdict)
        self.__dict__ = self

    @staticmethod
    def load(filepath):
        """Load configuration from given JSON filepath"""
        with open(filepath) as f:
            return Config(json.load(f))

    def save(self, filepath):
        """Save configuration to given JSON filepath"""
        with open(filepath, 'w') as f:
            json.dump(self, f, indent=2)

    def __repr__(self):
        """Pretty string representation of configuration"""
        return json.dumps(self, sort_keys=True, indent=2)
