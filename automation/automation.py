import re

with open("assets/potential-contacts.txt", "r") as f:
    text_from_file = f.read()
with open("assets/existing-contacts.txt", "r") as f:
    existing_contacts = f.read()

email_pattern = r"\w+@[\w.]+"
phone_pattern = r"\s*(?:\+?(\d{1,3}))?[-. (]*(\d{3})[-. )]*(\d{3})[-. ]*(\d{4})(?: *(x\d+))?\s*"
emails = re.findall(email_pattern, text_from_file)
phone_numbers = re.findall(phone_pattern, text_from_file)

# combine the parts of the tuple returned
phone_numbers_combined = []
for x in phone_numbers:
    phone_numbers_combined.append(str(x[1]) + "-" + str(x[2]) + "-" + str(x[3]) + str(x[4]))

# remove duplicates by putting into set
phone_numbers_combined = set(phone_numbers_combined)
emails = set(emails)

with open('results/phone_numbers.txt', 'w')as f:
    for x in phone_numbers_combined:
        if x not in existing_contacts:
            f.write(x + "\n")

with open('results/emails.txt', 'w')as f:
    for x in emails:
        if x not in existing_contacts:
            f.write(x + "\n")

print(f"{len(emails)} unique emails found ")
print(f"{len(phone_numbers_combined)} unique phone numbers found ")
