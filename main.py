from anagram_generator import AnagramGenerator

def main():
    anagram_generator = AnagramGenerator()
    anagram_generator.load_word_list('word_list/words_alpha.txt')
    print(anagram_generator.root_node.children)

if __name__ == '__main__':
    main()