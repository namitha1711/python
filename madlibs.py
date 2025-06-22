import re

def mad_libs(input_file, output_file):
    text = open(input_file).read()
    for part in ["ADJECTIVE", "NOUN", "ADVERB", "VERB"]:
        while part in text:
            word = input(f"Enter {'an' if part[0] in 'AEIOU' else 'a'} {part.lower()}: ")
            text = text.replace(part, word, 1)
    print(text)
    open(output_file, "w").write(text)

if __name__ == "__main__":
    mad_libs("madlib_input.txt", "madlib_output.txt")
