# Faker-Security

Provider for [Faker](https://github.com/joke2k/faker)
to generate random/fake data related to security.

## Requirements

- Faker
- Python 3.8+

## Installation and Usage

- Add `faker-security` to your requirements
- Install `faker-security` using `pip` or whatever package manager you use
- Add the `SecurityProvider` during tests or wherever you use Faker

```python
from faker import Faker
from faker_security.providers import SecurityProvider

fake = Faker()
fake.add_provider(SecurityProvider)

# generate a CVSSv3 vector
fake.cvss3()
```

## Provider Features

- `cvss3`: generates a CVSS v3 vector
- `cvss2`: generates a CVSS v2 vector
- `version`: generates a [semver version number](https://semver.org/)
- `npm_semver_range`: generates a [npm compatible semver version range](https://docs.npmjs.com/about-semantic-versioning)
- `cwe`: generates a CWE identifier
- `cve`: generates a CVE identifier

## Developing

- Install `poetry` and run `poetry install`
- Install `pre-commit` and run `pre-commit install --install-hooks`

## Testing

`poetry run pytest` to run tests.
