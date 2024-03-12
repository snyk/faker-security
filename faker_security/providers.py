"""
Custom providers for the Faker library that help generate random data within
our factories.
"""

import random
from typing import Tuple

from faker import Faker
from faker.providers import BaseProvider

fake = Faker()


class SecurityProvider(BaseProvider):
    def version(
        self,
        major_range: Tuple[int, int] = (1, 10),
        minor_range: Tuple[int, int] = (1, 10),
        patch_range: Tuple[int, int] = (1, 10),
    ):
        major = random.randint(*major_range)
        minor = random.randint(*minor_range)
        patch = random.randint(*patch_range)
        return f"{major}.{minor}.{patch}"

    def snyk_id(self, suffix_range: Tuple[int, int] = (1000, 90000)):
        ecosystem = random.choice(["python", "java", "ruby", "dotnet"]).upper()
        slug = fake.slug().replace("-", "").upper()
        suffix = random.randint(*suffix_range)
        return f"SNYK-{ecosystem}-{slug}-{suffix}"

    def npm_semver_range(self):
        version = self.version()
        operator = random.choice(["=", "<", ">", "<=", ">="])
        return f"{operator}{version}"

    def cwe(self, range: Tuple[int, int] = (1, 1000)):
        value = random.randint(*range)
        return f"CWE-{value}"

    def cve(self, year_range: Tuple[int, int] = (1990, 2024)):
        year = random.randint(*year_range)
        number = random.randint(1000, 9999)
        return f"CVE-{year}-{number}"

    def cvss4(self):
        # values obtained from:
        # https://www.first.org/cvss/calculator/4.0
        attack_vector = random.choice("NALP")
        attack_complexity = random.choice("LH")
        attack_requirements = random.choice("NP")
        priviliges_required = random.choice("NLH")
        user_interaction = random.choice("NPA")
        confidentiality_vulnerable_system = random.choice("NLH")
        integrity_vulnerable_system = random.choice("NLH")
        availability_vulnerable_system = random.choice("NLH")
        confidentiality_subsequent_system = random.choice("NLH")
        integrity_subsequent_system = random.choice("NLH")
        availability_subsequent_system = random.choice("NLH")
        return (
            "CVSS:4.0/"
            f"AV:{attack_vector}/"
            f"AC:{attack_complexity}/"
            f"AT:{attack_requirements}/"
            f"PR:{priviliges_required}/"
            f"UI:{user_interaction}/"
            f"VC:{confidentiality_vulnerable_system}/"
            f"VI:{integrity_vulnerable_system}/"
            f"VA:{availability_vulnerable_system}/"
            f"SC:{confidentiality_subsequent_system}/"
            f"SI:{integrity_subsequent_system}/"
            f"SA:{availability_subsequent_system}"
        )

    def cvss3(self):
        # values obtained from:
        # https://www.first.org/cvss/calculator/3.1
        attack_vector = random.choice("NALP")
        attack_complexity = random.choice("LH")
        privileges_required = random.choice("NLH")
        user_interaction = random.choice("NR")
        scope = random.choice("UC")
        confidentiality = random.choice("NLH")
        integrity = random.choice("NLH")
        availability = random.choice("NLH")
        return (
            "CVSS:3.1/"
            f"AV:{attack_vector}/"
            f"AC:{attack_complexity}/"
            f"PR:{privileges_required}/"
            f"UI:{user_interaction}/"
            f"S:{scope}/"
            f"C:{confidentiality}/"
            f"I:{integrity}/"
            f"A:{availability}"
        )

    def cvss2(self):
        # values obtained from:
        # https://nvd.nist.gov/vuln-metrics/cvss/v2-calculator

        # base metric scores
        access_vector = random.choice("LAN")
        access_complexity = random.choice("HML")
        authentication = random.choice("MSN")
        confidentiality = random.choice("NPC")
        integrity_impact = random.choice("NPC")
        availability_impact = random.choice("NPC")

        result = "/".join(
            [
                f"AV:{access_vector}",
                f"AC:{access_complexity}",
                f"Au:{authentication}",
                f"C:{confidentiality}",
                f"I:{integrity_impact}",
                f"A:{availability_impact}",
            ]
        )

        return f"({result})"

    def ccss(self):
        # values obtained from:
        # https://nvlpubs.nist.gov/nistpubs/Legacy/IR/nistir7502.pdf

        # base metric scores
        access_vector = random.choice("LAN")
        access_complexity = random.choice("HML")
        authentication = random.choice("MSN")
        confidentiality = random.choice("NPC")
        integrity_impact = random.choice("NPC")
        availability_impact = random.choice("NPC")
        privilege_level = random.choice(["R", "U", "A", "ND"])
        exploitation_method = random.choice("AP")

        return "/".join(
            [
                f"AV:{access_vector}",
                f"AC:{access_complexity}",
                f"Au:{authentication}",
                f"C:{confidentiality}",
                f"I:{integrity_impact}",
                f"A:{availability_impact}",
                f"PL:{privilege_level}",
                f"EM:{exploitation_method}",
            ]
        )
