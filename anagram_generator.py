import re


class AnagramGenerator:
    def __init__(self):
        self.root_node = AnagramNode()

    def load_word_list(self, path):
        with open(path, 'r') as f:
            for word in f.readlines():
                word = word.lower()
                word = re.sub(r"[^a-z]", "", word)
                self.load_letters(word)

    def load_letters(self, word):
        node = self.root_node
        for index, letter in enumerate(word):
            if letter not in node.children:
                node.children[letter] = AnagramNode(letter=letter, depth=node.depth+1, leaf=(index == len(word)-1))
            node = node.children[letter]

    def generate_anagram(self, input_word):
        pass

class AnagramNode:
    def __init__(self, letter='', depth=0, leaf=False):
        self.letter = letter
        self.depth = depth
        self.leaf = leaf
        self.children = {}
