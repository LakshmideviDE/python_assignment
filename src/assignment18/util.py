import re

def filter_valid_emails(n, emails):
    pattern = re.compile(r'^[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')
    valid_emails = sorted(filter(lambda email: bool(pattern.match(email)), emails))
    return valid_emails
