def parse_input(user_input: str) -> tuple[str, list[str]]:
    """
    Parses user input into a command and arguments.
    Args:
        user_input (str): The user's input string.
    Returns:
        tuple[str, list[str]]: A tuple containing the command (lowercase and stripped) and a list of arguments.
    """
    cmd, *args = user_input.split()
    return cmd.strip().lower(), args


def show_contact(args: list[str], contacts: dict) -> str:
    """
    Displays the phone number of a contact.
    Args:
        args (list[str]): A list of arguments containing the name of the contact to display.
        contacts (dict): A dictionary storing contact names as keys and phone numbers as values.
    Returns:
        str: The phone number of the contact, or a message indicating that the contact was not found.
    """
    if len(args) != 1:
        return "Invalid input. Usage: phone [name]"
    name = args[0]


def show_all(contacts: dict):
    if contacts:
        return "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
    else:
        return "Контакти відсутні"