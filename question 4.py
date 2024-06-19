#Design a function that determines whether a given string is a pangram.
import string
def is_pangram(s):
    alphabet_set = set(string.ascii_lowercase)
    input_set = set(char.lower() for char in s if char.isalpha())
    return alphabet_set <= input_set
if __name__ == "__main__":
    input_str = input("Enter a string to check if it's a pangram: ")
    if is_pangram(input_str):
        print(f"'{input_str}' is a pangram.")
    else:
        print(f"'{input_str}' is not a pangram.")
