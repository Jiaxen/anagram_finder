from anagram_generator import AnagramGenerator


def main():
    anagram_generator = AnagramGenerator()
    anagram_generator.min_word_length = 4
    anagram_generator.load_word_list("word_list/words_alpha.txt")
    anagram_generator.generate_anagram("onmayd")


if __name__ == "__main__":
    main()
