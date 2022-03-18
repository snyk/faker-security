Faker-Security
==============

Add on provider for [Faker](https://github.com/joke2k/faker)
to generate random/fake data related to security.

Requirements
------------

* Faker
* Python 3.9+

Installation and Usage
----------------------

* Add `faker-security` to your requirements
* Install `faker-security` using `pip` or whatever package manager you use
* Add the `SecurityProvider` during tests or wherever you use Faker

```python
from faker import Faker
from faker_security.providers import SecurityProvider

fake = Faker()
fake.add_provider(SecurityProvider)

# generate a CVSSv3 vector
fake.cvss3()
```

Developing
----------

Install `poetry` and run `poetry install`

`poetry run pytest` to run tests.
