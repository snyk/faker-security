# Faker-Security

[![Pypi](https://badge.fury.io/py/faker-security.svg)](https://pypi.org/project/faker-security/)
[![CircleCI](https://circleci.com/gh/snyk/faker-security/tree/main.svg?style=svg)](https://circleci.com/gh/snyk/faker-security/tree/main)

Provider for [Faker](https://github.com/joke2k/faker)
to generate random/fake data related to security.

## Requirements

- Faker
- Python 3.8+

## Installation and Usage

If you want to use `faker-security` within your project, add it to your dependency file of choice.

This is typically your project's `requirements.txt` file. If you are using a higher-level package manager like `poetry` or `pipenv`, follow their instructions for adding new packages.

Once installed, you need to setup `Faker` to make use of the `SecurityProvider`. An example of how that could be done is shown below:

```python
from faker import Faker
from faker_security.providers import SecurityProvider

fake = Faker()
fake.add_provider(SecurityProvider)

# generate a CVSSv3 vector
fake.cvss3()
```

## Provider Features

- `cvss4`: generates a CVSS v4 vector
- `cvss3`: generates a CVSS v3 vector
- `cvss2`: generates a CVSS v2 vector
- `ccss`: generates a CCSS vector
- `version`: generates a [semver version number](https://semver.org/)
- `npm_semver_range`: generates a [npm compatible semver version range](https://docs.npmjs.com/about-semantic-versioning)
- `cwe`: generates a CWE identifier
- `cve`: generates a CVE identifier

## Developing

- Install `poetry` and run `poetry install`
- Install `pre-commit` and run `pre-commit install --install-hooks`

## Testing

`poetry run pytest` to run tests.
