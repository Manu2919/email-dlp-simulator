import re

# Define sensitive patterns
patterns = {
    "PAN Number": r"[A-Z]{5}[0-9]{4}[A-Z]",
    "Credit Card Number": r"\b(?:\d[ -]*?){13,16}\b",
    "Sensitive Keywords": r"\b(confidential|password|salary|ssn)\b"
}

def scan_content(content):
    violations = []
    for label, pattern in patterns.items():
        if re.search(pattern, content, re.IGNORECASE):
            violations.append(label)
    return violations

def is_external_email(to_email, company_domain="yourcompany.com"):
    return not to_email.lower().endswith("@" + company_domain)

def apply_policy(to_email, content):
    violations = scan_content(content)
    if violations and is_external_email(to_email):
        return False, violations
    return True, violations
