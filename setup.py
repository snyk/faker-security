from setuptools import find_packages, setup

with open("README.md") as fp:
    long_description = fp.read()

CLASSIFIERS = [
    "Intended Audience :: Developers",
    "License :: MIT",
    "Operating System :: Unix",
    "Operating System :: POSIX",
    "Operating System :: Microsoft :: Windows",
    "Programming Language :: Python",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Topic :: Utilities",
]

setup(
    name="faker_security",
    version="0.1",
    license="MIT",
    description="Provider of security related data for Faker",
    long_description=long_description,
    author="Snyk",
    author_email="security@snyk.io",
    url="https://github.com/snyk/faker-security",
    packages=find_packages("faker_security"),
    package_dir={"": "faker_security"},
    py_modules=["faker_security.providers"],
    include_package_data=True,
    zip_safe=True,
    classifiers=CLASSIFIERS,
    python_requires=">=3.9",
    install_requires=["Faker>=8.2.1"],
    test_requires=["pytest"],
)
