import pandas as pd


class Convertor:
    def __init__(self):
        self.df = pd.read_csv(filepath_or_buffer="data.csv")

    def convert(self, input: str, convert_to: str) -> str:
        """This method converts text from Morse code to the alphabet or from the alphabet to Morse code.

        Args:
            input (str): Your message (in Morse code or in the alphabet).
            convert_to (str): If you want to convert your message to Morse code, set this argument to 'm' (for 'Morse').
                              If you want to translate Morse code to text, enter 'ch' (for 'character').

        Raises:
            Exception: Raises an exception with the message 'Wrong convert_to parameter' if you set the convert_to argument incorrectly.

        Returns:
            str: Your converted message.
        """

        # Set parameters
        if convert_to == "m":
            translation = ["ch", "m"]  # From alphabet to Morse code
            space = [" ", "/"]
        elif convert_to == "ch":
            translation = ["m", "ch"]  # From Morse code to alphabet
            space = ["/", " "]
        else:
            raise Exception("Wrong convert_to parameter")

        words = input.split(
            space[0]
        )  # Split the message using the correct "space" separator

        translated_message = []
        for word in words:  # Iterate through all words in the message
            translated_word = ""
            if convert_to == "ch":
                word = word.split()
            for char in word:
                index = self.df.loc[
                    self.df[translation[0]] == char.upper()
                ].index  # Find character index
                if convert_to == "m":
                    add_space = " "
                else:
                    add_space = ""
                translated_word += (
                    self.df[translation[1]][index[0]] + add_space
                )  # Find the character by index
            translated_message.append(translated_word)
        return space[1].join(translated_message)  # Return the converted message
