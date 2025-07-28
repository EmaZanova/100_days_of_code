# Import custom module
from convertor import Convertor

# Import #rd party modules
from unidecode import unidecode

C = Convertor()

run = True

while run:
    # Ask for conversion type
    convert_to = input(
        "If you want to convert a message to Morse code, enter 'm'.\nIf you want to convert a message to text, enter 'ch'.\n"
    ).lower()

    # Ask for the message
    message = unidecode(input("Enter your message:\n"))

    try:
        converted_message = C.convert(
            input=message, convert_to=convert_to
        )  # Convert the message
    except Exception:
        print(
            "There is something wrong with your input. Please try again and follow the instructions."
        )
        continue

    print("Here is your converted message:")
    print(converted_message)

    # Ask the user if they want to continue
    again = input("\nDo you want me to translate another message? (Y/n):\n").lower()

    if again == "n":
        run = False
