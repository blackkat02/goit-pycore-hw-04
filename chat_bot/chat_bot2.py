import re


def phone_number(phon_number: str) -> str:
    """
    Normalizes a phone number to a standard format (+38XXXXXXXXX).
    Args:
        phon_number (str): The phone number in any format (e.g., 0501234567, +380501234567, (050) 123-45-67).
    Returns:
        str: The normalized phone number in standard format (+38XXXXXXXXX).
    Raises:
        ValueError: If the phone number cannot be normalized (e.g., contains non-numeric characters besides whitespace and parentheses).
    """
    pattern = r"[^\d\s()+-]"
    modified_number = re.sub(pattern, "", phon_number.strip())
    if not modified_number.startswith("+38"):
        modified_number = "+38" + modified_number
    return modified_number


def add_contact(args: list[str], contacts: dict) -> str:
    """
    Adds a new contact to the phonebook.
    Args:
        args (list[str]): A list of arguments containing the name and phone number.
        contacts (dict): A dictionary storing contact names as keys and phone numbers as values.
    Returns:
        str: A message indicating the success or failure of adding the contact, or an error message if the input is invalid.
    """
    if len(args) != 2:
        return "Invalid input. Usage: add [name] [phone]"
    name, phone = args
    if name in contacts:
        return "This name already exists in your contacts."
    else:
        try:
            phone = phone_number(phone)
            contacts[name] = phone
            return f"Contact {name}: {phone} added."
        except ValueError as e:
            return str(e)


def change_contact(args: list[str], contacts: dict) -> str:
    """
    Changes the phone number of an existing contact.
    Args:
        args (list[str]): A list of arguments containing the name and new phone number.
        contacts (dict): A dictionary storing contact names as keys and phone numbers as values.

    Returns:
        str: A message indicating the success or failure of changing the contact, or an error message if the input
        is invalid.
    """
    if len(args) != 2:
        return "Invalid input. Usage: change [name] [new phone]"
    name, new_phone = args

    if name not in contacts:
        return "Contact not found."
    else:
        try:
            new_phone = phone_number(new_phone)
            contacts[name] = new_phone
            return f"Contact {name}: {new_phone} updated."
        except ValueError as e:
            return str(e)
