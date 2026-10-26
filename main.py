import csv

def load_contacts(
        file_path : str,
) -> list[dict]:
    with open(file_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        return list(reader)


def clean_contact(contact : dict) -> dict | None:
    contact = contact.copy()

    contact['name'] = contact['name'].strip().title()
    if not contact['name']:
        return None

    contact['email'] = contact['email'].strip().lower()
    email = contact['email']

    # Ensure exactly one @ symbol exists
    if email.count('@') != 1:
        return None

    # Separate username and domain
    username, domain = email.split('@')

    # Ensure both components exist
    if not domain or not username:
        return None

    # reject whitespace
    if any(char.isspace() for char in email):
        return None

    # validate domain structure
    domain_parts = domain.split('.')
    if len(domain_parts) < 2 or '' in domain_parts:
        return None

    try:
        contact['age'] = int(contact['age'])
    except (ValueError, TypeError):
        return None
    
    if not (0 <= contact['age'] <= 120):
        return None

    contact['city'] = contact['city'].strip().title() or "Unknown"

    return contact


def process_contacts(contacts : list) -> tuple[list[dict], int, int]:
    new_contacts = []
    invalid = 0
    duplicate = 0
    emails = set()

    for contact in contacts:
        cleaned = clean_contact(contact)
        if not cleaned:
            invalid += 1
            continue

        if cleaned['email'] in emails:
            duplicate += 1
            continue
        
        emails.add(cleaned['email'])
        new_contacts.append(cleaned)

    return new_contacts, invalid, duplicate

def save_contacts(contacts : list, file_path : str) -> None:
    fieldnames = ['id', 'name', 'email', 'age', 'city']
    with open(file_path, mode='w', newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)

def main():
    input_file = 'data/raw_contacts.csv'
    output_file = 'data/clean_contacts.csv'
    try:
        contacts = load_contacts(input_file)
    except FileNotFoundError:
        print(f"Error: Could not find {input_file}")
        return
    processed_contacts, invalid, duplicate = process_contacts(contacts)
    save_contacts(processed_contacts, output_file)
    print('CSV Data Cleaner\n------------------------')
    print(f'Total contacts read: {len(contacts)}')
    print(f'Valid contacts saved: {len(processed_contacts)}')
    print(f'Invalid contacts skipped: {invalid}')
    print(f'Duplicate contacts removed: {duplicate}\n')
    print(f"Cleaned data saved to:\n{output_file}")

if __name__ == "__main__":
    main()


# Old Code
# if '..' in domain or domain[0] == '.' or domain[-1] == '.' \
#     or domain.count('.') < 1:
#     return None
# grab how many characters are before the @
# cool part is: the @'s index is zero-based, therefore the count before @
# which is 1-based is equal to @'s index
# length_before_at = at_index
# the number of characters after @ equals the (1-based) total number of 
# characters minus (0-based) @'s index minus 1 (shifts @'s index to 1-based)
# length_after_at = len(email) - at_index - 1
# if length_before_at == 0 or length_after_at == 0:
#     return None

# before_period = len(email[at_index:period_index]) - 1
# after_period = len(email[period_index:]) - 1
# if before_period == 0 or after_period == 0:
#     return None

# email_after_at = email[at_index + 1:]
# if email_after_at[0] == '.' or email[-1] == '.':
#     return None

# if '..' in email_after_at or '.' not in email_after_at:
#     return None

# period_indices = [index for index, char in enumerate(email_after_at) if char == '.']
# if 0 in period_indices or (len(email_after_at) - 1) in period_indices or not period_indices:
#     return None
# if not contact['city']:
#     contact['city'] = "Unknown"