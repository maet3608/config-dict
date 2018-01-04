# Configuration dictionary

A dictionary class to hold configuration data. Operates the same way as a plain
Python dictionary but allows to access data via dot notation instead of
brackets with key values.

## Example

Creating a configuration dictionary

```python
>>> contact = Config({"address": {"street": "Baker St", "number": 221}})
```

and accessing data the 'traditional' way:

```python
>>> print(contact['address']['number'])
221
```

Much more readable using dot notation:

```python
>>> print(contact.address.number)
221
```

Pretty printing is supported

```python
>>> print(contact.address)
{
  "number": 221,
  "street": "Baker St"
}
```

and configuration values can be updated

```python
>>> contact.address.number = 111
>>> print(contact.address)
{
  "number": 221,
  "street": "Baker St"
}
```

Just watch out when updating non-primitive values. Dictionaries need to be
wrapped into `Config`:

```python
>>> contact.address = Config({"street": "Downing", "number": 12})
>>> print(contact.address.street)
Downing
```

Finally, configurations can be loaded from and save to JSON files

```python
contact = Config.load('contactdata.json')
contact.save('contactdata.json')
```

