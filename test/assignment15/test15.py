import unittest
from python_assignments.src.assignment15.util import word_occ

def word_occ(n, words):
    word_count = {}
    distinct_words = []
    occurrences = []

    for word in words:
        if word not in word_count:
            word_count[word] = 1
            distinct_words.append(word)
        else:
            word_count[word] += 1

    for distinct_word in distinct_words:
        occurrences.append(str(word_count[distinct_word]))

    return len(distinct_words), ' '.join(occurrences)

class TestWordOccurrences(unittest.TestCase):
    def test_example(self):
        n = 4
        words = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
        distinct_count, occurrences_list = word_occ(n, words)
        self.assertEqual(distinct_count, 3)
        self.assertEqual(occurrences_list, '2 1 1')

if __name__ == '__main__':
    unittest.main()
