from context import search
import unittest

class BasicTestSuite(unittest.TestCase):

    global isf
    global corpus
    global corpus_complex

    corpus = 'The quick brown fox jumped over the lazy dog'
    corpus_complex = 'When in the Course of human events, it becomes necessary for one people to dissolve the political bands which have connected them with another, and to assume among the powers of the earth, the separate and equal station to which the Laws of Nature and of Nature\'s God entitle them, a decent respect to the opinions of mankind requires that they should declare the causes which impel them to the separation'
    isf = search.Search()

    def test_searchSimple(self):
        result = isf.searchSimple(corpus, 'brown')
        self.assertTrue(result, True)
    
    def test_forward_searchJoint(self):
        result = isf.searchJoint(corpus_complex, 'decent', 'respect', '1',  5)
        self.assertEqual(result, 5)

    def test_twoway_searchJoint(self):
        result = isf.searchJoint(corpus_complex, 'respect', 'decent', '2', 5)
if __name__ == '__main__':
    unittest.main()


