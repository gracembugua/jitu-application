#Master Yoda, a renowned Jedi Master from the Star Wars universe, is known
#for his unique way of speaking. He often reverses the order of words in his
#sentences.
def yoda(sentence):
    words = sentence.split()
    reversed_words = words[::-1]
    reversed_sentence = ' '.join(reversed_words)
    return reversed_sentence

if __name__ == "__main__":
    input_sentence = input("Enter a sentence: ")
    yoda_sentence = yoda(input_sentence)
    print(f"Yoda speaks: {yoda_sentence}")
