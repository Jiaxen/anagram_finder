import re


class AnagramNode:
    def __init__(self, letter='', depth=0, leaf=False):
        self.letter = letter
        self.depth = depth
        self.leaf = leaf
        self.children = {}

    def load_word(self, word):
        node = self
        for index, letter in enumerate(word):
            if letter not in node.children:
                node.children[letter] = AnagramNode(letter=letter, depth=node.depth+1, leaf=(index == len(word)-1))
            node = node.children[letter]

    def load_word_list(self, path):
        with open(path, 'r') as f:
            for word in f.readlines():
                word = word.lower()
                word = re.sub(r"[^a-z]", "", word)
                self.load_word(word)

    def generate_anagrams(self):
        pass

