#Design a function that takes a string or sequence of characters as input and
#returns the character that appears most frequently
def frequent(p):
    frequency = {}
    for char in p:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    max_freq = 0
    max_char = None
    for char, freq in frequency.items():
        if freq > max_freq:
            max_freq = freq
            max_char = char

    return max_char



if __name__ == "__main__":
    input_str = input("Enter a string: ")
    result = frequent(input_str)
    print(f"The most frequent character is: '{result}'")
