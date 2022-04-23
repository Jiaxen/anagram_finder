from anagram_generator import AnagramNode

def main():
    anagram_generator = AnagramNode()
    anagram_generator.load_word_list('word_list/words_alpha.txt')
    print(anagram_generator.children)

if __name__ == '__main__':
    main()