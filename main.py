from anagram_generator import AnagramGenerator


def main():
    anagram_generator = AnagramGenerator()
    anagram_generator.min_word_length = 4
    anagram_generator.load_word_list("word_list/words_simple.txt")
    while True:
        input_word = input('Find the anagram of: ')
        if not input_word:
            break
        anagram_generator.generate_anagram(input_word)


if __name__ == "__main__":
    main()
