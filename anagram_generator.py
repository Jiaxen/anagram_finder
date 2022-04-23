import re
from collections import Counter


class AnagramGenerator:
    min_word_length = 3

    def __init__(self):
        self.root_node = AnagramNode()

    def load_word_list(self, path):
        with open(path, "r") as f:
            for word in f.readlines():
                word = self.clean_word(word)
                if len(word) > self.min_word_length:
                    self.load_letters(word)

    def load_letters(self, word):
        node = self.root_node
        for index, letter in enumerate(word):
            if letter not in node.children:
                node.children[letter] = AnagramNode(
                    letter=letter, depth=node.depth + 1, leaf=(index == len(word) - 1)
                )
            node = node.children[letter]

    def generate_anagram(self, input_word):
        input_word = self.clean_word(input_word)
        letter_count = Counter(input_word)
        word_len = len(input_word)
        for anagram in self.generate_anagram_helper(letter_count, [], self.root_node, word_len):
            print(anagram)

    def generate_anagram_helper(self, letter_count, builder, node, target_length):
        if node.leaf:
            if len([x for x in builder if x != ' ']) >= target_length:
                yield "".join(builder)
            builder.append(" ")
            for res in self.generate_anagram_helper(letter_count, builder, self.root_node, target_length):
                yield res
            builder.pop()
        for letter, sub_node in node.children.items():
            if letter not in letter_count.keys() or letter_count[letter] == 0:
                continue
            letter_count[letter] -= 1
            builder.append(letter)
            for res in self.generate_anagram_helper(letter_count, builder, sub_node, target_length):
                yield res
            builder.pop()
            letter_count[letter] += 1

    @staticmethod
    def clean_word(word):
        word = word.lower()
        word = re.sub(r"[^a-z]", "", word)
        return word


class AnagramNode:
    def __init__(self, letter="", depth=0, leaf=False):
        self.letter = letter
        self.depth = depth
        self.leaf = leaf
        self.children = {}
