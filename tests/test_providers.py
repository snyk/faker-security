import re


class TestVersion:
    def test_correct_default(self, faker):
        version = faker.version()
        assert version

    def test_major_range(self, faker):
        version = faker.version(major_range=(4, 8))
        assert version

    def test_minor_range(self, faker):
        version = faker.version(minor_range=(4, 8))
        assert version

    def test_patch_range(self, faker):
        version = faker.version(patch_range=(4, 8))
        assert version

    def test_specific_major(self, faker):
        version = faker.version(major_range=(4, 4))
        assert version.startswith("4.")

    def test_specific_minor(self, faker):
        version = faker.version(minor_range=(6, 6))
        assert ".6." in version

    def test_specific_patch(self, faker):
        version = faker.version(patch_range=(8, 8))
        assert version.endswith(".8")


class TestSnykId:
    pattern = r"^SNYK-[A-Z]+-[A-Z0-9]+-\d+$"

    def test_correct_default(self, faker):
        snyk_id = faker.snyk_id()
        assert re.match(self.pattern, snyk_id)

    def test_suffix_range(self, faker):
        snyk_id = faker.snyk_id(suffix_range=(1030, 8000))
        assert re.match(self.pattern, snyk_id)

    def test_specific_suffix(self, faker):
        snyk_id = faker.snyk_id(suffix_range=(80, 80))
        assert re.match(self.pattern, snyk_id)
        assert snyk_id.endswith("-80")


class TestNpmSemverRange:
    def test_correct_default(self, faker):
        semver = faker.npm_semver_range()
        assert semver


class TestCwe:
    def test_correct_default(self, faker):
        cwe = faker.cwe()
        assert cwe

    def test_range(self, faker):
        cwe = faker.cwe(range=(80, 85))
        assert cwe


class TestCve:
    def test_correct_default(self, faker):
        cve = faker.cve()
        assert cve

    def test_year_range(self, faker):
        cve = faker.cve(year_range=(2010, 2014))
        assert cve

    def test_specific_year(self, faker):
        cve = faker.cve(year_range=(2013, 2013))
        assert cve.startswith("CVE-2013-")


class TestCVSSv3:
    def test_correct_default(self, faker):
        cvssv3 = faker.cvss3()
        assert cvssv3


class TestCVSSv2:
    def test_correct_default(self, faker):
        cvssv2 = faker.cvss2()
        assert cvssv2
