from chat_bot2 import add_contact, change_contact
from chat_bot3 import parse_input, show_contact, show_all


def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_contact(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "show_cont":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()