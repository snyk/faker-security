import pytest
from faker import Faker

from faker_security.providers import SecurityProvider


@pytest.fixture(scope="session")
def faker():
    faker = Faker()
    faker.add_provider(SecurityProvider)
    yield faker
