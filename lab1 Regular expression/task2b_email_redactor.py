import re

def redact_emails(text_block):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    redacted_text = re.sub(email_pattern, '[EMAIL_REDACTED]', text_block)

    print("==== Original Text ===")
    print(text_block)
    print("\n=== Redacted Text ===")
    print(redacted_text)
    return redacted_text

sample_log = """
A user with the email waqar.baloch@example.com has reported a problem.
Kindly share the issue details with the admin team at admin@my-company.net.
For any additional help, reach out to support-team@help.org.
Note that the leak originated from test_user_waqar@gmail.com
and not from any internal account.”
"""

redact_emails(sample_log)
