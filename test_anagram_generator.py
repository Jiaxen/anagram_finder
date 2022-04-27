import anagram_generator
import pytest


@pytest.fixture
def new_anagram_generator():
    return anagram_generator.AnagramGenerator()


def test_clean_word(new_anagram_generator):
    assert new_anagram_generator.clean_word('A.bC  D%2tzf') == 'abcdtzf'


def test_anagram_generator(new_anagram_generator, capsys):
    input_word = 'onmayd'
    new_anagram_generator.min_word_length = 5
    new_anagram_generator.load_word_list("word_list/words_alpha.txt")
    new_anagram_generator.generate_anagram(input_word)
    captured = capsys.readouterr()
    assert captured.out == "amydon\ndynamo\nmonday\n"