#  extracting some word of a string

text = "hello world!"
print(f"text:{text}")

def demonstrate_slicing():
    text = "hello to the world!!"
    print("slicing of text")
    first_word = text[:5]
    print(f"first word:{first_word}")
    #print("\nfirst word:", first_word)

    second_word = text[5:]
    print(f"second word:{second_word}")

if __name__ == "__main__":
    print("\npython string slicing:")
    demonstrate_slicing ()