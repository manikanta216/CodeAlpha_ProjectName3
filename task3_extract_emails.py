"""
TASK 3: Task Automation with Python Scripts
Idea chosen: Extract all email addresses from a .txt file and save them to another file.

Usage:
    python task3_extract_emails.py

The script will prompt for an input .txt file path, then extract all
email addresses found in it and save the unique results to an output file.
"""

import re
import os

EMAIL_PATTERN = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"


def extract_emails_from_file(input_path):
    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        content = f.read()

    emails = re.findall(EMAIL_PATTERN, content)

    # Remove duplicates while preserving order, and normalize case
    seen = set()
    unique_emails = []
    for email in emails:
        key = email.lower()
        if key not in seen:
            seen.add(key)
            unique_emails.append(email)

    return unique_emails


def save_emails(emails, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        for email in emails:
            f.write(email + "\n")


def main():
    print("=" * 50)
    print("EMAIL EXTRACTOR")
    print("=" * 50)

    input_path = input("Enter path to the input .txt file: ").strip()

    if not os.path.isfile(input_path):
        print(f"Error: File not found -> {input_path}")
        return

    emails = extract_emails_from_file(input_path)

    if not emails:
        print("No email addresses found in the file.")
        return

    print(f"\nFound {len(emails)} unique email address(es):")
    for email in emails:
        print(f"  - {email}")

    default_output = "extracted_emails.txt"
    output_path = input(
        f"\nEnter output file name (press Enter for '{default_output}'): "
    ).strip() or default_output

    save_emails(emails, output_path)
    print(f"\nSaved {len(emails)} email(s) to '{output_path}'")


if __name__ == "__main__":
    main()
