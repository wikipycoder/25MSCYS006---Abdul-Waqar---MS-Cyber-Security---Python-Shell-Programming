import re

def find_phone_numbers(text):
    pattern = r'(\+\d{1,3})?[\s.-]?\(?\d{2,4}\)?[\s.-]?\d{3,4}[\s.-]?\d{3,4}'
    
    matches = re.findall(pattern, text)
    if matches:
        print(f"Found the following phone numbers:")
        full_matches = re.finditer(pattern, text)
        for match in full_matches:
            print(f"- {match.group(0)}")
    else:
        print("No phone numbers found.")

text_to_search = """
Please contact us at 123-456-7890 for support.
International callers can reach us at +44-20-1234-5678.
Our other line is (555) 888-9999.
Pakistani Number: +923163194314
You can also dial +1 987 654 3210.
Invalid number: 12345.
"""

find_phone_numbers(text_to_search)
