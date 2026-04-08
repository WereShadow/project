import re

def detect_pii(data):
    findings = {}

    for col in data.columns:
        sample_values = data[col].astype(str)

        email_pattern = r'\S+@\S+'
        phone_pattern = r'\b\d{10}\b'

        email_found = sample_values.str.contains(email_pattern).any()
        phone_found = sample_values.str.contains(phone_pattern).any()

        findings[col] = {
            "email_detected": email_found,
            "phone_detected": phone_found
        }

    return findings