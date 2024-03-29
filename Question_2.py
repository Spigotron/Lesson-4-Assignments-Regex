import re

text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"
emails = re.findall(r"[A-Za-z0-9._%+-]+@(?!exclude.com)[A-Za-z0-9.-]+", text)
print(emails)